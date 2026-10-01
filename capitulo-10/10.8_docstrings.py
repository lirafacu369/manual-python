# Docstrings
# Manual do Desenvolvedor Python - Capitulo 10

def calcular_idade_categoria(idade):
    """
    Classifica uma idade em categoria etária.

    Args:
        idade (int): idade da pessoa em anos.

    Returns:
        str: categoria correspondente.
    """
    if idade < 12:
        return "crianca"
    elif idade < 18:
        return "adolescente"
    return "adulto"

print(calcular_idade_categoria(10))
print(calcular_idade_categoria.__doc__)
