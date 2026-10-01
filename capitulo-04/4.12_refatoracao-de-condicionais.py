# Refatoração de condicionais
# Manual do Desenvolvedor Python - Capitulo 4

def verificar_acesso_v1(idade, tem_ingresso, perfil):
    # versão original: aninhada e difícil de seguir
    if tem_ingresso:
        if idade >= 18:
            if perfil != "bloqueado":
                return "Acesso liberado."
            else:
                return "Acesso negado: perfil bloqueado."
        else:
            return "Acesso negado: menor de idade."
    else:
        return "Acesso negado: sem ingresso."


def verificar_acesso_v2(idade, tem_ingresso, perfil):
    # versão refatorada: guard clauses, sem aninhamento
    if not tem_ingresso:
        return "Acesso negado: sem ingresso."
    if idade < 18:
        return "Acesso negado: menor de idade."
    if perfil == "bloqueado":
        return "Acesso negado: perfil bloqueado."
    return "Acesso liberado."


# confirmando que as duas versões produzem o MESMO resultado:
casos_teste = [(20, True, "normal"), (15, True, "normal"), (20, False, "normal"), (20, True, "bloqueado")]
for idade, ingresso, perfil in casos_teste:
    r1 = verificar_acesso_v1(idade, ingresso, perfil)
    r2 = verificar_acesso_v2(idade, ingresso, perfil)
    print(f"v1: {r1} | v2: {r2} | iguais: {r1 == r2}")
