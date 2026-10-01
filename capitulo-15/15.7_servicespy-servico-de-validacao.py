# `services.py` — serviço de validação
# Manual do Desenvolvedor Python - Capitulo 15

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
