# Mensagens de erro claras
# Manual do Desenvolvedor Python - Capitulo 4

idade_texto = "vinte e cinco"

try:
    idade = int(idade_texto)
except ValueError:
    # mensagem RUIM: "Erro."
    # mensagem BOA: específica, com o valor recebido e o formato esperado
    print(f"Erro: '{idade_texto}' não é um número válido. Digite apenas dígitos, como 25.")
