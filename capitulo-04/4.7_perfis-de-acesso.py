# Perfis de acesso
# Manual do Desenvolvedor Python - Capitulo 4

perfil = "organizador"

if perfil == "visitante":
    print("Acesso: apenas às áreas públicas do evento.")
elif perfil == "organizador":
    print("Acesso: áreas públicas, backstage e painel administrativo.")
elif perfil == "seguranca":
    print("Acesso: áreas públicas, backstage e lista de bloqueio.")
else:
    print(f"Perfil desconhecido: '{perfil}'. Acesso negado por padrão.")
