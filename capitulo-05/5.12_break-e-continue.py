# `break` e `continue`
# Manual do Desenvolvedor Python - Capitulo 5

idades = [15, 22, -5, 30, 200, 45]

for idade in idades:
    if idade < 0 or idade > 120:
        continue
    if idade >= 100:
        break
    print(f"Idade válida processada: {idade}")
