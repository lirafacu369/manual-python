# O operador `not`
# Manual do Desenvolvedor Python - Capitulo 3

esta_na_lista_negra = False
documento_expirado = False

pode_entrar = not esta_na_lista_negra and not documento_expirado
print(f"Pode entrar: {pode_entrar}")

# cuidado comum: not tem precedência MAIOR que and/or
# not esta_na_lista_negra and not documento_expirado
# é equivalente a:
# (not esta_na_lista_negra) and (not documento_expirado)
# — não a "not (esta_na_lista_negra and not documento_expirado)"
