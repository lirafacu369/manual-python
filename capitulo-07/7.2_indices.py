# Índices
# Manual do Desenvolvedor Python - Capitulo 7

visitantes = ["Andy Angel", "Gabriella Santiago", "Lu Brandão", "João P"]

print(f"Primeiro: {visitantes[0]}")
print(f"Segundo: {visitantes[1]}")
print(f"Último: {visitantes[-1]}")
print(f"Penúltimo: {visitantes[-2]}")

try:
    print(visitantes[10])
except IndexError as erro:
    print(f"Erro: {erro}")
