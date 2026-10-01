# Conversão de tipos
# Manual do Desenvolvedor Python - Capitulo 2

idade_texto = "29"
idade_numero = int(idade_texto)

print(type(idade_texto), type(idade_numero))
print(idade_numero + 1)  # funciona, porque agora é número

# tentativa de conversão inválida:
try:
    numero_invalido = int("vinte e nove")
except ValueError as erro:
    print(f"Erro ao converter: {erro}")
