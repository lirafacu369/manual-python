# Fila de visitantes (projeto prático do capítulo)
# Manual do Desenvolvedor Python - Capitulo 7

fila_espera = []

def entrar_na_fila(nome):
    fila_espera.append(nome)
    print(f"{nome} entrou na fila. Posição: {len(fila_espera)}")

def chamar_proximo():
    if not fila_espera:
        print("Fila vazia.")
        return None
    proximo = fila_espera.pop(0)
    print(f"Chamando: {proximo}")
    return proximo


entrar_na_fila("Andy Angel")
entrar_na_fila("Gabriella Santiago")
entrar_na_fila("Lu Brandão")

chamar_proximo()
chamar_proximo()

print(f"Restantes na fila: {fila_espera}")
