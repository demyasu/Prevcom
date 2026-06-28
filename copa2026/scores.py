import json
import os

SCORES_FILE = os.path.join(os.path.dirname(__file__), "matches_data.json")

def load_scores():
    if os.path.exists(SCORES_FILE):
        try:
            with open(SCORES_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except:
            pass
    return {"matches": {}, "standings": {}, "last_update": None}

def save_score(match_id, home_score, away_score, status="FINISHED"):
    data = load_scores()
    data["matches"][match_id] = {
        "home_score": home_score,
        "away_score": away_score,
        "status": status,
        "updated_at": __import__("datetime").datetime.now().isoformat()
    }
    with open(SCORES_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    return data

def update_standings(standings):
    data = load_scores()
    data["standings"] = standings
    data["last_update"] = __import__("datetime").datetime.now().isoformat()
    with open(SCORES_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
