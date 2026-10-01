# `continue` em laços indeterminados
# Manual do Desenvolvedor Python - Capitulo 6

idades_simuladas = [15, -3, 22, 200, 30]
indice = 0
processadas = []

while indice < len(idades_simuladas):
    idade = idades_simuladas[indice]
    indice += 1

    if idade < 0 or idade > 120:
        continue

    processadas.append(idade)

print(f"Idades processadas: {processadas}")
