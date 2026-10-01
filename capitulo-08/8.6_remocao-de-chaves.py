# Remoção de chaves
# Manual do Desenvolvedor Python - Capitulo 8

visitante = {"nome": "Lu Brandão", "idade": 30, "documento": "123.456.789-00"}

documento_removido = visitante.pop("documento")
print(f"Removido: {documento_removido}")
print(visitante)

valor_padrao = visitante.pop("telefone", "campo não existia")
print(valor_padrao)
