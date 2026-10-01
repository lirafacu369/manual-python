# `break` em laços indeterminados
# Manual do Desenvolvedor Python - Capitulo 6

codigos_simulados = ["A1", "B2", "ENCERRAR", "C3"]
indice = 0

while indice < len(codigos_simulados):
    codigo = codigos_simulados[indice]
    indice += 1

    if codigo == "ENCERRAR":
        print("Comando de encerramento recebido.")
        break

    print(f"Processando código: {codigo}")

print("Fim do processamento.")
