"""Builds programmatic_flashcards.py - part 1"""
import os

path = r'D:\Prevcom\prevcom_app\programmatic_flashcards.py'

def write(s):
    with open(path, 'a', encoding='utf-8') as f:
        f.write(s + '\n')

if os.path.exists(path):
    os.remove(path)

header = '''"""Geracao programatica em massa de flashcards para PREVCOM 2026.
Produz ~4300 cards adicionais, distribuidos entre 5 disciplinas.
"""
from itertools import product


def gerar_flashcards_programaticamente():
    """Gera milhares de flashcards usando combinacoes, templates e iteracao."""
    cards = {
        "Lingua Portuguesa": [],
        "Etica e Integridade": [],
        "Raciocinio Logico e Analitico": [],
        "Previdencia Complementar no Brasil": [],
        "Conhecimentos Especificos em Tecnologia": [],
    }

    LP = cards["Lingua Portuguesa"]
    ET = cards["Etica e Integridade"]
    RL = cards["Raciocinio Logico e Analitico"]
    PR = cards["Previdencia Complementar no Brasil"]
    TI = cards["Conhecimentos Especificos em Tecnologia"]

    # ================================================================
    # 1. LINGUA PORTUGUESA
    # ================================================================

    # -- Verb conjugation patterns (regular endings) --
    tempos_indicativo = [
        ("presente", "o/as/a/amos/ais/am", "o/es/e/emos/eis/em", "o/es/e/imos/is/em"),
        ("preterito perfeito", "ei/aste/ou/amos/astes/aram", "i/este/eu/emos/estes/eram", "i/iste/iu/imos/istes/iram"),
        ("preterito imperfeito", "ava/avas/ava/avamos/aveis/avam", "ia/ias/ia/iamos/ieis/iam", "ia/ias/ia/iamos/ieis/iam"),
        ("futuro do presente", "arei/aras/ara/aremos/areis/arao", "erei/eras/era/eremos/ereis/erao", "irei/iras/ira/iremos/ireis/irao"),
        ("futuro do preterito", "aria/arias/aria/ariamos/arieis/ariam", "eria/erias/eria/eriamos/erieis/eriam", "iria/irias/iria/iriamos/irieis/iriam"),
    ]
    for tempo, ar, er, ir in tempos_indicativo:
        LP.append((f"Conjugacao verbos -ar no {tempo} do indicativo", f"radical + {ar}. Ex: falar -> fal{ar.split('/')[0]}..."))
        LP.append((f"Conjugacao verbos -er no {tempo} do indicativo", f"radical + {er}. Ex: comer -> com{er.split('/')[0]}..."))
        LP.append((f"Conjugacao verbos -ir no {tempo} do indicativo", f"radical + {ir}. Ex: partir -> part{ir.split('/')[0]}..."))

    tempos_subjuntivo = [
        ("presente", "e/es/e/emos/eis/em", "a/as/a/amos/ais/am", "a/as/a/amos/ais/am"),
        ("preterito imperfeito", "asse/asses/asse/assemos/asseis/assem", "esse/esses/esse/essemos/esseis/essem", "isse/isses/isse/issemos/isseis/issem"),
        ("futuro", "ar/ares/ar/armos/ardes/arem", "er/eres/er/ermos/erdes/erem", "ir/ires/ir/irmos/irdes/irem"),
    ]
    for tempo, ar, er, ir in tempos_subjuntivo:
        LP.append((f"Conjugacao verbos -ar no {tempo} do subjuntivo", f"radical + {ar}"))
        LP.append((f"Conjugacao verbos -er no {tempo} do subjuntivo", f"radical + {er}"))
        LP.append((f"Conjugacao verbos -ir no {tempo} do subjuntivo", f"radical + {ir}"))

'''
write(header)
print("Header written")
