# Evitando condicionais frágeis
# Manual do Desenvolvedor Python - Capitulo 4

resposta = "Sim"  # usuário digitou com maiúscula

# forma FRÁGIL: falha se o usuário digitar "Sim", "SIM" ou " sim"
if resposta == "sim":
    print("Confirmado (forma frágil).")
else:
    print("Não reconhecido (forma frágil) — mas era 'Sim', deveria ter funcionado!")

# forma ROBUSTA: normaliza antes de comparar
resposta_normalizada = resposta.strip().lower()
if resposta_normalizada == "sim":
    print("Confirmado (forma robusta).")
else:
    print("Não reconhecido (forma robusta).")
