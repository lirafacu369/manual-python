# Validação de idade (projeto prático)
# Manual do Desenvolvedor Python - Capitulo 3

idade_texto = input("Digite a idade do visitante: ")

try:
    idade = int(idade_texto)
    if idade < 0 or idade > 120:
        print("Idade fora de uma faixa plausível — verifique o valor digitado.")
    else:
        maior_de_idade = idade >= 18
        print(f"Idade válida: {idade}. Maior de idade: {maior_de_idade}")
except ValueError:
    print(f"'{idade_texto}' não é um número válido para idade.")
