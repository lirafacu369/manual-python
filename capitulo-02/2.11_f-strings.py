# f-strings
# Manual do Desenvolvedor Python - Capitulo 2

nome = "Lu Brandão"
idade = 29
preco_ingresso = 89.9

# expressão direta dentro da f-string:
print(f"{nome} tem {idade} anos e terá {65 - idade} anos em 2091.")

# formatação numérica:
print(f"Ingresso: R$ {preco_ingresso:.2f}")

# alinhamento (útil para relatórios em colunas, no Capítulo 9):
print(f"{nome:<20}{idade:>5}")
