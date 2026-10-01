# Acumuladores
# Manual do Desenvolvedor Python - Capitulo 5

precos_ingressos = [89.90, 120.00, 89.90, 150.00, 89.90]

total_arrecadado = 0
for preco in precos_ingressos:
    total_arrecadado += preco

print(f"Total arrecadado: R$ {total_arrecadado:.2f}")
