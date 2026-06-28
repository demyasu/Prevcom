import requests
import json
import os
from datetime import datetime
from data import GROUPS_DATA

API_BASE = "https://worldcup26.ir"
CACHE_FILE = os.path.join(os.path.dirname(__file__), "api_cache.json")
CACHE_TTL = 600

SESSION = requests.Session()
SESSION.verify = True

EN_TO_PT = {
    "Mexico": "México", "South Africa": "África do Sul", "South Korea": "Coreia do Sul",
    "Czech Republic": "República Tcheca", "Canada": "Canadá", "Bosnia and Herzegovina": "Bósnia e Herzegovina",
    "Qatar": "Catar", "Switzerland": "Suíça", "Brazil": "Brasil", "Morocco": "Marrocos",
    "Haiti": "Haiti", "Scotland": "Escócia",     "USA": "Estados Unidos", "United States": "Estados Unidos", "Australia": "Austrália",
    "Paraguay": "Paraguai", "Turkey": "Turquia", "Germany": "Alemanha", "Curacao": "Curaçao",
    "Ivory Coast": "Costa do Marfim", "Ecuador": "Equador", "Netherlands": "Holanda",
    "Japan": "Japão", "Sweden": "Suécia", "Tunisia": "Tunísia", "Belgium": "Bélgica",
    "Egypt": "Egito", "Iran": "Irã", "New Zealand": "Nova Zelândia", "Spain": "Espanha",
    "Cape Verde": "Cabo Verde", "Saudi Arabia": "Arábia Saudita", "Uruguay": "Uruguai",
    "France": "França", "Norway": "Noruega", "Senegal": "Senegal", "Iraq": "Iraque",
    "Argentina": "Argentina", "Algeria": "Argélia", "Jordan": "Jordânia", "Austria": "Áustria",
    "Colombia": "Colômbia", "Portugal": "Portugal", "Uzbekistan": "Uzbequistão",
    "DR Congo": "RD Congo", "Democratic Republic of the Congo": "RD Congo", "Croatia": "Croácia", "England": "Inglaterra", "Ghana": "Gana",
    "Panama": "Panamá",
}

_cache = None

def _load_cache():
    global _cache
    if _cache is not None:
        return _cache
    if os.path.exists(CACHE_FILE):
        try:
            with open(CACHE_FILE, "r") as f:
                _cache = json.load(f)
            return _cache
        except:
            pass
    _cache = {}
    return _cache

def _save_cache(data):
    global _cache
    _cache = data
    try:
        with open(CACHE_FILE, "w") as f:
            json.dump(data, f, indent=2)
    except:
        pass

def _is_cache_valid():
    cache = _load_cache()
    if not cache.get("last_update"):
        return False
    try:
        last = datetime.fromisoformat(cache["last_update"])
        return (datetime.now() - last).total_seconds() < CACHE_TTL
    except:
        return False

def _api_get(path, timeout=15):
    try:
        resp = SESSION.get(f"{API_BASE}{path}", timeout=timeout)
        if resp.status_code == 200:
            return resp
    except requests.exceptions.SSLError:
        try:
            resp = requests.get(f"{API_BASE}{path}", timeout=timeout, verify=False)
            if resp.status_code == 200:
                return resp
        except:
            pass
    except:
        pass
    return None

def fetch_data(force=False):
    if not force and _is_cache_valid():
        return _load_cache()

    try:
        teams_resp = _api_get("/get/teams", timeout=10)
        groups_resp = _api_get("/get/groups", timeout=10)
        games_resp = _api_get("/get/games", timeout=30)

        if not teams_resp or not groups_resp or not games_resp:
            raise Exception("API returned non-200")

        teams_data = teams_resp.json().get("teams", [])
        groups_data = groups_resp.json().get("groups", [])
        games_data = games_resp.json().get("games", [])

        team_map = {}
        for t in teams_data:
            en_name = t["name_en"]
            pt_name = EN_TO_PT.get(en_name, en_name)
            team_map[t["id"]] = {
                "name": pt_name,
                "name_en": en_name,
                "flag": t.get("flag", ""),
                "fifa_code": t.get("fifa_code", ""),
                "group": t.get("groups", ""),
            }

        standings = {}
        for gd in groups_data:
            g = gd["name"]
            standings[g] = []
            for td in gd.get("teams", []):
                tid = td["team_id"]
                info = team_map.get(tid, {})
                standings[g].append({
                    "name": info.get("name", f"Team {tid}"),
                    "points": int(td.get("pts", 0)),
                    "played": int(td.get("mp", 0)),
                    "wins": int(td.get("w", 0)),
                    "draws": int(td.get("d", 0)),
                    "losses": int(td.get("l", 0)),
                    "gf": int(td.get("gf", 0)),
                    "ga": int(td.get("ga", 0)),
                    "gd": int(td.get("gd", 0)),
                })

        from data import GROUP_MATCHES
        TYPE_MAP = {"group": "G", "r32": "R32_", "r16": "R16_", "qf": "QF_", "sf": "SF_", "final": "FINAL", "third": "3RD"}
        en_to_pt_api = {v["name_en"]: v["name"] for v in team_map.values()}

        def _pt(en_name):
            return en_to_pt_api.get(en_name) or EN_TO_PT.get(en_name, en_name)

        match_scores = {}
        for gm in games_data:
            gtype = gm.get("type", "group")
            if gm.get("finished") == "TRUE":
                hs = int(gm.get("home_score", 0))
                aws = int(gm.get("away_score", 0))
                entry = {"home_score": hs, "away_score": aws, "status": "FINISHED"}
                api_home = _pt(gm.get("home_team_name_en", ""))
                api_away = _pt(gm.get("away_team_name_en", ""))

                if gtype == "group":
                    g = gm.get("group", "X")
                    if g in GROUP_MATCHES:
                        for local_m in GROUP_MATCHES[g]:
                            if local_m["home"] == api_home and local_m["away"] == api_away:
                                match_scores[local_m["id"]] = entry
                                break
                else:
                    prefix = TYPE_MAP.get(gtype, "X")
                    match_scores[f"{prefix}{gm.get('id', '0')}"] = entry

        games = []
        for gm in games_data:
            games.append({
                "id": gm.get("id"),
                "type": gm.get("type", "group"),
                "group": gm.get("group", ""),
                "home_team": _pt(gm.get("home_team_name_en", "")),
                "away_team": _pt(gm.get("away_team_name_en", "")),
                "home_score": int(gm.get("home_score", 0)),
                "away_score": int(gm.get("away_score", 0)),
                "status": gm.get("status", "not_started"),
                "finished": gm.get("finished", "FALSE"),
                "minute": gm.get("minute"),
                "datetime": gm.get("datetime", ""),
            })

        result = {
            "standings": standings,
            "match_scores": match_scores,
            "games": games,
            "team_map": team_map,
            "last_update": datetime.now().isoformat(),
        }
        _save_cache(result)
        return result

    except Exception as e:
        cache = _load_cache()
        if cache and "standings" in cache:
            return cache
        return {"standings": {}, "match_scores": {}, "games": [], "team_map": {}, "last_update": None, "error": str(e)}

def get_standings(force=False):
    data = fetch_data(force)
    api_standings = data.get("standings", {})
    standings = {}
    for g in "ABCDEFGHIJKL":
        local_teams = GROUPS_DATA[g]["teams"]
        api_teams = api_standings.get(g) if g in api_standings and api_standings[g] else []
        # Build lookup: API team name (already PT) -> stats
        api_lookup = {}
        for entry in api_teams:
            api_lookup[entry["name"]] = entry
        # Always return all local teams, merge API stats where name matches
        merged = []
        for lt in local_teams:
            name = lt["name"]
            if name in api_lookup:
                ap = api_lookup[name]
                merged.append({
                    "name": name, "points": ap["points"], "played": ap["played"],
                    "wins": ap["wins"], "draws": ap["draws"], "losses": ap["losses"],
                    "gf": ap["gf"], "ga": ap["ga"], "gd": ap["gd"],
                })
            else:
                merged.append({
                    "name": name, "points": 0, "played": 0,
                    "wins": 0, "draws": 0, "losses": 0,
                    "gf": 0, "ga": 0, "gd": 0,
                })
        merged.sort(key=lambda x: (-x["points"], -x["gd"], -x["gf"]))
        standings[g] = merged
    return standings

def get_match_scores(force=False):
    data = fetch_data(force)
    return data.get("match_scores", {})

def get_team_map(force=False):
    data = fetch_data(force)
    return data.get("team_map", {})

def get_games(force=False):
    data = fetch_data(force)
    return data.get("games", [])

def get_last_update():
    cache = _load_cache()
    return cache.get("last_update", None) if _is_cache_valid() else None
