# Cadastro inicial (projeto prático do capítulo)
# Manual do Desenvolvedor Python - Capitulo 2

print("=" * 40)
print("CADASTRO DE VISITANTE")
print("=" * 40)

nome_bruto = input("Nome completo: ")
nome = nome_bruto.strip().title()

idade_texto = input("Idade: ")
idade = int(idade_texto)

idade_minima = 18
maior_de_idade = idade >= idade_minima

documento = None  # campo opcional, ainda não capturado

print()
print(f"Visitante: {nome}")
print(f"Idade: {idade} anos")
print(f"Maior de idade: {maior_de_idade}")
print(f"Documento informado: {documento is not None}")
