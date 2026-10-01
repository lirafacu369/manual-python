# Percorrendo strings
# Manual do Desenvolvedor Python - Capitulo 5

codigo_ingresso = "EVT2026"

for caractere in codigo_ingresso:
    print(caractere, end=" ")
print()

apenas_numeros = "".join(c for c in codigo_ingresso if c.isdigit())
print(f"Apenas números: {apenas_numeros}")
