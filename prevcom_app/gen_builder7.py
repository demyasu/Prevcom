"""Builds programmatic_flashcards.py - part 7: close function"""
import os

path = r'D:\Prevcom\prevcom_app\programmatic_flashcards.py'

def write(s):
    with open(path, 'a', encoding='utf-8') as f:
        f.write(s + '\n')

write('''
    print(f"\\n=== RESUMO PROGRAMATICO ===")
    print(f"  Lingua Portuguesa: {len(LP)} cards")
    print(f"  Etica e Integridade: {len(ET)} cards")
    print(f"  Raciocinio Logico: {len(RL)} cards")
    print(f"  Previdencia Complementar: {len(PR)} cards")
    print(f"  Conhecimentos Tecnologia: {len(TI)} cards")
    print(f"  TOTAL programatico: {len(LP)+len(ET)+len(RL)+len(PR)+len(TI)} cards")

    return {
        "Lingua Portuguesa": LP,
        "Etica e Integridade": ET,
        "Raciocinio Logico e Analitico": RL,
        "Previdencia Complementar no Brasil": PR,
        "Conhecimentos Especificos em Tecnologia": TI,
    }

''')

print("Part 7 written (function close)")
