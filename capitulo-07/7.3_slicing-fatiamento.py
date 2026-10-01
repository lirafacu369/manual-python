# Slicing (fatiamento)
# Manual do Desenvolvedor Python - Capitulo 7

visitantes = ["Andy Angel", "Gabriella Santiago", "Lu Brandão", "Adry Alves", "Gabi Moreira"]

primeiros_tres = visitantes[0:3]
do_terceiro_em_diante = visitantes[2:]
ultimos_dois = visitantes[-2:]
todos_invertidos = visitantes[::-1]

print(f"Primeiros três: {primeiros_tres}")
print(f"Do terceiro em diante: {do_terceiro_em_diante}")
print(f"Últimos dois: {ultimos_dois}")
print(f"Invertidos: {todos_invertidos}")
