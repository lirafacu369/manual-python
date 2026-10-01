# Services (serviços de regra de negócio)
# Manual do Desenvolvedor Python - Capitulo 14

class ServicoValidacao:
    def validar_idade(self, idade_texto):
        try:
            idade = int(idade_texto)
        except ValueError:
            return None, "Idade invalida"
        if idade < 0 or idade > 120:
            return None, "Idade fora da faixa plausivel"
        return idade, None

    def validar_nome(self, nome):
        nome_tratado = nome.strip()
        if not nome_tratado:
            return None, "Nome obrigatorio"
        return nome_tratado.title(), None


servico = ServicoValidacao()
print(servico.validar_idade("24"))
print(servico.validar_nome("  joão p  "))
