# Validação defensiva
# Manual do Desenvolvedor Python - Capitulo 11

def cadastrar_visitante(dados):
    campos_obrigatorios = ["nome", "idade"]

    for campo in campos_obrigatorios:
        if campo not in dados:
            return None, f"Campo obrigatório ausente: {campo}"
        if not dados[campo]:
            return None, f"Campo obrigatório vazio: {campo}"

    return dados, None


registro, erro = cadastrar_visitante({"nome": "Andy Angel", "idade": 25})
print(registro, erro)

registro2, erro2 = cadastrar_visitante({"nome": ""})
print(registro2, erro2)
