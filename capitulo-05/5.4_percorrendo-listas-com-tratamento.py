# Percorrendo listas com tratamento
# Manual do Desenvolvedor Python - Capitulo 5

visitantes = ["Adry Alves", "Gabi Moreira", "João P"]

for visitante in visitantes:
    nome_tratado = visitante.strip().title()
    print(f"Visitante confirmado: {nome_tratado}")
