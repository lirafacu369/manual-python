# Tentativas de acesso limitadas
# Manual do Desenvolvedor Python - Capitulo 6

senha_correta = "portaria123"
tentativas_simuladas = ["errada1", "errada2", "portaria123"]
indice = 0
max_tentativas = 3

while indice < max_tentativas:
    tentativa = tentativas_simuladas[indice]
    indice += 1

    if tentativa == senha_correta:
        print("Acesso concedido.")
        break

    print(f"Senha incorreta. Tentativa {indice} de {max_tentativas}.")
else:
    print("Número máximo de tentativas excedido. Acesso bloqueado.")
