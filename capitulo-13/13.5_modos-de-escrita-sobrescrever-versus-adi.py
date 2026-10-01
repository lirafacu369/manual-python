# Modos de escrita: sobrescrever versus adicionar
# Manual do Desenvolvedor Python - Capitulo 13

with open("log_teste.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write("Primeira linha\n")

with open("log_teste.txt", "a", encoding="utf-8") as arquivo:
    arquivo.write("Segunda linha (append)\n")

with open("log_teste.txt", "r", encoding="utf-8") as arquivo:
    print(arquivo.read())
