# `models.py` — a classe `Usuario`
# Manual do Desenvolvedor Python - Capitulo 15

class Usuario:
    def __init__(self, nome, perfil="visitante"):
        self.nome = nome.strip().title()
        self.perfil = perfil

    def to_dict(self):
        return {"nome": self.nome, "perfil": self.perfil}
