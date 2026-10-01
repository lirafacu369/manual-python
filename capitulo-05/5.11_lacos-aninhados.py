# Laços aninhados
# Manual do Desenvolvedor Python - Capitulo 5

eventos = {
    "Show de Abertura": ["Andy Angel", "João P"],
    "Palestra Principal": ["Lu Brandão", "Gabi Moreira"],
}

for evento, participantes in eventos.items():
    print(f"Evento: {evento}")
    for participante in participantes:
        print(f"  - {participante}")
