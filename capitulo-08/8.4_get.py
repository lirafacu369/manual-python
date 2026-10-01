# `get()`
# Manual do Desenvolvedor Python - Capitulo 8

visitante = {"nome": "Andy Angel", "idade": 25}

documento = visitante.get("documento")
documento_com_padrao = visitante.get("documento", "não informado")
nome = visitante.get("nome")

print(f"Documento (sem padrão): {documento}")
print(f"Documento (com padrão): {documento_com_padrao}")
print(f"Nome: {nome}")
