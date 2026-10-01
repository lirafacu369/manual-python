# Recuperação do sistema (projeto prático do capítulo)
# Manual do Desenvolvedor Python - Capitulo 11

class ServicoVisitante:
    def __init__(self):
        self.visitantes = []

    def cadastrar(self, nome, idade_texto):
        try:
            idade = int(idade_texto)
            if idade < 0 or idade > 120:
                raise ValueError("Idade fora da faixa plausível")
        except ValueError as erro:
            return None, f"Falha ao cadastrar '{nome}': {erro}"

        visitante = {"nome": nome.strip().title(), "idade": idade}
        self.visitantes.append(visitante)
        return visitante, None

    def cadastrar_lote(self, lista_dados):
        sucesso = []
        falhas = []
        for nome, idade_texto in lista_dados:
            visitante, erro = self.cadastrar(nome, idade_texto)
            if erro:
                falhas.append(erro)
            else:
                sucesso.append(visitante)
        return sucesso, falhas


servico = ServicoVisitante()
dados_lote = [
    ("Andy Angel", "25"),
    ("Lu Brandão", "abc"),
    ("João P", "200"),
    ("Gabi Moreira", "30"),
]

sucesso, falhas = servico.cadastrar_lote(dados_lote)
print(f"Cadastrados com sucesso: {sucesso}")
print(f"Falhas: {falhas}")
