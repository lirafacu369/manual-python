# Módulo e divisão inteira na prática
# Manual do Desenvolvedor Python - Capitulo 3

numero_visitante = 47

# a cada 10º visitante, o sistema destaca no relatório (padrão comum em sistemas reais)
destaque_no_relatorio = numero_visitante % 10 == 0

print(f"Visitante número {numero_visitante}")
print(f"É um marco de dezena? {destaque_no_relatorio}")

# checar se um número é par ou ímpar usando módulo
def eh_par(numero):
    return numero % 2 == 0

print(f"47 é par? {eh_par(47)}")
print(f"48 é par? {eh_par(48)}")
