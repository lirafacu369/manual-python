# Fluxo de autorização completo (projeto prático do capítulo)
# Manual do Desenvolvedor Python - Capitulo 4

def autorizar_entrada_evento(idade, tem_ingresso, perfil, status_evento):
    if status_evento != "em_andamento":
        return f"Entrada negada: evento está '{status_evento}', não em andamento."

    if perfil == "bloqueado":
        return "Entrada negada: perfil bloqueado pela organização."

    if perfil in ("organizador", "seguranca"):
        return f"Entrada autorizada: acesso de {perfil}."

    if not tem_ingresso:
        return "Entrada negada: visitante sem ingresso."

    if idade < 0 or idade > 120:
        return f"Entrada negada: idade {idade} fora de uma faixa plausível."

    if idade < 18:
        return "Entrada negada: menor de idade sem acompanhamento verificado."

    return "Entrada autorizada: visitante regular."


casos = [
    (25, True, "visitante", "em_andamento"),
    (16, True, "visitante", "em_andamento"),
    (30, False, "visitante", "em_andamento"),
    (40, False, "organizador", "em_andamento"),
    (25, True, "visitante", "planejamento"),
    (25, True, "bloqueado", "em_andamento"),
]

for idade, ingresso, perfil, status in casos:
    resultado = autorizar_entrada_evento(idade, ingresso, perfil, status)
    print(f"idade={idade}, ingresso={ingresso}, perfil={perfil}, status={status}")
    print(f"  -> {resultado}")
