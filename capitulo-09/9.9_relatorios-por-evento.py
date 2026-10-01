# Relatórios por evento
# Manual do Desenvolvedor Python - Capitulo 9

eventos = [
    {"nome": "Festa Andy Angel", "visitantes_confirmados": 137, "capacidade": 200},
    {"nome": "Show Lu Brandão", "visitantes_confirmados": 480, "capacidade": 500},
]

print("=" * 40)
print("RELATÓRIO DE OCUPAÇÃO POR EVENTO")
print("=" * 40)

for evento in eventos:
    ocupacao = (evento["visitantes_confirmados"] / evento["capacidade"]) * 100
    print(f"{evento['nome']}: {ocupacao:.1f}% ocupado")
