# Fluxo de cadastro (visão de ponta a ponta)
# Manual do Desenvolvedor Python - Capitulo 14

def fluxo_cadastro(nome_bruto, idade_texto, repositorio_simulado):
    nome = nome_bruto.strip().title()
    try:
        idade = int(idade_texto)
    except ValueError:
        return None, "Idade invalida"
    if idade < 0 or idade > 120:
        return None, "Idade fora da faixa plausivel"
    visitante = {"nome": nome, "idade": idade}
    repositorio_simulado.append(visitante)
    return visitante, None


dados = []
resultado, erro = fluxo_cadastro("gabi moreira", "24", dados)
print(resultado, erro)
print(f"Repositorio simulado: {dados}")
