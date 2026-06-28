import os
import re
from datetime import datetime
from flask import Flask, render_template, jsonify, request, send_file
from data import GROUPS_DATA, BRACKET_MATCHUPS, KNOCKOUT_STAGES, MATCH_DATES, SUFFIX_LEGEND, GROUP_MATCHES, dia_semana
from utils import calcular_probabilidade, exportar_xlsx
from scores import load_scores, save_score
from worldcup_api import get_standings as api_standings, get_match_scores as api_scores, get_games as api_games, get_last_update

app = Flask(__name__)
app.secret_key = os.urandom(24).hex()

@app.context_processor
def inject_globals():
    return {"last_update": get_last_update(), "now": datetime.now()}

def grupo_para_nome(g):
    return f"Grupo {g}"

def format_date(d):
    if isinstance(d, dict):
        dt = d.get("date", "")
        dw = dia_semana(dt) if dt else ""
        if dw:
            return {**d, "date": f"{dw} {dt}"}
        return d
    return d

def merge_scores(api_scores_dict, local_scores_dict):
    merged = dict(api_scores_dict)
    for mid, data in local_scores_dict.items():
        if data.get("status") == "FINISHED":
            merged[mid] = data
    return merged

def resolver_chaveamento(standings, match_scores):
    """Resolve position codes (1A, 2B, 3C/D/E, WR32_1, WSF_1, etc.) to team names."""
    pos_map = {}
    for g in "ABCDEFGHIJKL":
        group = standings.get(g, [])
        for i, t in enumerate(group):
            pos_map[f"{i+1}{g}"] = t["name"]

    thirds = []
    for g in "ABCDEFGHIJKL":
        group = standings.get(g, [])
        if len(group) >= 3:
            thirds.append((g, group[2]))
    thirds.sort(key=lambda x: (-x[1]["points"], -x[1]["gd"], -x[1]["gf"]))
    advancing_thirds = {g for g, _ in thirds[:8]}

    def resolve_code(code, resolved_cache):
        if code in resolved_cache:
            return resolved_cache[code]
        if "/" in code:
            groups = re.split(r'[/,]', code[1:])
            candidates = [(g, t) for g, t in thirds if g in groups and g in advancing_thirds]
            if candidates:
                resolved_cache[code] = candidates[0][1]["name"]
                return resolved_cache[code]
            resolved_cache[code] = code
            return code
        if code in pos_map:
            resolved_cache[code] = pos_map[code]
            return pos_map[code]
        resolved_cache[code] = code
        return code

    def resolve_knockout(code, resolved_cache, bracket_lookup):
        if not (code.startswith("W") or code.startswith("L")):
            return resolve_code(code, resolved_cache)
        is_loser = code.startswith("L")
        source_id = code[1:]
        src = bracket_lookup.get(source_id)
        if src and source_id in match_scores:
            sm = match_scores[source_id]
            if sm.get("status") == "FINISHED":
                hs, aws = sm.get("home_score", 0), sm.get("away_score", 0)
                if hs != aws:
                    src_home = resolve_knockout(src["home"], resolved_cache, bracket_lookup)
                    src_away = resolve_knockout(src["away"], resolved_cache, bracket_lookup)
                    if hs > aws:
                        resolved_cache[code] = src_away if is_loser else src_home
                    else:
                        resolved_cache[code] = src_home if is_loser else src_away
                    return resolved_cache[code]
        resolved_cache[code] = code
        return code

    resolved_cache = {}
    bracket_lookup = {}
    for stage_key, matches in BRACKET_MATCHUPS.items():
        for m in matches:
            bracket_lookup[m["id"]] = m

    for stage_key in ["round_of_32", "round_of_16", "quarter_finals", "semi_finals", "third_place", "final"]:
        for m in BRACKET_MATCHUPS.get(stage_key, []):
            home_r = resolve_knockout(m["home"], resolved_cache, bracket_lookup)
            away_r = resolve_knockout(m["away"], resolved_cache, bracket_lookup)

    return resolved_cache

@app.route("/")
def index():
    api_sc = api_scores()
    local_sc = load_scores().get("matches", {})
    scores = merge_scores(api_sc, local_sc)
    standings = api_standings()
    grupos = []
    for g in "ABCDEFGHIJKL":
        grupos.append({
            "letra": g,
            "nome": grupo_para_nome(g),
            "times": GROUPS_DATA[g]["teams"],
            "classificacao": standings.get(g, []),
        })
    return render_template("index.html", grupos=grupos, group_matches=GROUP_MATCHES)

@app.route("/groups")
def groups():
    api_sc = api_scores()
    local_sc = load_scores().get("matches", {})
    scores = merge_scores(api_sc, local_sc)
    standings = api_standings()
    grupos = []
    for g in "ABCDEFGHIJKL":
        times_data = []
        for t in GROUPS_DATA[g]["teams"]:
            pos = next((i+1 for i, s in enumerate(standings.get(g, [])) if s["name"] == t["name"]), 0)
            stats = next((s for s in standings.get(g, []) if s["name"] == t["name"]), {})
            times_data.append({**t, "pos": pos, "stats": stats})
        grupos.append({"letra": g, "nome": grupo_para_nome(g), "times": times_data})
    group_dates = MATCH_DATES.get("group", {})
    group_dates_fmt = {g: [format_date(m) for m in matches] for g, matches in group_dates.items()}
    return render_template("groups.html", grupos=grupos, group_matches=GROUP_MATCHES, group_dates=group_dates_fmt, match_scores=scores)

@app.route("/ao-vivo")
def ao_vivo():
    games = api_games()
    standings = api_standings()
    finished_groups = set()
    for g in games:
        if g["type"] == "group" and g["finished"] == "TRUE":
            finished_groups.add(g["group"])

    # Build local match date lookup
    local_dates = {}
    for g_letra, matches in MATCH_DATES.get("group", {}).items():
        for m in matches:
            key = (m["home"], m["away"])
            local_dates[key] = m
    for stage, stage_matches in MATCH_DATES.get("knockout", {}).items():
        for mid, m in stage_matches.items():
            local_dates[mid] = m

    TYPE_MAP_REV = {"group": "G", "r32": "R32_", "r16": "R16_", "qf": "QF_", "sf": "SF_", "final": "FINAL", "third": "3RD"}
    for g in games:
        dt_str = g.get("datetime", "")
        matched = None
        if g["type"] == "group":
            key = (g["home_team"], g["away_team"])
            matched = local_dates.get(key)
        else:
            mid_prefix = TYPE_MAP_REV.get(g["type"], "")
            mid = f"{mid_prefix}{g.get('id', '')}"
            matched = local_dates.get(mid)
        if matched:
            g["date_formatted"] = matched.get("date", "")
            g["dia_semana"] = dia_semana(matched.get("date", ""))
            g["time_formatted"] = matched.get("time", "")
            g["venue"] = matched.get("venue", "")
        elif dt_str:
            try:
                dt = datetime.fromisoformat(dt_str.replace("Z", "+00:00"))
                g["date_formatted"] = dt.strftime("%d/%m")
                g["dia_semana"] = dia_semana(dt.strftime("%d/%m"))
                g["time_formatted"] = dt.strftime("%H:%M")
            except:
                g["date_formatted"] = ""
                g["dia_semana"] = ""
                g["time_formatted"] = ""
        else:
            g["date_formatted"] = ""
            g["dia_semana"] = ""
            g["time_formatted"] = ""
    grupos = []
    for g in "ABCDEFGHIJKL":
        grupos.append({
            "letra": g,
            "nome": grupo_para_nome(g),
            "times": GROUPS_DATA[g]["teams"],
            "classificacao": standings.get(g, []),
            "tem_jogos": g in finished_groups,
        })
    return render_template("ao-vivo.html", games=games, grupos=grupos)

@app.route("/bracket")
def bracket():
    local_sc = load_scores().get("matches", {})
    standings = api_standings()
    resolved_teams = resolver_chaveamento(standings, local_sc)
    bracket = {}
    for stage_key, stage_info in KNOCKOUT_STAGES.items():
        matches = BRACKET_MATCHUPS.get(stage_key, [])
        stage_dates = MATCH_DATES.get("knockout", {}).get(stage_key, {})
        bracket[stage_key] = {
            "name": stage_info["name"],
            "matches": [
                {
                    "id": m["id"],
                    "home": m["home"],
                    "away": m["away"],
                    "home_resolvido": resolved_teams.get(m["home"], m["home"]),
                    "away_resolvido": resolved_teams.get(m["away"], m["away"]),
                    "next": m["next"],
                    "date": stage_dates.get(m["id"], {}).get("date", ""),
                    "dia_semana": dia_semana(stage_dates.get(m["id"], {}).get("date", "")),
                    "time": stage_dates.get(m["id"], {}).get("time", ""),
                    "venue": stage_dates.get(m["id"], {}).get("venue", ""),
                    "home_score": local_sc.get(m["id"], {}).get("home_score"),
                    "away_score": local_sc.get(m["id"], {}).get("away_score"),
                    "status": local_sc.get(m["id"], {}).get("status", "SCHEDULED"),
                }
                for m in matches
            ]
        }
    last_update = get_last_update()
    return render_template("bracket.html", bracket=bracket, legend=SUFFIX_LEGEND, last_update=last_update)

@app.route("/probabilidade")
def probabilidade_page():
    home = request.args.get("home", "")
    away = request.args.get("away", "")
    if not home or not away:
        return render_template("probabilidade.html", prob=None)
    prob = calcular_probabilidade(home, away)
    return render_template("probabilidade.html", prob=prob)

@app.route("/api/atualizar")
def api_atualizar():
    from worldcup_api import fetch_data
    data = fetch_data(force=True)
    if data.get("standings"):
        return jsonify({"status": "ok", "updated": data.get("last_update")})
    return jsonify({"status": "error", "message": data.get("error", "Falha ao atualizar")}), 500

@app.route("/api/probabilidade")
def api_probabilidade():
    home = request.args.get("home", "")
    away = request.args.get("away", "")
    if not home or not away:
        return jsonify({"error": "Parâmetros home e away são obrigatórios"}), 400
    return jsonify(calcular_probabilidade(home, away))

@app.route("/api/probabilidades")
def api_probabilidades():
    stage = request.args.get("stage", "all")
    resultados = []
    for s in list(BRACKET_MATCHUPS.keys()):
        if stage != "all" and s != stage:
            continue
        for m in BRACKET_MATCHUPS[s]:
            prob = calcular_probabilidade(m["home"], m["away"])
            resultados.append({
                "stage": s,
                "match_id": m["id"],
                **prob
            })
    for g in "ABCDEFGHIJKL":
        for gm in GROUP_MATCHES[g]:
            prob = calcular_probabilidade(gm["home"], gm["away"])
            resultados.append({
                "stage": f"group_{g}",
                "match_id": gm["id"],
                **prob
            })
    return jsonify(resultados)

@app.route("/api/placar", methods=["POST"])
def api_placar():
    data = request.get_json()
    match_id = data.get("match_id")
    home_score = data.get("home_score")
    away_score = data.get("away_score")
    status = data.get("status", "FINISHED")
    if not all([match_id, home_score is not None, away_score is not None]):
        return jsonify({"error": "Dados incompletos"}), 400

    home_score = int(home_score)
    away_score = int(away_score)

    found = any(
        m["id"] == match_id
        for stage in BRACKET_MATCHUPS.values()
        for m in stage
    ) or any(
        m["id"] == match_id
        for g in GROUP_MATCHES.values()
        for m in g
    )
    if not found:
        return jsonify({"error": "Partida não encontrada"}), 404

    save_score(match_id, home_score, away_score, status)
    return jsonify({"status": "ok"})

@app.route("/api/placar/batch", methods=["POST"])
def api_placar_batch():
    data = request.get_json()
    resultados = data.get("resultados", [])
    for r in resultados:
        save_score(r["match_id"], int(r["home_score"]), int(r["away_score"]), r.get("status", "FINISHED"))
    return jsonify({"status": "ok", "count": len(resultados)})

@app.route("/exportar")
def exportar():
    try:
        from scores import load_scores
        filename = f"copa2026_chaveamento_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx"
        filepath = os.path.join(os.path.dirname(__file__), filename)
        standings = api_standings()
        api_sc = api_scores()
        local_sc = load_scores().get("matches", {})
        scores = merge_scores(api_sc, local_sc)
        exportar_xlsx(filepath, standings=standings, match_scores=scores)
        return send_file(filepath, as_attachment=True, download_name=filename)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
