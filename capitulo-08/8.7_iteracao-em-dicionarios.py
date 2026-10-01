# Iteração em dicionários
# Manual do Desenvolvedor Python - Capitulo 8

visitante = {"nome": "João P", "idade": 28, "vip": False}

for chave in visitante:
    print(f"Chave: {chave}")

for chave, valor in visitante.items():
    print(f"{chave}: {valor}")
