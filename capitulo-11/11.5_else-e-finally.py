# `else` e `finally`
# Manual do Desenvolvedor Python - Capitulo 11

def abrir_e_processar(numero_texto):
    try:
        numero = int(numero_texto)
    except ValueError:
        print("Entrada inválida.")
    else:
        print(f"Processamento bem-sucedido: {numero * 2}")
    finally:
        print("Limpeza/encerramento executado sempre.")


abrir_e_processar("10")
print("---")
abrir_e_processar("abc")
