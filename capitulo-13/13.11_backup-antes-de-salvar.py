# Backup antes de salvar
# Manual do Desenvolvedor Python - Capitulo 13

import json
import shutil
import os

def salvar_com_backup(caminho, dados):
    if os.path.exists(caminho):
        shutil.copy(caminho, caminho + ".bak")
    with open(caminho, "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, ensure_ascii=False, indent=2)

salvar_com_backup("dados_com_backup.json", [{"nome": "Andy Angel"}])
salvar_com_backup("dados_com_backup.json", [{"nome": "Lu Brandão"}])

print(f"Backup existe: {os.path.exists('dados_com_backup.json.bak')}")
with open("dados_com_backup.json.bak", "r", encoding="utf-8") as arquivo:
    print("Conteúdo do backup:", arquivo.read())
