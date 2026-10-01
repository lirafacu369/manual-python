# Fluxo de acesso (visão de ponta a ponta)
# Manual do Desenvolvedor Python - Capitulo 14

def fluxo_acesso(idade, tem_ingresso, perfil, idade_minima=18):
    if perfil == "bloqueado":
        return False, "Perfil bloqueado"
    if perfil in ("organizador", "seguranca"):
        return True, None
    if not tem_ingresso:
        return False, "Sem ingresso"
    if idade < idade_minima:
        return False, "Menor de idade"
    return True, None


print(fluxo_acesso(22, True, "visitante"))
print(fluxo_acesso(15, True, "visitante"))
