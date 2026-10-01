# Dados aninhados em múltiplos níveis
# Manual do Desenvolvedor Python - Capitulo 9

evento = {
    "nome": "Festa Andy Angel",
    "local": {"endereco": "Rua das Flores, 123", "capacidade": 200},
    "organizador": {"nome": "Gabriella Santiago", "contato": "gabi@evento.com"},
}

print(f"Evento: {evento['nome']}")
print(f"Local: {evento['local']['endereco']}")
print(f"Organizador: {evento['organizador']['nome']}")
