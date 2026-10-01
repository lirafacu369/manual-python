# Models (modelos de dados)
# Manual do Desenvolvedor Python - Capitulo 14

class Visitante:
    def __init__(self, nome, idade, vip=False):
        self.nome = nome.strip().title()
        self.idade = idade
        self.vip = vip

    def maior_de_idade(self):
        return self.idade >= 18

    def to_dict(self):
        return {"nome": self.nome, "idade": self.idade, "vip": self.vip}


v = Visitante("andy angel", 52, vip=True)
print(v.to_dict())
print(f"Maior de idade: {v.maior_de_idade()}")
