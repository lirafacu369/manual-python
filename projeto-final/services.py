"""Camada de serviço: regras de negócio e validação."""

from models import Visitante


class ServicoValidacao:
    def validar_idade(self, idade_texto):
        try:
            idade = int(idade_texto)
        except ValueError:
            return None, "Idade inválida"
        if idade < 0 or idade > 120:
            return None, "Idade fora da faixa plausível"
        return idade, None

    def validar_nome(self, nome):
        nome_tratado = nome.strip()
        if not nome_tratado:
            return None, "Nome é obrigatório"
        return nome_tratado.title(), None


class ServicoAcesso:
    def __init__(self, idade_minima=18):
        self.idade_minima = idade_minima

    def autorizar(self, idade, tem_ingresso, perfil="visitante"):
        if perfil == "bloqueado":
            return False, "Perfil bloqueado"
        if perfil in ("organizador", "seguranca"):
            return True, None
        if not tem_ingresso:
            return False, "Sem ingresso"
        if idade < self.idade_minima:
            return False, "Menor de idade sem acompanhamento verificado"
        return True, None


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
