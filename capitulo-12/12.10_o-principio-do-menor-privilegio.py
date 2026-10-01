# O princípio do menor privilégio
# Manual do Desenvolvedor Python - Capitulo 12

def criar_usuario_padrao(nome, perfil_solicitado):
    perfis_validos = ["visitante", "organizador", "seguranca"]
    perfil_seguro = perfil_solicitado if perfil_solicitado in perfis_validos else "visitante"
    return {"nome": nome, "perfil": perfil_seguro}

print(criar_usuario_padrao("Andy Angel", "organizador"))
print(criar_usuario_padrao("Lu Brandão", "administrador_totall"))
