# O bloco `except` e múltiplas exceções
# Manual do Desenvolvedor Python - Capitulo 11

def processar_valor(valor_texto):
    try:
        valor = float(valor_texto)
        return valor
    except ValueError:
        print(f"'{valor_texto}' não é um número válido.")
        return None
    except TypeError:
        print("Tipo de dado inesperado.")
        return None


print(processar_valor("89.90"))
print(processar_valor("abc"))
print(processar_valor(None))
