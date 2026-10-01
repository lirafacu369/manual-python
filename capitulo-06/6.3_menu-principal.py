# Menu principal
# Manual do Desenvolvedor Python - Capitulo 6

opcoes_simuladas = ["1", "2", "0"]
indice = 0

while True:
    opcao = opcoes_simuladas[indice]
    indice += 1

    if opcao == "1":
        print("Cadastrar visitante")
    elif opcao == "2":
        print("Listar visitantes")
    elif opcao == "0":
        print("Encerrando o sistema...")
        break
    else:
        print("Opção inválida.")
