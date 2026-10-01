# Busca por chave em coleções de dicionários
# Manual do Desenvolvedor Python - Capitulo 8

eventos = {
    "evt001": {"nome": "Festa Andy Angel", "capacidade": 200},
    "evt002": {"nome": "Show Lu Brandão", "capacidade": 500},
}

codigo_procurado = "evt002"
if codigo_procurado in eventos:
    print(f"Encontrado: {eventos[codigo_procurado]['nome']}")
else:
    print("Evento não encontrado.")
