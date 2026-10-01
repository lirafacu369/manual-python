# Condição de parada
# Manual do Desenvolvedor Python - Capitulo 6

senha_correta = "evento2026"
senhas_simuladas = ["senha1", "senha2", "evento2026"]
indice = 0
tentativas = 0

while senhas_simuladas[indice] != senha_correta:
    tentativas += 1
    indice += 1

tentativas += 1
print(f"Senha correta encontrada após {tentativas} tentativa(s).")
