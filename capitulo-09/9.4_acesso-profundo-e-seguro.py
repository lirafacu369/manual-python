# Acesso profundo e seguro
# Manual do Desenvolvedor Python - Capitulo 9

eventos = {
    "evt001": {
        "nome": "Festa Andy Angel",
        "local": {"endereco": "Rua das Flores, 123"},
    }
}

endereco = eventos["evt001"]["local"]["endereco"]
print(f"Endereço: {endereco}")

endereco_seguro = eventos.get("evt002", {}).get("local", {}).get("endereco", "não encontrado")
print(f"Endereço (evento inexistente): {endereco_seguro}")
