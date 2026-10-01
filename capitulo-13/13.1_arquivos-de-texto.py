# Arquivos de texto
# Manual do Desenvolvedor Python - Capitulo 13

caminho = "teste.txt"
with open(caminho, "w", encoding="utf-8") as arquivo:
    arquivo.write("Sistema de Portaria\n")
    arquivo.write("Linha de teste")

print("Arquivo criado com sucesso.")
