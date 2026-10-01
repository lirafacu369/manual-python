# Logs básicos
# Manual do Desenvolvedor Python - Capitulo 11

import datetime

def registrar_log(mensagem, nivel="INFO"):
    momento = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{momento}] [{nivel}] {mensagem}")


registrar_log("Sistema iniciado.")
registrar_log("Falha ao validar idade.", nivel="ERROR")
