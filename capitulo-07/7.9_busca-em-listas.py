# Busca em listas
# Manual do Desenvolvedor Python - Capitulo 7

visitantes = ["Andy Angel", "Gabriella Santiago", "Lu Brandão"]

print(f"'Lu Brandão' está na lista? {'Lu Brandão' in visitantes}")
print(f"'João P' está na lista? {'João P' in visitantes}")

indice = visitantes.index("Gabriella Santiago")
print(f"Índice de Gabriella Santiago: {indice}")
