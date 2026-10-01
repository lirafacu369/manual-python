# O operador `and`
# Manual do Desenvolvedor Python - Capitulo 3

idade = 22
tem_ingresso = True
documento_valido = True

pode_entrar = idade >= 18 and tem_ingresso and documento_valido
print(f"Pode entrar: {pode_entrar}")

# short-circuit: se a primeira condição for False, o Python nem avalia a segunda
def checagem_com_aviso():
    print("Checagem cara sendo executada...")
    return True

resultado = False and checagem_com_aviso()
print(f"Resultado: {resultado}")
# repare que "Checagem cara sendo executada..." NUNCA é impresso
