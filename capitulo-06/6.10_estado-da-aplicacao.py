# Estado da aplicação
# Manual do Desenvolvedor Python - Capitulo 6

estado = {"visitantes_cadastrados": 0, "evento_iniciado": False}

acoes_simuladas = ["cadastrar", "cadastrar", "iniciar", "status"]

for acao in acoes_simuladas:
    if acao == "cadastrar":
        estado["visitantes_cadastrados"] += 1
    elif acao == "iniciar":
        estado["evento_iniciado"] = True
    elif acao == "status":
        print(f"Visitantes: {estado['visitantes_cadastrados']}, Evento iniciado: {estado['evento_iniciado']}")
