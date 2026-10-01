# List comprehensions
# Manual do Desenvolvedor Python - Capitulo 7

idades = [25, 17, 42, 8, 60]

maiores_de_idade = [idade for idade in idades if idade >= 18]
dobradas = [idade * 2 for idade in idades]

nomes = ["andy angel", "lu brandão", "joão p"]
nomes_formatados = [nome.title() for nome in nomes]

print(f"Maiores de idade: {maiores_de_idade}")
print(f"Dobradas: {dobradas}")
print(f"Nomes formatados: {nomes_formatados}")
