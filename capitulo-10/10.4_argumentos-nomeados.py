# Argumentos nomeados
# Manual do Desenvolvedor Python - Capitulo 10

def criar_ingresso(nome, tipo, preco):
    return f"{nome} - {tipo} - R$ {preco:.2f}"

ingresso1 = criar_ingresso("Andy Angel", "VIP", 250.00)
ingresso2 = criar_ingresso(preco=89.90, nome="Lu Brandão", tipo="Comum")

print(ingresso1)
print(ingresso2)
