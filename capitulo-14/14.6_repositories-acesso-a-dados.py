# Repositories (acesso a dados)
# Manual do Desenvolvedor Python - Capitulo 14

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


repo = RepositorioJSON("teste_repo.json")
repo.salvar([{"nome": "Adry Alves", "idade": 56}])
print(repo.carregar())
