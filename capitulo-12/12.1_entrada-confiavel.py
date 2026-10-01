# Entrada confiável
# Manual do Desenvolvedor Python - Capitulo 12

def sanitizar_texto(entrada):
    if not isinstance(entrada, str):
        return None
    texto = entrada.strip()
    if len(texto) == 0 or len(texto) > 200:
        return None
    return texto

print(sanitizar_texto("  Andy Angel  "))
print(sanitizar_texto(""))
print(sanitizar_texto(123))
