# Prevenção de loop infinito
# Manual do Desenvolvedor Python - Capitulo 6

contador = 0
limite_seguranca = 1000
condicao_externa_simulada = [False, False, False, True]
indice = 0

while indice < len(condicao_externa_simulada):
    contador += 1

    if contador > limite_seguranca:
        print("Limite de segurança atingido — laço interrompido para evitar loop infinito.")
        break

    if condicao_externa_simulada[indice]:
        print(f"Condição satisfeita após {contador} iterações.")
        break

    indice += 1
