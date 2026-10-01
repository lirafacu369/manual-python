# Normalização de dados
# Manual do Desenvolvedor Python - Capitulo 8

def normalizar_chaves(dicionario_bruto):
    return {chave.strip().lower(): valor for chave, valor in dicionario_bruto.items()}


dados_brutos = {"  Nome ": "João P", "IDADE": 28, " Vip": True}
dados_normalizados = normalizar_chaves(dados_brutos)

print(dados_normalizados)
