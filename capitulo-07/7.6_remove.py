# `remove()`
# Manual do Desenvolvedor Python - Capitulo 7

visitantes = ["Andy Angel", "Gabriella Santiago", "Lu Brandão"]

visitantes.remove("Gabriella Santiago")
print(visitantes)

try:
    visitantes.remove("Fulano Inexistente")
except ValueError as erro:
    print(f"Erro: {erro}")
