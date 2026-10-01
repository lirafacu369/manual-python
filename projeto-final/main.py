"""Ponto de entrada do sistema de portaria."""

from repositories import RepositorioJSON
from services import ServicoPortaria
from menu import Menu
import config


def executar():
    repositorio = RepositorioJSON(config.ARQUIVO_VISITANTES)
    servico = ServicoPortaria(repositorio)
    Menu(servico).iniciar()


if __name__ == "__main__":
    executar()
