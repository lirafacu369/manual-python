# Funções puras
# Manual do Desenvolvedor Python - Capitulo 10

def dobrar_pura(numero):
    return numero * 2

contador_externo = 0
def incrementar_impura():
    global contador_externo
    contador_externo += 1
    return contador_externo

print(dobrar_pura(5))
print(dobrar_pura(5))

print(incrementar_impura())
print(incrementar_impura())
