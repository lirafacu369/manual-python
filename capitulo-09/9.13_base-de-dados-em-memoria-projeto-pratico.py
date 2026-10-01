# Base de dados em memória (projeto prático do capítulo)
# Manual do Desenvolvedor Python - Capitulo 9

class BaseDeDados:
    def __init__(self):
        self.visitantes = []
        self.eventos = {}

    def adicionar_visitante(self, visitante):
        self.visitantes.append(visitante)

    def adicionar_evento(self, codigo, evento):
        self.eventos[codigo] = evento

    def buscar_visitantes_por_evento(self, codigo_evento):
        return [v for v in self.visitantes if v.get("evento") == codigo_evento]


db = BaseDeDados()
db.adicionar_evento("evt001", {"nome": "Festa Andy Angel"})
db.adicionar_visitante({"nome": "Lu Brandão", "evento": "evt001"})
db.adicionar_visitante({"nome": "João P", "evento": "evt002"})

resultado = db.buscar_visitantes_por_evento("evt001")
print(f"Visitantes do evt001: {resultado}")
