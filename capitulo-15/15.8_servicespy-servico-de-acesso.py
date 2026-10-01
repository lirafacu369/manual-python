# `services.py` — serviço de acesso
# Manual do Desenvolvedor Python - Capitulo 15

class ServicoAcesso:
    def __init__(self, idade_minima=18):
        self.idade_minima = idade_minima

    def autorizar(self, idade, tem_ingresso, perfil="visitante"):
        if perfil == "bloqueado":
            return False, "Perfil bloqueado"
        if perfil in ("organizador", "seguranca"):
            return True, None
        if not tem_ingresso:
            return False, "Sem ingresso"
        if idade < self.idade_minima:
            return False, "Menor de idade sem acompanhamento verificado"
        return True, None
