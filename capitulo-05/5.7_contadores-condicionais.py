# Contadores condicionais
# Manual do Desenvolvedor Python - Capitulo 5

idades_visitantes = [15, 22, 17, 30, 45, 16, 60]

menores_de_idade = 0
for idade in idades_visitantes:
    if idade < 18:
        menores_de_idade += 1

print(f"Total de visitantes: {len(idades_visitantes)}")
print(f"Menores de idade: {menores_de_idade}")
