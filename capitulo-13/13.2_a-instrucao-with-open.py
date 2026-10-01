# A instrução `with open`
# Manual do Desenvolvedor Python - Capitulo 13

with open("teste2.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write("teste")

print("Arquivo fechado automaticamente pelo with.")

import os
print(f"Arquivo existe: {os.path.exists('teste2.txt')}")
