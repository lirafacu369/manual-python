# Status de evento
# Manual do Desenvolvedor Python - Capitulo 4

status_evento = "em_andamento"

if status_evento == "planejamento":
    print("Inscrições ainda não abertas.")
elif status_evento == "inscricoes_abertas":
    print("Você pode se inscrever agora.")
elif status_evento == "em_andamento":
    print("Evento já começou — check-in de última hora disponível.")
elif status_evento == "encerrado":
    print("Este evento já foi encerrado.")
else:
    print(f"Status desconhecido: '{status_evento}'.")
