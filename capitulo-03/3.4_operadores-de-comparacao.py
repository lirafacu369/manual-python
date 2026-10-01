# Operadores de comparação
# Manual do Desenvolvedor Python - Capitulo 3

idade = 25

# forma verbosa
maior_que_17 = idade > 17
menor_que_65 = idade < 65
esta_na_faixa = maior_que_17 and menor_que_65

# forma compacta equivalente (encadeamento de comparações, exclusivo do Python)
esta_na_faixa_compacto = 17 < idade < 65

print(f"Faixa (forma verbosa): {esta_na_faixa}")
print(f"Faixa (forma compacta): {esta_na_faixa_compacto}")
