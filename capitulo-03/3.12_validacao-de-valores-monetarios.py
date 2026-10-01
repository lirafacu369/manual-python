# Validação de valores monetários
# Manual do Desenvolvedor Python - Capitulo 3

valor_texto = input("Digite o valor do ingresso (ex: 89.90): ")

try:
    valor = float(valor_texto)
    if valor < 0:
        print("Valor não pode ser negativo.")
    elif valor == 0:
        print("Valor zero registrado — confirme se é uma cortesia.")
    else:
        valor_arredondado = round(valor, 2)
        print(f"Valor válido registrado: R$ {valor_arredondado:.2f}")
except ValueError:
    print(f"'{valor_texto}' não é um valor monetário válido.")
