# Validação de entrada com estruturas condicionais
# Manual do Desenvolvedor Python - Capitulo 4

def validar_idade(idade_texto):
    try:
        idade = int(idade_texto)
    except ValueError:
        return None, f"'{idade_texto}' não é um número válido."

    if idade < 0 or idade > 120:
        return None, f"Idade {idade} está fora de uma faixa plausível."

    return idade, None


for entrada in ["25", "abc", "-5", "200"]:
    idade, erro = validar_idade(entrada)
    if erro:
        print(f"Entrada '{entrada}': {erro}")
    else:
        print(f"Entrada '{entrada}': idade válida = {idade}")
