# O operador `or`
# Manual do Desenvolvedor Python - Capitulo 3

eh_convidado_vip = False
eh_organizador = True
tem_cortesia = False

entrada_liberada_sem_pagamento = eh_convidado_vip or eh_organizador or tem_cortesia
print(f"Entrada liberada sem pagamento: {entrada_liberada_sem_pagamento}")

# short-circuit com or: primeira condição True já resolve, sem checar as demais
def checagem_cara():
    print("Checagem cara sendo executada...")
    return True

resultado = True or checagem_cara()
print(f"Resultado: {resultado}")
# "Checagem cara sendo executada..." não é impresso aqui também
