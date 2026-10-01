# Submenus
# Manual do Desenvolvedor Python - Capitulo 6

opcoes_principal = ["2"]
opcoes_submenu = ["1", "0"]

for opcao in opcoes_principal:
    if opcao == "2":
        print("Entrando no submenu de relatórios...")
        indice_sub = 0
        while indice_sub < len(opcoes_submenu):
            sub_opcao = opcoes_submenu[indice_sub]
            indice_sub += 1
            if sub_opcao == "1":
                print("  Relatório de vendas")
            elif sub_opcao == "0":
                print("  Voltando ao menu principal...")
                break
