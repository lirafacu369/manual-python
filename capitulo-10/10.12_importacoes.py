# Importações
# Manual do Desenvolvedor Python - Capitulo 10

from validacoes import validar_idade, formatar_nome
import validacoes

nome = formatar_nome("  andy angel  ")
idade, erro = validar_idade("25")
print(f"Nome: {nome}, Idade: {idade}, Erro: {erro}")

print(validacoes.formatar_nome("lu brandão"))
