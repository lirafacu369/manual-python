# Codificação UTF-8
# Manual do Desenvolvedor Python - Capitulo 13

with open("teste_acentos.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write("São Paulo, Ana, João, coração")

with open("teste_acentos.txt", "r", encoding="utf-8") as arquivo:
    conteudo = arquivo.read()

print(conteudo)
