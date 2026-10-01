# Permissões
# Manual do Desenvolvedor Python - Capitulo 12

permissoes_por_perfil = {
    "visitante": ["ver_proprio_ingresso"],
    "organizador": ["ver_proprio_ingresso", "criar_evento", "ver_relatorios"],
    "seguranca": ["ver_proprio_ingresso", "validar_entrada", "ver_lista_bloqueio"],
}

def tem_permissao(perfil, acao):
    acoes_permitidas = permissoes_por_perfil.get(perfil, [])
    return acao in acoes_permitidas

print(tem_permissao("organizador", "criar_evento"))
print(tem_permissao("visitante", "criar_evento"))
print(tem_permissao("desconhecido", "ver_proprio_ingresso"))
