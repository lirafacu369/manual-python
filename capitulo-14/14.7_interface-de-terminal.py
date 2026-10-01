# Interface de terminal
# Manual do Desenvolvedor Python - Capitulo 14

def exibir_menu():
    print("=" * 30)
    print("1. Cadastrar visitante")
    print("2. Listar visitantes")
    print("0. Sair")
    print("=" * 30)

def processar_opcao(opcao, visitantes):
    if opcao == "2":
        for v in visitantes:
            print(v)
        return True
    elif opcao == "0":
        return False
    else:
        print("Opcao invalida ou nao implementada neste teste.")
        return True


exibir_menu()
continuar = processar_opcao("2", [{"nome": "João P", "idade": 24}])
print(f"Continuar: {continuar}")
