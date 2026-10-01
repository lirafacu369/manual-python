# `services.py` — o serviço coordenador `ServicoPortaria`
# Manual do Desenvolvedor Python - Capitulo 15

class ServicoPortaria:
    def __init__(self, repositorio):
        self.repositorio = repositorio
        self.validacao = ServicoValidacao()
        self.acesso = ServicoAcesso()

    def cadastrar_visitante(self, nome_bruto, idade_texto):
        nome, erro_nome = self.validacao.validar_nome(nome_bruto)
        if erro_nome:
            return None, erro_nome

        idade, erro_idade = self.validacao.validar_idade(idade_texto)
        if erro_idade:
            return None, erro_idade

        visitante = Visitante(nome, idade)
        dados = self.repositorio.carregar()
        dados.append(visitante.to_dict())
        self.repositorio.salvar(dados)
        return visitante, None

    def listar_visitantes(self):
        return self.repositorio.carregar()

    def buscar_por_nome(self, nome):
        return [v for v in self.repositorio.carregar() if v["nome"].lower() == nome.lower()]

    def gerar_relatorio(self):
        visitantes = self.repositorio.carregar()
        total = len(visitantes)
        maiores = len([v for v in visitantes if v["idade"] >= 18])
        return f"Total de visitantes: {total}\nMaiores de idade: {maiores}"
