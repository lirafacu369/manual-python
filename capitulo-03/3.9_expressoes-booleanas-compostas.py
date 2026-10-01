# Expressões booleanas compostas
# Manual do Desenvolvedor Python - Capitulo 3

idade = 16
tem_responsavel_presente = True
eh_evento_livre = False

# regra: pode entrar se (for maior de idade) OU (for menor mas COM responsável), 
#        E o evento permitir a faixa etária dele
pode_entrar = (idade >= 18 or tem_responsavel_presente) and (eh_evento_livre or idade >= 18)

print(f"Pode entrar: {pode_entrar}")
