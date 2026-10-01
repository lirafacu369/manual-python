# Refatoração de menus
# Manual do Desenvolvedor Python - Capitulo 6

def processar_opcao_v1(opcao):
    resultado = None
    if opcao == "1":
        resultado = "Cadastrar visitante"
    else:
        if opcao == "2":
            resultado = "Listar visitantes"
        else:
            if opcao == "0":
                resultado = "Sair"
            else:
                resultado = "Opção inválida"
    return resultado


def processar_opcao_v2(opcao):
    acoes = {
        "1": "Cadastrar visitante",
        "2": "Listar visitantes",
        "0": "Sair",
    }
    return acoes.get(opcao, "Opção inválida")


for opcao in ["1", "2", "0", "9"]:
    r1 = processar_opcao_v1(opcao)
    r2 = processar_opcao_v2(opcao)
    print(f"opcao={opcao}: v1={r1} | v2={r2} | iguais={r1 == r2}")
