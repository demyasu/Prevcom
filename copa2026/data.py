WEEKDAYS = ["Seg", "Ter", "Qua", "Qui", "Sex", "Sáb", "Dom"]

def dia_semana(data_str):
    """'11/06' -> 'Qui' (day of week in Portuguese, abbreviated)"""
    try:
        d, m = map(int, data_str.split("/"))
        from datetime import date
        return WEEKDAYS[date(2026, m, d).weekday()]
    except:
        return ""

GROUPS_DATA = {
    "A": {
        "teams": [
            {"name": "México", "ranking": 9, "confederation": "CONCACAF", "flag": "🇲🇽"},
            {"name": "República Tcheca", "ranking": 36, "confederation": "UEFA", "flag": "🇨🇿"},
            {"name": "África do Sul", "ranking": 57, "confederation": "CAF", "flag": "🇿🇦"},
            {"name": "Coreia do Sul", "ranking": 23, "confederation": "AFC", "flag": "🇰🇷"},
        ]
    },
    "B": {
        "teams": [
            {"name": "Canadá", "ranking": 40, "confederation": "CONCACAF", "flag": "🇨🇦"},
            {"name": "Bósnia e Herzegovina", "ranking": 62, "confederation": "UEFA", "flag": "🇧🇦"},
            {"name": "Catar", "ranking": 46, "confederation": "AFC", "flag": "🇶🇦"},
            {"name": "Suíça", "ranking": 15, "confederation": "UEFA", "flag": "🇨🇭"},
        ]
    },
    "C": {
        "teams": [
            {"name": "Brasil", "ranking": 5, "confederation": "CONMEBOL", "flag": "🇧🇷"},
            {"name": "Escócia", "ranking": 39, "confederation": "UEFA", "flag": "🏴󠁧󠁢󠁳󠁣󠁴󠁿"},
            {"name": "Haiti", "ranking": 85, "confederation": "CONCACAF", "flag": "🇭🇹"},
            {"name": "Marrocos", "ranking": 13, "confederation": "CAF", "flag": "🇲🇦"},
        ]
    },
    "D": {
        "teams": [
            {"name": "Estados Unidos", "ranking": 11, "confederation": "CONCACAF", "flag": "🇺🇸"},
            {"name": "Austrália", "ranking": 27, "confederation": "AFC", "flag": "🇦🇺"},
            {"name": "Paraguai", "ranking": 44, "confederation": "CONMEBOL", "flag": "🇵🇾"},
            {"name": "Turquia", "ranking": 28, "confederation": "UEFA", "flag": "🇹🇷"},
        ]
    },
    "E": {
        "teams": [
            {"name": "Alemanha", "ranking": 10, "confederation": "UEFA", "flag": "🇩🇪"},
            {"name": "Curaçao", "ranking": 90, "confederation": "CONCACAF", "flag": "🇨🇼"},
            {"name": "Costa do Marfim", "ranking": 41, "confederation": "CAF", "flag": "🇨🇮"},
            {"name": "Equador", "ranking": 30, "confederation": "CONMEBOL", "flag": "🇪🇨"},
        ]
    },
    "F": {
        "teams": [
            {"name": "Holanda", "ranking": 7, "confederation": "UEFA", "flag": "🇳🇱"},
            {"name": "Japão", "ranking": 18, "confederation": "AFC", "flag": "🇯🇵"},
            {"name": "Suécia", "ranking": 26, "confederation": "UEFA", "flag": "🇸🇪"},
            {"name": "Tunísia", "ranking": 32, "confederation": "CAF", "flag": "🇹🇳"},
        ]
    },
    "G": {
        "teams": [
            {"name": "Bélgica", "ranking": 6, "confederation": "UEFA", "flag": "🇧🇪"},
            {"name": "Egito", "ranking": 34, "confederation": "CAF", "flag": "🇪🇬"},
            {"name": "Irã", "ranking": 22, "confederation": "AFC", "flag": "🇮🇷"},
            {"name": "Nova Zelândia", "ranking": 104, "confederation": "OFC", "flag": "🇳🇿"},
        ]
    },
    "H": {
        "teams": [
            {"name": "Espanha", "ranking": 8, "confederation": "UEFA", "flag": "🇪🇸"},
            {"name": "Cabo Verde", "ranking": 72, "confederation": "CAF", "flag": "🇨🇻"},
            {"name": "Arábia Saudita", "ranking": 53, "confederation": "AFC", "flag": "🇸🇦"},
            {"name": "Uruguai", "ranking": 14, "confederation": "CONMEBOL", "flag": "🇺🇾"},
        ]
    },
    "I": {
        "teams": [
            {"name": "França", "ranking": 2, "confederation": "UEFA", "flag": "🇫🇷"},
            {"name": "Noruega", "ranking": 38, "confederation": "UEFA", "flag": "🇳🇴"},
            {"name": "Senegal", "ranking": 20, "confederation": "CAF", "flag": "🇸🇳"},
            {"name": "Iraque", "ranking": 59, "confederation": "AFC", "flag": "🇮🇶"},
        ]
    },
    "J": {
        "teams": [
            {"name": "Argentina", "ranking": 1, "confederation": "CONMEBOL", "flag": "🇦🇷"},
            {"name": "Argélia", "ranking": 33, "confederation": "CAF", "flag": "🇩🇿"},
            {"name": "Jordânia", "ranking": 71, "confederation": "AFC", "flag": "🇯🇴"},
            {"name": "Áustria", "ranking": 25, "confederation": "UEFA", "flag": "🇦🇹"},
        ]
    },
    "K": {
        "teams": [
            {"name": "Colômbia", "ranking": 12, "confederation": "CONMEBOL", "flag": "🇨🇴"},
            {"name": "Portugal", "ranking": 6, "confederation": "UEFA", "flag": "🇵🇹"},
            {"name": "Uzbequistão", "ranking": 65, "confederation": "AFC", "flag": "🇺🇿"},
            {"name": "RD Congo", "ranking": 63, "confederation": "CAF", "flag": "🇨🇩"},
        ]
    },
    "L": {
        "teams": [
            {"name": "Croácia", "ranking": 16, "confederation": "UEFA", "flag": "🇭🇷"},
            {"name": "Inglaterra", "ranking": 4, "confederation": "UEFA", "flag": "🏴󠁧󠁢󠁥󠁮󠁧󠁿"},
            {"name": "Gana", "ranking": 29, "confederation": "CAF", "flag": "🇬🇭"},
            {"name": "Panamá", "ranking": 47, "confederation": "CONCACAF", "flag": "🇵🇦"},
        ]
    }
}

ALL_TEAMS = []
for g, data in GROUPS_DATA.items():
    for t in data["teams"]:
        ALL_TEAMS.append({**t, "group": g})

GROUP_NAMES = {chr(ord('A')+i): f"Grupo {chr(ord('A')+i)}" for i in range(12)}

SUFFIX_LEGEND = {
    "R32": "16-avos de Final (Round of 32) — 1ª fase eliminatória com 32 seleções",
    "R16": "Oitavas de Final (Round of 16) — 2ª fase eliminatória com 16 seleções",
    "QF": "Quartas de Final (Quarter Finals) — 3ª fase eliminatória com 8 seleções",
    "SF": "Semifinais (Semi Finals) — 4ª fase eliminatória com 4 seleções",
    "FINAL": "Grande Final — Disputa do título",
    "3RD": "Disputa de 3º Lugar",
    "WR32": "Vencedor da partida R32 correspondente",
    "WR16": "Vencedor da partida R16 correspondente",
    "WQF": "Vencedor da partida QF correspondente",
    "WSF": "Vencedor da partida SF correspondente",
    "LSF": "Perdedor da partida SF correspondente",
    "1A": "1º colocado do Grupo A",
    "2A": "2º colocado do Grupo A",
    "3A/B/C": "Melhor 3º colocado entre grupos A, B e C",
}

MATCH_DATES = {
    "group": {
        "A": [
            {"date": "11/06", "time": "16:00", "home": "México", "away": "África do Sul", "venue": "Estádio Azteca (Cidade do México)"},
            {"date": "11/06", "time": "23:00", "home": "Coreia do Sul", "away": "República Tcheca", "venue": "Estádio Akron (Guadalajara)"},
            {"date": "18/06", "time": "13:00", "home": "República Tcheca", "away": "África do Sul", "venue": "Mercedes-Benz (Atlanta)"},
            {"date": "18/06", "time": "22:00", "home": "México", "away": "Coreia do Sul", "venue": "Estádio Akron (Guadalajara)"},
            {"date": "24/06", "time": "22:00", "home": "República Tcheca", "away": "México", "venue": "Estádio Azteca (Cidade do México)"},
            {"date": "24/06", "time": "22:00", "home": "África do Sul", "away": "Coreia do Sul", "venue": "Estádio BBVA (Monterrey)"},
        ],
        "B": [
            {"date": "12/06", "time": "16:00", "home": "Canadá", "away": "Bósnia e Herzegovina", "venue": "BMO Field (Toronto)"},
            {"date": "13/06", "time": "16:00", "home": "Catar", "away": "Suíça", "venue": "Levi's Stadium (San Francisco)"},
            {"date": "18/06", "time": "16:00", "home": "Suíça", "away": "Bósnia e Herzegovina", "venue": "SoFi Stadium (Los Angeles)"},
            {"date": "18/06", "time": "19:00", "home": "Canadá", "away": "Catar", "venue": "BC Place (Vancouver)"},
            {"date": "24/06", "time": "16:00", "home": "Suíça", "away": "Canadá", "venue": "BC Place (Vancouver)"},
            {"date": "24/06", "time": "16:00", "home": "Bósnia e Herzegovina", "away": "Catar", "venue": "Lumen Field (Seattle)"},
        ],
        "C": [
            {"date": "13/06", "time": "19:00", "home": "Brasil", "away": "Marrocos", "venue": "MetLife Stadium (Nova York/NJ)"},
            {"date": "13/06", "time": "22:00", "home": "Haiti", "away": "Escócia", "venue": "Gillette Stadium (Boston)"},
            {"date": "19/06", "time": "22:00", "home": "Brasil", "away": "Haiti", "venue": "Lincoln Financial (Filadélfia)"},
            {"date": "19/06", "time": "19:00", "home": "Escócia", "away": "Marrocos", "venue": "Gillette Stadium (Boston)"},
            {"date": "24/06", "time": "19:00", "home": "Escócia", "away": "Brasil", "venue": "Hard Rock Stadium (Miami)"},
            {"date": "24/06", "time": "19:00", "home": "Marrocos", "away": "Haiti", "venue": "Mercedes-Benz (Atlanta)"},
        ],
        "D": [
            {"date": "12/06", "time": "22:00", "home": "Estados Unidos", "away": "Paraguai", "venue": "SoFi Stadium (Los Angeles)"},
            {"date": "13/06", "time": "01:00", "home": "Austrália", "away": "Turquia", "venue": "BC Place (Vancouver)"},
            {"date": "19/06", "time": "01:00", "home": "Turquia", "away": "Paraguai", "venue": "Levi's Stadium (San Francisco)"},
            {"date": "19/06", "time": "16:00", "home": "Estados Unidos", "away": "Austrália", "venue": "Lumen Field (Seattle)"},
            {"date": "25/06", "time": "23:00", "home": "Turquia", "away": "Estados Unidos", "venue": "SoFi Stadium (Los Angeles)"},
            {"date": "25/06", "time": "23:00", "home": "Paraguai", "away": "Austrália", "venue": "Levi's Stadium (San Francisco)"},
        ],
        "E": [
            {"date": "14/06", "time": "14:00", "home": "Alemanha", "away": "Curaçao", "venue": "NRG Stadium (Houston)"},
            {"date": "14/06", "time": "20:00", "home": "Costa do Marfim", "away": "Equador", "venue": "Lincoln Financial (Filadélfia)"},
            {"date": "20/06", "time": "17:00", "home": "Alemanha", "away": "Costa do Marfim", "venue": "BMO Field (Toronto)"},
            {"date": "20/06", "time": "21:00", "home": "Equador", "away": "Curaçao", "venue": "Arrowhead (Kansas City)"},
            {"date": "25/06", "time": "17:00", "home": "Equador", "away": "Alemanha", "venue": "MetLife Stadium (Nova York/NJ)"},
            {"date": "25/06", "time": "17:00", "home": "Curaçao", "away": "Costa do Marfim", "venue": "Lincoln Financial (Filadélfia)"},
        ],
        "F": [
            {"date": "14/06", "time": "17:00", "home": "Holanda", "away": "Japão", "venue": "AT&T Stadium (Dallas)"},
            {"date": "14/06", "time": "23:00", "home": "Suécia", "away": "Tunísia", "venue": "Estádio BBVA (Monterrey)"},
            {"date": "20/06", "time": "14:00", "home": "Holanda", "away": "Suécia", "venue": "NRG Stadium (Houston)"},
            {"date": "21/06", "time": "01:00", "home": "Tunísia", "away": "Japão", "venue": "Estádio BBVA (Monterrey)"},
            {"date": "25/06", "time": "20:00", "home": "Tunísia", "away": "Holanda", "venue": "Arrowhead (Kansas City)"},
            {"date": "25/06", "time": "20:00", "home": "Japão", "away": "Suécia", "venue": "AT&T Stadium (Dallas)"},
        ],
        "G": [
            {"date": "15/06", "time": "16:00", "home": "Bélgica", "away": "Egito", "venue": "Lumen Field (Seattle)"},
            {"date": "15/06", "time": "22:00", "home": "Irã", "away": "Nova Zelândia", "venue": "SoFi Stadium (Los Angeles)"},
            {"date": "21/06", "time": "16:00", "home": "Bélgica", "away": "Irã", "venue": "SoFi Stadium (Los Angeles)"},
            {"date": "21/06", "time": "22:00", "home": "Nova Zelândia", "away": "Egito", "venue": "BC Place (Vancouver)"},
            {"date": "26/06", "time": "00:00", "home": "Egito", "away": "Irã", "venue": "Lumen Field (Seattle)"},
            {"date": "26/06", "time": "00:00", "home": "Nova Zelândia", "away": "Bélgica", "venue": "BC Place (Vancouver)"},
        ],
        "H": [
            {"date": "15/06", "time": "13:00", "home": "Espanha", "away": "Cabo Verde", "venue": "Mercedes-Benz (Atlanta)"},
            {"date": "15/06", "time": "19:00", "home": "Arábia Saudita", "away": "Uruguai", "venue": "Hard Rock Stadium (Miami)"},
            {"date": "21/06", "time": "13:00", "home": "Espanha", "away": "Arábia Saudita", "venue": "Mercedes-Benz (Atlanta)"},
            {"date": "21/06", "time": "19:00", "home": "Uruguai", "away": "Cabo Verde", "venue": "Hard Rock Stadium (Miami)"},
            {"date": "26/06", "time": "21:00", "home": "Uruguai", "away": "Espanha", "venue": "Estádio Akron (Guadalajara)"},
            {"date": "26/06", "time": "21:00", "home": "Cabo Verde", "away": "Arábia Saudita", "venue": "NRG Stadium (Houston)"},
        ],
        "I": [
            {"date": "16/06", "time": "16:00", "home": "França", "away": "Senegal", "venue": "MetLife Stadium (Nova York/NJ)"},
            {"date": "16/06", "time": "19:00", "home": "Iraque", "away": "Noruega", "venue": "Gillette Stadium (Boston)"},
            {"date": "22/06", "time": "18:00", "home": "França", "away": "Iraque", "venue": "Lincoln Financial (Filadélfia)"},
            {"date": "22/06", "time": "21:00", "home": "Noruega", "away": "Senegal", "venue": "MetLife Stadium (Nova York/NJ)"},
            {"date": "26/06", "time": "16:00", "home": "Noruega", "away": "França", "venue": "Gillette Stadium (Boston)"},
            {"date": "26/06", "time": "16:00", "home": "Senegal", "away": "Iraque", "venue": "BMO Field (Toronto)"},
        ],
        "J": [
            {"date": "16/06", "time": "22:00", "home": "Argentina", "away": "Argélia", "venue": "Arrowhead (Kansas City)"},
            {"date": "17/06", "time": "01:00", "home": "Áustria", "away": "Jordânia", "venue": "Levi's Stadium (San Francisco)"},
            {"date": "22/06", "time": "14:00", "home": "Argentina", "away": "Áustria", "venue": "AT&T Stadium (Dallas)"},
            {"date": "23/06", "time": "00:00", "home": "Jordânia", "away": "Argélia", "venue": "Levi's Stadium (San Francisco)"},
            {"date": "27/06", "time": "23:00", "home": "Jordânia", "away": "Argentina", "venue": "AT&T Stadium (Dallas)"},
            {"date": "27/06", "time": "23:00", "home": "Argélia", "away": "Áustria", "venue": "Arrowhead (Kansas City)"},
        ],
        "K": [
            {"date": "17/06", "time": "14:00", "home": "Portugal", "away": "RD Congo", "venue": "NRG Stadium (Houston)"},
            {"date": "17/06", "time": "23:00", "home": "Uzbequistão", "away": "Colômbia", "venue": "Estádio Azteca (Cidade do México)"},
            {"date": "23/06", "time": "14:00", "home": "Portugal", "away": "Uzbequistão", "venue": "NRG Stadium (Houston)"},
            {"date": "23/06", "time": "23:00", "home": "Colômbia", "away": "RD Congo", "venue": "Estádio Akron (Guadalajara)"},
            {"date": "27/06", "time": "20:30", "home": "Colômbia", "away": "Portugal", "venue": "Hard Rock Stadium (Miami)"},
            {"date": "27/06", "time": "20:30", "home": "RD Congo", "away": "Uzbequistão", "venue": "Mercedes-Benz (Atlanta)"},
        ],
        "L": [
            {"date": "17/06", "time": "17:00", "home": "Inglaterra", "away": "Croácia", "venue": "AT&T Stadium (Dallas)"},
            {"date": "17/06", "time": "20:00", "home": "Gana", "away": "Panamá", "venue": "BMO Field (Toronto)"},
            {"date": "23/06", "time": "17:00", "home": "Inglaterra", "away": "Gana", "venue": "Gillette Stadium (Boston)"},
            {"date": "23/06", "time": "20:00", "home": "Panamá", "away": "Croácia", "venue": "BMO Field (Toronto)"},
            {"date": "27/06", "time": "18:00", "home": "Panamá", "away": "Inglaterra", "venue": "MetLife Stadium (Nova York/NJ)"},
            {"date": "27/06", "time": "18:00", "home": "Croácia", "away": "Gana", "venue": "Lincoln Financial (Filadélfia)"},
        ],
    },
    "knockout": {
        "round_of_32": {
            "R32_1": {"date": "28/06", "time": "16:00", "venue": "SoFi Stadium (Los Angeles)"},
            "R32_2": {"date": "29/06", "time": "17:30", "venue": "Gillette Stadium (Boston)"},
            "R32_3": {"date": "29/06", "time": "14:00", "venue": "NRG Stadium (Houston)"},
            "R32_4": {"date": "29/06", "time": "22:00", "venue": "Estádio BBVA (Monterrey)"},
            "R32_5": {"date": "30/06", "time": "14:00", "venue": "AT&T Stadium (Dallas)"},
            "R32_6": {"date": "30/06", "time": "18:00", "venue": "MetLife Stadium (Nova York/NJ)"},
            "R32_7": {"date": "30/06", "time": "22:00", "venue": "Estádio Azteca (Cidade do México)"},
            "R32_8": {"date": "01/07", "time": "13:00", "venue": "Mercedes-Benz (Atlanta)"},
            "R32_9": {"date": "01/07", "time": "21:00", "venue": "Levi's Stadium (San Francisco)"},
            "R32_10": {"date": "01/07", "time": "17:00", "venue": "Lumen Field (Seattle)"},
            "R32_11": {"date": "02/07", "time": "20:00", "venue": "BMO Field (Toronto)"},
            "R32_12": {"date": "02/07", "time": "16:00", "venue": "SoFi Stadium (Los Angeles)"},
            "R32_13": {"date": "03/07", "time": "00:00", "venue": "BC Place (Vancouver)"},
            "R32_14": {"date": "03/07", "time": "19:00", "venue": "Hard Rock Stadium (Miami)"},
            "R32_15": {"date": "03/07", "time": "22:30", "venue": "Arrowhead (Kansas City)"},
            "R32_16": {"date": "03/07", "time": "15:00", "venue": "AT&T Stadium (Dallas)"},
        },
        "round_of_16": {
            "R16_1": {"date": "04/07", "time": "14:00", "venue": "NRG Stadium (Houston)"},
            "R16_2": {"date": "04/07", "time": "18:00", "venue": "Lincoln Financial (Filadélfia)"},
            "R16_3": {"date": "05/07", "time": "17:00", "venue": "MetLife Stadium (Nova York/NJ)"},
            "R16_4": {"date": "05/07", "time": "21:00", "venue": "Estádio Azteca (Cidade do México)"},
            "R16_5": {"date": "06/07", "time": "16:00", "venue": "AT&T Stadium (Dallas)"},
            "R16_6": {"date": "06/07", "time": "21:00", "venue": "Lumen Field (Seattle)"},
            "R16_7": {"date": "07/07", "time": "13:00", "venue": "Mercedes-Benz (Atlanta)"},
            "R16_8": {"date": "07/07", "time": "17:00", "venue": "BC Place (Vancouver)"},
        },
        "quarter_finals": {
            "QF_1": {"date": "09/07", "time": "17:00", "venue": "Gillette Stadium (Boston)"},
            "QF_2": {"date": "10/07", "time": "16:00", "venue": "SoFi Stadium (Los Angeles)"},
            "QF_3": {"date": "11/07", "time": "18:00", "venue": "Hard Rock Stadium (Miami)"},
            "QF_4": {"date": "11/07", "time": "22:00", "venue": "Arrowhead (Kansas City)"},
        },
        "semi_finals": {
            "SF_1": {"date": "14/07", "time": "16:00", "venue": "AT&T Stadium (Dallas)"},
            "SF_2": {"date": "15/07", "time": "16:00", "venue": "Mercedes-Benz (Atlanta)"},
        },
        "third_place": {
            "3RD": {"date": "18/07", "time": "18:00", "venue": "Hard Rock Stadium (Miami)"},
        },
        "final": {
            "FINAL": {"date": "19/07", "time": "16:00", "venue": "MetLife Stadium (Nova York/NJ)"},
        },
    }
}

GROUP_MATCHES = {
    g: [
        {"id": f"G{g}_{i}", "home": m["home"], "away": m["away"]}
        for i, m in enumerate(MATCH_DATES["group"][g])
    ]
    for g in "ABCDEFGHIJKL"
}

KNOCKOUT_STAGES = {
    "round_of_32": {"name": "16-avos de Final", "matches": 16, "order": 0},
    "round_of_16": {"name": "Oitavas de Final", "matches": 8, "order": 1},
    "quarter_finals": {"name": "Quartas de Final", "matches": 4, "order": 2},
    "semi_finals": {"name": "Semifinais", "matches": 2, "order": 3},
    "third_place": {"name": "Disputa de 3º Lugar", "matches": 1, "order": 4},
    "final": {"name": "Final", "matches": 1, "order": 5}
}

BRACKET_MATCHUPS = {
    "round_of_32": [
        {"id": "R32_1", "home": "1A", "away": "3C/D/E", "next": "R16_1"},
        {"id": "R32_2", "home": "2A", "away": "2B", "next": "R16_1"},
        {"id": "R32_3", "home": "1B", "away": "3A/C/D", "next": "R16_2"},
        {"id": "R32_4", "home": "1C", "away": "3A/B/F", "next": "R16_2"},
        {"id": "R32_5", "home": "2C", "away": "2D", "next": "R16_3"},
        {"id": "R32_6", "home": "1D", "away": "3B/E/F", "next": "R16_3"},
        {"id": "R32_7", "home": "2E", "away": "2F", "next": "R16_4"},
        {"id": "R32_8", "home": "1E", "away": "3C/D/F", "next": "R16_4"},
        {"id": "R32_9", "home": "1F", "away": "3A/B/E", "next": "R16_5"},
        {"id": "R32_10", "home": "2G", "away": "2H", "next": "R16_5"},
        {"id": "R32_11", "home": "1G", "away": "3D/E/F", "next": "R16_6"},
        {"id": "R32_12", "home": "1H", "away": "3A/B/C", "next": "R16_6"},
        {"id": "R32_13", "home": "2I", "away": "2J", "next": "R16_7"},
        {"id": "R32_14", "home": "1I", "away": "3D/E/F", "next": "R16_7"},
        {"id": "R32_15", "home": "1J", "away": "3A/C/D", "next": "R16_8"},
        {"id": "R32_16", "home": "2K", "away": "2L", "next": "R16_8"},
    ],
    "round_of_16": [
        {"id": "R16_1", "home": "WR32_1", "away": "WR32_2", "next": "QF_1"},
        {"id": "R16_2", "home": "WR32_3", "away": "WR32_4", "next": "QF_1"},
        {"id": "R16_3", "home": "WR32_5", "away": "WR32_6", "next": "QF_2"},
        {"id": "R16_4", "home": "WR32_7", "away": "WR32_8", "next": "QF_2"},
        {"id": "R16_5", "home": "WR32_9", "away": "WR32_10", "next": "QF_3"},
        {"id": "R16_6", "home": "WR32_11", "away": "WR32_12", "next": "QF_3"},
        {"id": "R16_7", "home": "WR32_13", "away": "WR32_14", "next": "QF_4"},
        {"id": "R16_8", "home": "WR32_15", "away": "WR32_16", "next": "QF_4"},
    ],
    "quarter_finals": [
        {"id": "QF_1", "home": "WR16_1", "away": "WR16_2", "next": "SF_1"},
        {"id": "QF_2", "home": "WR16_3", "away": "WR16_4", "next": "SF_1"},
        {"id": "QF_3", "home": "WR16_5", "away": "WR16_6", "next": "SF_2"},
        {"id": "QF_4", "home": "WR16_7", "away": "WR16_8", "next": "SF_2"},
    ],
    "semi_finals": [
        {"id": "SF_1", "home": "WQF_1", "away": "WQF_2", "next": "FINAL"},
        {"id": "SF_2", "home": "WQF_3", "away": "WQF_4", "next": "FINAL"},
    ],
    "third_place": [
        {"id": "3RD", "home": "LSF_1", "away": "LSF_2", "next": None},
    ],
    "final": [
        {"id": "FINAL", "home": "WSF_1", "away": "WSF_2", "next": None},
    ]
}
