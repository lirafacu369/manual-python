# Ponto flutuante
# Manual do Desenvolvedor Python - Capitulo 2

preco_ingresso = 89.90
desconto_percentual = 15

preco_com_desconto = preco_ingresso * (1 - desconto_percentual / 100)

print(f"Preço original: R$ {preco_ingresso:.2f}")
print(f"Preço com desconto: R$ {preco_com_desconto:.2f}")

# a armadilha clássica de ponto flutuante:
print(0.1 + 0.2 == 0.3)  # imprime False, não True!
