# Validação de formato de CPF
# Manual do Desenvolvedor Python - Capitulo 12

import re

def validar_formato_cpf(cpf):
    apenas_digitos = re.sub(r"[^0-9]", "", cpf)
    if len(apenas_digitos) != 11:
        return None, "CPF deve ter 11 dígitos."
    if apenas_digitos == apenas_digitos[0] * 11:
        return None, "CPF inválido (todos os dígitos iguais)."
    return apenas_digitos, None

print(validar_formato_cpf("123.456.789-09"))
print(validar_formato_cpf("111.111.111-11"))
print(validar_formato_cpf("123"))
