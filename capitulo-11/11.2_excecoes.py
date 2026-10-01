# Exceções
# Manual do Desenvolvedor Python - Capitulo 11

try:
    resultado = 10 / 0
except ZeroDivisionError as erro:
    print(f"Erro de execução (exceção): {erro}")

print("Programa continua rodando normalmente.")
