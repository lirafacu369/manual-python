# Cadastro estruturado com funções
# Manual do Desenvolvedor Python - Capitulo 8

def criar_visitante(nome, idade, vip=False):
    return {"nome": nome.strip().title(), "idade": idade, "vip": vip}


v1 = criar_visitante("  andy angel  ", 25)
v2 = criar_visitante("lu brandão", 30, vip=True)

print(v1)
print(v2)
