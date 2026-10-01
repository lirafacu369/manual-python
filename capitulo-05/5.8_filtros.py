# Filtros
# Manual do Desenvolvedor Python - Capitulo 5

visitantes = [
    {"nome": "Andy Angel", "idade": 25},
    {"nome": "Gabriella Santiago", "idade": 16},
    {"nome": "Lu Brandão", "idade": 30},
]

maiores_de_idade = []
for visitante in visitantes:
    if visitante["idade"] >= 18:
        maiores_de_idade.append(visitante["nome"])

print(f"Maiores de idade: {maiores_de_idade}")
