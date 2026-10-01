# Falhas previsíveis versus inesperadas
# Manual do Desenvolvedor Python - Capitulo 11

def dividir_ingressos_por_lote(total, tamanho_lote):
    if tamanho_lote <= 0:
        return None, "Tamanho de lote deve ser maior que zero."

    try:
        lotes = total // tamanho_lote
        resto = total % tamanho_lote
        return (lotes, resto), None
    except TypeError:
        return None, "Os valores fornecidos devem ser numéricos."


resultado, erro = dividir_ingressos_por_lote(137, 20)
print(resultado, erro)

resultado2, erro2 = dividir_ingressos_por_lote(137, 0)
print(resultado2, erro2)
