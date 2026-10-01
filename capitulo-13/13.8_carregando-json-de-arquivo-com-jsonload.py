# Carregando JSON de arquivo com `json.load`
# Manual do Desenvolvedor Python - Capitulo 13

import json

with open("visitantes.json", "r", encoding="utf-8") as arquivo:
    visitantes_carregados = json.load(arquivo)

print(visitantes_carregados)
print(type(visitantes_carregados))
for v in visitantes_carregados:
    print(f"{v['nome']}, {v['idade']} anos")
