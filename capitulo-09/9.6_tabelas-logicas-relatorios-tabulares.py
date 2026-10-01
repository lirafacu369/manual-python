# Tabelas lógicas (relatórios tabulares)
# Manual do Desenvolvedor Python - Capitulo 9

visitantes = [
    {"nome": "Andy Angel", "idade": 25, "vip": True, "pago": True},
    {"nome": "Lu Brandão", "idade": 17, "vip": False, "pago": False},
    {"nome": "João P", "idade": 30, "vip": True, "pago": False},
]

print(f"{'Nome':<15}{'Idade':<8}{'VIP':<8}{'Pago':<8}")
for v in visitantes:
    print(f"{v['nome']:<15}{v['idade']:<8}{str(v['vip']):<8}{str(v['pago']):<8}")
