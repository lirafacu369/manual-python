# Testando sem `input()` real
# Manual do Desenvolvedor Python - Capitulo 15

def iniciar_com_entradas_simuladas(self, entradas_simuladas):
    indice = [0]

    def proxima_entrada():
        valor = entradas_simuladas[indice[0]]
        indice[0] += 1
        return valor

    while True:
        opcao = proxima_entrada()
        if opcao == "1":
            nome = proxima_entrada()
            idade = proxima_entrada()
            continuar = self.processar(opcao, nome, idade)
        else:
            continuar = self.processar(opcao)
        if not continuar:
            break
