# Valores padrão
# Manual do Desenvolvedor Python - Capitulo 10

def criar_visitante(nome, idade, vip=False, documento=None):
    return {"nome": nome, "idade": idade, "vip": vip, "documento": documento}

v1 = criar_visitante("Andy Angel", 25)
v2 = criar_visitante("Lu Brandão", 30, vip=True)

print(v1)
print(v2)
