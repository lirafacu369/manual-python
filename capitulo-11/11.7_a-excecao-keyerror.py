# A exceção `KeyError`
# Manual do Desenvolvedor Python - Capitulo 11

visitante = {"nome": "Andy Angel", "idade": 25}

try:
    documento = visitante["documento"]
except KeyError as erro:
    print(f"Campo ausente: {erro}")
    documento = "não informado"

print(f"Documento: {documento}")
