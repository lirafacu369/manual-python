# Separação de responsabilidades
# Manual do Desenvolvedor Python - Capitulo 10

def validar_idade(idade_texto):
    try:
        idade = int(idade_texto)
        if idade < 0 or idade > 120:
            return None, "Idade fora da faixa plausível"
        return idade, None
    except ValueError:
        return None, "Idade inválida"

def formatar_nome(nome):
    return nome.strip().title()

def criar_visitante(nome_bruto, idade_texto):
    nome = formatar_nome(nome_bruto)
    idade, erro = validar_idade(idade_texto)
    if erro:
        return None, erro
    return {"nome": nome, "idade": idade}, None


registro, erro = criar_visitante("  andy angel  ", "25")
print(registro)
