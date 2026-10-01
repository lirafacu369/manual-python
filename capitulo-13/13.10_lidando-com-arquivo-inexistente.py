# Lidando com arquivo inexistente
# Manual do Desenvolvedor Python - Capitulo 13

import json
import os

def carregar_visitantes(caminho):
    if not os.path.exists(caminho):
        return []
    with open(caminho, "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)

resultado = carregar_visitantes("arquivo_que_nao_existe.json")
print(f"Resultado: {resultado}")

resultado2 = carregar_visitantes("visitantes.json")
print(f"Resultado 2: {resultado2}")
