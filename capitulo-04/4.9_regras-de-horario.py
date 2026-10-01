# Regras de horário
# Manual do Desenvolvedor Python - Capitulo 4

from datetime import datetime

hora_atual = datetime.now().hour  # hora do sistema, de 0 a 23
abertura = 18
fechamento = 23

if abertura <= hora_atual < fechamento:
    print(f"Portaria aberta (agora são {hora_atual}h). Entrada liberada.")
else:
    print(f"Portaria fechada (agora são {hora_atual}h). Entrada apenas das {abertura}h às {fechamento}h.")
