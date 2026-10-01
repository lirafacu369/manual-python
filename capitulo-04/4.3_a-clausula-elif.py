# A cláusula `elif`
# Manual do Desenvolvedor Python - Capitulo 4

idade = 10

if idade < 12:
    categoria = "criança"
elif idade < 18:
    categoria = "adolescente"
elif idade < 60:
    categoria = "adulto"
else:
    categoria = "idoso"

print(f"Categoria: {categoria}")
