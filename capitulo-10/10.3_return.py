# `return`
# Manual do Desenvolvedor Python - Capitulo 10

def calcular_desconto(preco, percentual):
    return preco * (1 - percentual / 100)

preco_final = calcular_desconto(100, 15)
print(f"Preço com desconto: R$ {preco_final:.2f}")

def funcao_sem_return(valor):
    print(f"Recebi: {valor}")

resultado = funcao_sem_return("teste")
print(f"Retorno de função sem return: {resultado}")
