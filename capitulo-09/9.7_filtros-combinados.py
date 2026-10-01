# Filtros combinados
# Manual do Desenvolvedor Python - Capitulo 9

visitantes = [
    {"nome": "Andy Angel", "idade": 25, "vip": True},
    {"nome": "Lu Brandão", "idade": 17, "vip": False},
    {"nome": "João P", "idade": 30, "vip": True},
    {"nome": "Gabi Moreira", "idade": 16, "vip": True},
]

vips_maiores_de_idade = [v["nome"] for v in visitantes if v["vip"] and v["idade"] >= 18]
print(f"VIPs maiores de idade: {vips_maiores_de_idade}")
