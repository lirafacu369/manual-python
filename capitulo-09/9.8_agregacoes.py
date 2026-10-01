# Agregações
# Manual do Desenvolvedor Python - Capitulo 9

visitantes = [
    {"nome": "Andy Angel", "idade": 25},
    {"nome": "Lu Brandão", "idade": 17},
    {"nome": "João P", "idade": 30},
]

idades = [v["idade"] for v in visitantes]

media_idade = sum(idades) / len(idades)
idade_maxima = max(idades)
idade_minima = min(idades)

print(f"Média de idade: {media_idade:.1f}")
print(f"Idade máxima: {idade_maxima}")
print(f"Idade mínima: {idade_minima}")
