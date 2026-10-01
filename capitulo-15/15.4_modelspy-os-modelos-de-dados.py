# `models.py` — os modelos de dados
# Manual do Desenvolvedor Python - Capitulo 15

"""Modelos de dados do sistema de portaria."""


class Visitante:
    def __init__(self, nome, idade, vip=False):
        self.nome = nome.strip().title()
        self.idade = idade
        self.vip = vip

    def maior_de_idade(self):
        return self.idade >= 18

    def to_dict(self):
        return {"nome": self.nome, "idade": self.idade, "vip": self.vip}

    @staticmethod
    def from_dict(dados):
        return Visitante(dados["nome"], dados["idade"], dados.get("vip", False))


class Evento:
    def __init__(self, nome, capacidade_maxima, visitantes_confirmados=0):
        self.nome = nome.strip()
        self.capacidade_maxima = capacidade_maxima
        self.visitantes_confirmados = visitantes_confirmados

    def vagas_restantes(self):
        return self.capacidade_maxima - self.visitantes_confirmados

    def to_dict(self):
        return {
            "nome": self.nome,
            "capacidade_maxima": self.capacidade_maxima,
            "visitantes_confirmados": self.visitantes_confirmados,
        }

    @staticmethod
    def from_dict(dados):
        return Evento(dados["nome"], dados["capacidade_maxima"], dados.get("visitantes_confirmados", 0))
