# Listas de dicionários
# Manual do Desenvolvedor Python - Capitulo 9

visitantes = [
    {"nome": "Andy Angel", "idade": 25},
    {"nome": "Lu Brandão", "idade": 17},
    {"nome": "João P", "idade": 30},
]

for visitante in visitantes:
    print(f"{visitante['nome']}: {visitante['idade']} anos")

print(f"Total de visitantes: {len(visitantes)}")
