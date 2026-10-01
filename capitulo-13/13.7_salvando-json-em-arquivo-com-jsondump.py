# Salvando JSON em arquivo com `json.dump`
# Manual do Desenvolvedor Python - Capitulo 13

import json

visitantes = [
    {"nome": "Andy Angel", "idade": 25},
    {"nome": "Lu Brandão", "idade": 17},
]

with open("visitantes.json", "w", encoding="utf-8") as arquivo:
    json.dump(visitantes, arquivo, ensure_ascii=False, indent=2)

print("Arquivo JSON criado.")
with open("visitantes.json", "r", encoding="utf-8") as arquivo:
    print(arquivo.read())
