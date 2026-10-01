# Menu comercial completo (projeto prático do capítulo)
# Manual do Desenvolvedor Python - Capitulo 6

entradas_simuladas = ["1", "Andy Angel", "1", "Lu Brandão", "2", "0"]
indice = 0
visitantes = []

def proxima_entrada():
    global indice
    valor = entradas_simuladas[indice]
    indice += 1
    return valor


while True:
    opcao = proxima_entrada()

    if opcao == "1":
        nome = proxima_entrada().strip().title()
        visitantes.append(nome)
        print(f"Visitante '{nome}' cadastrado.")
    elif opcao == "2":
        print(f"Total de visitantes cadastrados: {len(visitantes)}")
        for i, v in enumerate(visitantes, start=1):
            print(f"  {i}. {v}")
    elif opcao == "0":
        print("Encerrando o sistema de portaria...")
        break
    else:
        print("Opção inválida.")
