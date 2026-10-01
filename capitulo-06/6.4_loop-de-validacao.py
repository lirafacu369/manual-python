# Loop de validação
# Manual do Desenvolvedor Python - Capitulo 6

entradas_simuladas = ["-5", "abc", "25"]
indice = 0
idade = None

while idade is None:
    entrada = entradas_simuladas[indice]
    indice += 1
    try:
        valor = int(entrada)
        if valor < 0 or valor > 120:
            print(f"'{entrada}' fora da faixa plausível. Tente novamente.")
        else:
            idade = valor
    except ValueError:
        print(f"'{entrada}' não é um número válido. Tente novamente.")

print(f"Idade validada: {idade}")
