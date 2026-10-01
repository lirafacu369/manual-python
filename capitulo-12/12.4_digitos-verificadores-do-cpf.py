# Dígitos verificadores do CPF
# Manual do Desenvolvedor Python - Capitulo 12

def calcular_digito_verificador(cpf_parcial):
    soma = 0
    multiplicador = len(cpf_parcial) + 1
    for digito in cpf_parcial:
        soma += int(digito) * multiplicador
        multiplicador -= 1
    resto = soma % 11
    return 0 if resto < 2 else 11 - resto

def validar_cpf_completo(cpf_digitos):
    primeiros_nove = cpf_digitos[:9]
    digito1 = calcular_digito_verificador(primeiros_nove)
    primeiros_dez = primeiros_nove + str(digito1)
    digito2 = calcular_digito_verificador(primeiros_dez)
    cpf_calculado = primeiros_dez + str(digito2)
    return cpf_calculado == cpf_digitos

print(validar_cpf_completo("11144477735"))
print(validar_cpf_completo("12345678900"))
