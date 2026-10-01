# Configuração centralizada
# Manual do Desenvolvedor Python - Capitulo 14

CONFIGURACAO = {
    "arquivo_dados": "visitantes.json",
    "idade_minima": 18,
    "capacidade_maxima_padrao": 200,
}

def obter_configuracao(chave):
    return CONFIGURACAO.get(chave)

print(obter_configuracao("idade_minima"))
print(obter_configuracao("chave_inexistente"))
