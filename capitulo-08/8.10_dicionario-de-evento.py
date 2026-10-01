# Dicionário de evento
# Manual do Desenvolvedor Python - Capitulo 8

evento = {
    "nome": "Festa Andy Angel",
    "data": "2026-12-31",
    "capacidade_maxima": 200,
    "visitantes_confirmados": 137,
    "status": "inscricoes_abertas",
}

vagas_restantes = evento["capacidade_maxima"] - evento["visitantes_confirmados"]
print(f"Evento: {evento['nome']}")
print(f"Vagas restantes: {vagas_restantes}")
