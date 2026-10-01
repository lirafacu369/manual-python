# Acesso seguro
# Manual do Desenvolvedor Python - Capitulo 8

visitante = {"nome": "João P", "idade": 28}

print(visitante["nome"])

try:
    print(visitante["documento"])
except KeyError as erro:
    print(f"Erro: chave {erro} não existe.")
