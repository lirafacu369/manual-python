# Módulos
# Manual do Desenvolvedor Python - Capitulo 10

"""Módulo de validações do sistema de portaria."""

def validar_idade(idade_texto):
    try:
        idade = int(idade_texto)
        if idade < 0 or idade > 120:
            return None, "Idade fora da faixa plausível"
        return idade, None
    except ValueError:
        return None, "Idade inválida"


def formatar_nome(nome):
    return nome.strip().title()
