# Busca sequencial
# Manual do Desenvolvedor Python - Capitulo 5

visitantes = ["Andy Angel", "Gabriella Santiago", "Lu Brandão"]
nome_procurado = "Lu Brandão"

encontrado = False
for visitante in visitantes:
    if visitante == nome_procurado:
        encontrado = True
        break

print(f"'{nome_procurado}' está na lista? {encontrado}")
