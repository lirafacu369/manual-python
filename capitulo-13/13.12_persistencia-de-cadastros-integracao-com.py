# Persistência de cadastros (integração completa)
# Manual do Desenvolvedor Python - Capitulo 13

import json
import os

ARQUIVO_DADOS = "cadastros_teste.json"

def carregar_visitantes():
    if not os.path.exists(ARQUIVO_DADOS):
        return []
    with open(ARQUIVO_DADOS, "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)

def salvar_visitantes(visitantes):
    with open(ARQUIVO_DADOS, "w", encoding="utf-8") as arquivo:
        json.dump(visitantes, arquivo, ensure_ascii=False, indent=2)

def cadastrar_visitante(nome, idade):
    visitantes = carregar_visitantes()
    visitantes.append({"nome": nome, "idade": idade})
    salvar_visitantes(visitantes)


cadastrar_visitante("Andy Angel", 25)
cadastrar_visitante("Gabi Moreira", 30)

visitantes_finais = carregar_visitantes()
print(f"Total persistido: {len(visitantes_finais)}")
for v in visitantes_finais:
    print(v)
