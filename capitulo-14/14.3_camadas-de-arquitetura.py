# Camadas de arquitetura
# Manual do Desenvolvedor Python - Capitulo 14

def camada_apresentacao(nome_bruto, idade_texto):
    return camada_servico(nome_bruto, idade_texto)

def camada_servico(nome_bruto, idade_texto):
    nome = nome_bruto.strip().title()
    try:
        idade = int(idade_texto)
    except ValueError:
        return None, "Idade invalida"
    return camada_dados(nome, idade)

def camada_dados(nome, idade):
    registro = {"nome": nome, "idade": idade}
    return registro, None


resultado, erro = camada_apresentacao("gabi moreira", "24")
print(resultado, erro)
