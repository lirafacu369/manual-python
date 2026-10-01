# Visitantes por local (agrupamento)
# Manual do Desenvolvedor Python - Capitulo 9

visitantes = [
    {"nome": "Andy Angel", "local": "Salão Principal"},
    {"nome": "Lu Brandão", "local": "Área Externa"},
    {"nome": "João P", "local": "Salão Principal"},
]

contagem_por_local = {}
for v in visitantes:
    local = v["local"]
    contagem_por_local[local] = contagem_por_local.get(local, 0) + 1

for local, total in contagem_por_local.items():
    print(f"{local}: {total} visitante(s)")
