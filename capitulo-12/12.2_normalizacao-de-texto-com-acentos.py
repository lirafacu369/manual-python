# Normalização de texto com acentos
# Manual do Desenvolvedor Python - Capitulo 12

import unicodedata

def remover_acentos(texto):
    forma_nfkd = unicodedata.normalize("NFKD", texto)
    return "".join(c for c in forma_nfkd if not unicodedata.combining(c))

nome = "Gabriélla Sántiágo"
print(remover_acentos(nome))
print(remover_acentos(nome).lower())
