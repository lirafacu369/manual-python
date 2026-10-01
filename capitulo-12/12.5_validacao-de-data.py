# Validação de data
# Manual do Desenvolvedor Python - Capitulo 12

from datetime import datetime

def validar_data_nascimento(data_texto):
    try:
        data = datetime.strptime(data_texto, "%d/%m/%Y")
    except ValueError:
        return None, "Formato de data inválido. Use DD/MM/AAAA."

    hoje = datetime.now()
    if data > hoje:
        return None, "Data de nascimento não pode ser no futuro."

    idade_anos = (hoje - data).days // 365
    if idade_anos > 120:
        return None, "Data de nascimento implausível (idade acima de 120 anos)."

    return data, None

print(validar_data_nascimento("15/03/1998"))
print(validar_data_nascimento("31/02/2000"))
print(validar_data_nascimento("01/01/2099"))
