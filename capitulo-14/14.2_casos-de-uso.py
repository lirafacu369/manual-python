# Casos de uso
# Manual do Desenvolvedor Python - Capitulo 14

def caso_de_uso_cadastro(nome, idade_texto):
    """Caso de uso: operador cadastra um novo visitante na portaria."""
    try:
        idade = int(idade_texto)
    except ValueError:
        return None, "Idade invalida"
    if idade < 0 or idade > 120:
        return None, "Idade fora da faixa plausivel"
    return {"nome": nome.strip().title(), "idade": idade}, None


visitante, erro = caso_de_uso_cadastro("Lu Brandão", "22")
print(visitante, erro)
