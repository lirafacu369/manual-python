# `enumerate()`
# Manual do Desenvolvedor Python - Capitulo 5

visitantes = ["Andy Angel", "Lu Brandão", "João P"]

for indice, nome in enumerate(visitantes, start=1):
    print(f"{indice}. {nome}")
