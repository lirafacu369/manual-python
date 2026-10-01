# Modos de leitura
# Manual do Desenvolvedor Python - Capitulo 13

with open("visitantes_teste.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write("Andy Angel\n")
    arquivo.write("Lu Brandão\n")
    arquivo.write("João P\n")

with open("visitantes_teste.txt", "r", encoding="utf-8") as arquivo:
    conteudo_completo = arquivo.read()
print("Leitura completa:")
print(conteudo_completo)

with open("visitantes_teste.txt", "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
        print(f"Visitante: {linha.strip()}")
