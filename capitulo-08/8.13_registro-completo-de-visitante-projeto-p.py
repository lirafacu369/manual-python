# Registro completo de visitante (projeto prático do capítulo)
# Manual do Desenvolvedor Python - Capitulo 8

def criar_registro_visitante(nome, idade_texto, tem_ingresso):
    try:
        idade = int(idade_texto)
    except ValueError:
        return None, f"Idade inválida: '{idade_texto}'"

    if idade < 0 or idade > 120:
        return None, f"Idade fora da faixa plausível: {idade}"

    registro = {
        "nome": nome.strip().title(),
        "idade": idade,
        "tem_ingresso": tem_ingresso,
        "maior_de_idade": idade >= 18,
        "status": "pendente",
    }
    return registro, None


registro, erro = criar_registro_visitante("  andy angel  ", "25", True)
if erro:
    print(f"Erro: {erro}")
else:
    print(registro)

registro2, erro2 = criar_registro_visitante("lu brandão", "abc", True)
if erro2:
    print(f"Erro: {erro2}")
