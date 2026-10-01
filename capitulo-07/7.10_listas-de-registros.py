# Listas de registros
# Manual do Desenvolvedor Python - Capitulo 7

visitantes = [
    {"nome": "Andy Angel", "idade": 25, "vip": True},
    {"nome": "Lu Brandão", "idade": 17, "vip": False},
]

for visitante in visitantes:
    print(f"{visitante['nome']}, {visitante['idade']} anos, VIP: {visitante['vip']}")

visitantes.append({"nome": "João P", "idade": 30, "vip": False})
print(f"Total de registros: {len(visitantes)}")
