# `repositories.py` — persistência genérica
# Manual do Desenvolvedor Python - Capitulo 15

"""Camada de acesso a dados (persistência em JSON)."""

import json
import os


class RepositorioJSON:
    def __init__(self, caminho):
        self.caminho = caminho

    def carregar(self):
        if not os.path.exists(self.caminho):
            return []
        with open(self.caminho, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)

    def salvar(self, dados):
        with open(self.caminho, "w", encoding="utf-8") as arquivo:
            json.dump(dados, arquivo, ensure_ascii=False, indent=2)
