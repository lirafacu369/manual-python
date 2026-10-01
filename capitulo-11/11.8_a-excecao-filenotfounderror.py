# A exceção `FileNotFoundError`
# Manual do Desenvolvedor Python - Capitulo 11

try:
    with open("arquivo_que_nao_existe.txt", "r") as arquivo:
        conteudo = arquivo.read()
except FileNotFoundError as erro:
    print(f"Arquivo não encontrado: {erro.filename}")
