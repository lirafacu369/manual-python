# Auditoria
# Manual do Desenvolvedor Python - Capitulo 12

import datetime

registro_auditoria = []

def registrar_acao(usuario, acao, sucesso):
    entrada = {
        "momento": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "usuario": usuario,
        "acao": acao,
        "sucesso": sucesso,
    }
    registro_auditoria.append(entrada)

registrar_acao("andy.angel", "login", True)
registrar_acao("lu.brandao", "login", False)
registrar_acao("andy.angel", "criar_evento", True)

for entrada in registro_auditoria:
    print(entrada)
