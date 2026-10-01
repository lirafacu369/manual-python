# Service layer (projeto prático do capítulo)
# Manual do Desenvolvedor Python - Capitulo 10

def validar_idade(idade_texto):
    try:
        idade = int(idade_texto)
        if idade < 0 or idade > 120:
            return None, "Idade fora da faixa plausível"
        return idade, None
    except ValueError:
        return None, "Idade inválida"

def formatar_nome(nome):
    return nome.strip().title()


class ServicoVisitante:
    def __init__(self):
        self.visitantes = []

    def cadastrar(self, nome_bruto, idade_texto):
        nome = formatar_nome(nome_bruto)
        idade, erro = validar_idade(idade_texto)
        if erro:
            return None, erro

        visitante = {"nome": nome, "idade": idade, "maior_de_idade": idade >= 18}
        self.visitantes.append(visitante)
        return visitante, None

    def total_cadastrados(self):
        return len(self.visitantes)


servico = ServicoVisitante()
visitante1, erro1 = servico.cadastrar("  andy angel  ", "25")
visitante2, erro2 = servico.cadastrar("lu brandão", "abc")

print(f"Visitante 1: {visitante1}")
print(f"Visitante 2: {visitante2}, erro: {erro2}")
print(f"Total cadastrados: {servico.total_cadastrados()}")
