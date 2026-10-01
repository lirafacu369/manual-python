# Condições aninhadas
# Manual do Desenvolvedor Python - Capitulo 4

idade = 16
tem_responsavel = True

if idade >= 18:
    print("Entrada autorizada: maior de idade.")
else:
    if tem_responsavel:
        print("Entrada autorizada: menor acompanhado de responsável.")
    else:
        print("Entrada negada: menor sem responsável.")
