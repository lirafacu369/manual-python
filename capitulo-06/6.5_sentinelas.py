# Sentinelas
# Manual do Desenvolvedor Python - Capitulo 6

entradas_simuladas = ["Andy Angel", "Lu Brandão", "sair"]
visitantes = []
indice = 0

while True:
    entrada = entradas_simuladas[indice]
    indice += 1

    if entrada.lower() == "sair":
        break

    visitantes.append(entrada)

print(f"Visitantes cadastrados: {visitantes}")
