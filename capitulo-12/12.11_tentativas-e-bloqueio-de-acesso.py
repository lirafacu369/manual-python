# Tentativas e bloqueio de acesso
# Manual do Desenvolvedor Python - Capitulo 12

class ControleDeAcesso:
    def __init__(self, max_tentativas=3):
        self.tentativas_por_usuario = {}
        self.max_tentativas = max_tentativas

    def registrar_tentativa_falha(self, usuario):
        self.tentativas_por_usuario[usuario] = self.tentativas_por_usuario.get(usuario, 0) + 1

    def esta_bloqueado(self, usuario):
        return self.tentativas_por_usuario.get(usuario, 0) >= self.max_tentativas

    def resetar_tentativas(self, usuario):
        self.tentativas_por_usuario[usuario] = 0


controle = ControleDeAcesso()
controle.registrar_tentativa_falha("andy.angel")
controle.registrar_tentativa_falha("andy.angel")
print(f"Bloqueado após 2 tentativas: {controle.esta_bloqueado('andy.angel')}")

controle.registrar_tentativa_falha("andy.angel")
print(f"Bloqueado após 3 tentativas: {controle.esta_bloqueado('andy.angel')}")
