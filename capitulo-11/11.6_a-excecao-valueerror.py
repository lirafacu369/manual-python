# A exceção `ValueError`
# Manual do Desenvolvedor Python - Capitulo 11

def validar_idade(idade_texto):
    try:
        idade = int(idade_texto)
    except ValueError:
        raise ValueError(f"'{idade_texto}' não é um número inteiro válido.")
    return idade


try:
    validar_idade("abc")
except ValueError as erro:
    print(f"Capturado: {erro}")
