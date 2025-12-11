
import json

filename = "c:/Users/christian.vasquez/Documents/antigravity/storytelling/storytelling_executive.ipynb"

with open(filename, 'r', encoding='utf-8') as f:
    lines = f.readlines()

search_terms = [
    "Crisis de los 90s",
    "Geografía como destino",
    "LA RESOLUCIÓN",
    "EL CONTEXTO",
    "EL ANÁLISIS",
    "EL QUIEBRE",
    "Mensaje Central",
    "Framework ABT"
]

for i, line in enumerate(lines):
    for term in search_terms:
        if term.lower() in line.lower():
            print(f"Line {i+1}: {term} -> {line.strip()[:100]}")
