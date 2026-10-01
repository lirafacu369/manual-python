# `menu.py` — a interface de terminal
# Manual do Desenvolvedor Python - Capitulo 15

"""Camada de apresentação: interface de terminal."""


class Menu:
    def __init__(self, servico):
        self.servico = servico

    def exibir(self):
        print("=" * 40)
        print("SISTEMA DE PORTARIA E GESTÃO DE EVENTOS")
        print("=" * 40)
        print("1. Cadastrar visitante")
        print("2. Listar visitantes")
        print("3. Gerar relatório")
        print("0. Sair")
        print("=" * 40)

    def processar(self, opcao, entrada_nome=None, entrada_idade=None):
        if opcao == "1":
            visitante, erro = self.servico.cadastrar_visitante(entrada_nome, entrada_idade)
            if erro:
                print(f"Erro ao cadastrar: {erro}")
            else:
                print(f"Visitante '{visitante.nome}' cadastrado com sucesso.")
            return True
        elif opcao == "2":
            visitantes = self.servico.listar_visitantes()
            for i, v in enumerate(visitantes, start=1):
                print(f"{i}. {v['nome']}, {v['idade']} anos")
            return True
        elif opcao == "3":
            print(self.servico.gerar_relatorio())
            return True
        elif opcao == "0":
            print("Encerrando o sistema...")
            return False
        else:
            print("Opção inválida.")
            return True

    def iniciar(self):
        while True:
            self.exibir()
            opcao = input("Escolha uma opção: ")
            if opcao == "1":
                nome = input("Nome do visitante: ")
                idade = input("Idade: ")
                continuar = self.processar(opcao, nome, idade)
            else:
                continuar = self.processar(opcao)
            if not continuar:
                break
