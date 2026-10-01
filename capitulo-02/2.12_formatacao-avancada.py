# Formatação avançada
# Manual do Desenvolvedor Python - Capitulo 2

nome = "João P"
idade = 31

# forma 1 (f-string — a que usaremos no livro):
print(f"{nome} tem {idade} anos.")

# forma 2 (.format() — comum em código mais antigo):
print("{} tem {} anos.".format(nome, idade))

# forma 3 (% — a mais antiga, raramente usada em código novo):
print("%s tem %d anos." % (nome, idade))
