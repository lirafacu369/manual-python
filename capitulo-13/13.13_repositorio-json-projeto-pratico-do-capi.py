# Repositório JSON (projeto prático do capítulo)
# Manual do Desenvolvedor Python - Capitulo 13

import json
import os

class RepositorioVisitantes:
    def __init__(self, caminho_arquivo):
        self.caminho_arquivo = caminho_arquivo

    def _carregar(self):
        if not os.path.exists(self.caminho_arquivo):
            return []
        with open(self.caminho_arquivo, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)

    def _salvar(self, dados):
        with open(self.caminho_arquivo, "w", encoding="utf-8") as arquivo:
            json.dump(dados, arquivo, ensure_ascii=False, indent=2)

    def adicionar(self, visitante):
        dados = self._carregar()
        dados.append(visitante)
        self._salvar(dados)
        return visitante

    def listar(self):
        return self._carregar()

    def buscar_por_nome(self, nome):
        return [v for v in self._carregar() if v["nome"] == nome]


repo = RepositorioVisitantes("repositorio_teste.json")
repo.adicionar({"nome": "Andy Angel", "idade": 25})
repo.adicionar({"nome": "Lu Brandão", "idade": 17})

print(f"Todos: {repo.listar()}")
print(f"Busca: {repo.buscar_por_nome('Lu Brandão')}")
