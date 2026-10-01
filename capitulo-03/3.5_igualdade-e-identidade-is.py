# Igualdade (`==`) e identidade (`is`)
# Manual do Desenvolvedor Python - Capitulo 3

lista_a = ["Andy Angel", "João P"]
lista_b = ["Andy Angel", "João P"]
lista_c = lista_a

print(f"lista_a == lista_b: {lista_a == lista_b}")  # True: mesmo conteúdo
print(f"lista_a is lista_b: {lista_a is lista_b}")  # False: objetos diferentes na memória
print(f"lista_a is lista_c: {lista_a is lista_c}")  # True: lista_c aponta para o MESMO objeto
