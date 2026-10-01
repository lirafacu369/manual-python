# Escopo de variáveis
# Manual do Desenvolvedor Python - Capitulo 10

total_global = 100

def modificar_local():
    total_global = 50
    print(f"Dentro da função: {total_global}")

modificar_local()
print(f"Fora da função: {total_global}")

def modificar_com_global():
    global total_global
    total_global = 999

modificar_com_global()
print(f"Depois de modificar com global: {total_global}")
