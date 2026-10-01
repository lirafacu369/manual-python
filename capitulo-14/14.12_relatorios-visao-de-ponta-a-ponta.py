# Relatórios (visão de ponta a ponta)
# Manual do Desenvolvedor Python - Capitulo 14

def gerar_relatorio_simples(visitantes):
    total = len(visitantes)
    maiores = len([v for v in visitantes if v["idade"] >= 18])
    linhas = [f"Total de visitantes: {total}", f"Maiores de idade: {maiores}"]
    return "\n".join(linhas)


visitantes_teste = [{"nome": "Lu Brandão", "idade": 22}, {"nome": "Menor Exemplo", "idade": 15}]
print(gerar_relatorio_simples(visitantes_teste))
