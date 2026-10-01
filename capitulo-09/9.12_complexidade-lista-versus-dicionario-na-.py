# Complexidade: lista versus dicionário na busca
# Manual do Desenvolvedor Python - Capitulo 9

import time

lista_grande = list(range(10000))

inicio = time.time()
encontrado_lista = 9999 in lista_grande
tempo_lista = time.time() - inicio

dicionario_grande = {i: True for i in range(10000)}
inicio = time.time()
encontrado_dict = 9999 in dicionario_grande
tempo_dict = time.time() - inicio

print(f"Busca em lista: {encontrado_lista}")
print(f"Busca em dicionário: {encontrado_dict}")
