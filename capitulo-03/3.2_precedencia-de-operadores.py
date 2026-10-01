# Precedência de operadores
# Manual do Desenvolvedor Python - Capitulo 3

preco_ingresso = 100
desconto = 10
taxa_servico = 5

# forma ERRADA (por precedência): calcula taxa sobre o preço cheio, sem aplicar o desconto antes
total_errado = preco_ingresso - desconto + taxa_servico / 100 * preco_ingresso

# forma CORRETA: parênteses deixam explícita a ordem pretendida
total_correto = (preco_ingresso - desconto) + (taxa_servico / 100) * preco_ingresso

print(f"Total (sem parênteses de apoio): {total_errado}")
print(f"Total (com parênteses explícitos): {total_correto}")
