# O bloco `try`
# Manual do Desenvolvedor Python - Capitulo 11

idade_texto = "vinte e cinco"

try:
    idade = int(idade_texto)
    print(f"Idade: {idade}")
except ValueError:
    print("Não foi possível converter para número.")

print("Fluxo continua após o try/except.")
