# Cópia de listas
# Manual do Desenvolvedor Python - Capitulo 7

original = ["Andy Angel", "Lu Brandão"]

referencia = original
copia_rasa = original.copy()
copia_slice = original[:]

referencia.append("Alterou original")

print(f"Original: {original}")
print(f"Referência (mesma lista): {referencia}")
print(f"Cópia .copy(): {copia_rasa}")
print(f"Cópia [:]: {copia_slice}")
