# Dicionários com listas
# Manual do Desenvolvedor Python - Capitulo 9

evento = {
    "nome": "Festa Andy Angel",
    "visitantes": ["Lu Brandão", "Gabi Moreira", "João P"],
}

evento["visitantes"].append("Adry Alves")

print(f"Evento: {evento['nome']}")
print(f"Visitantes: {evento['visitantes']}")
print(f"Total: {len(evento['visitantes'])}")
