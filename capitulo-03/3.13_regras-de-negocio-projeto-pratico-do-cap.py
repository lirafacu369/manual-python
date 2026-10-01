# Regras de negócio (projeto prático do capítulo)
# Manual do Desenvolvedor Python - Capitulo 3

print("=" * 40)
print("VALIDAÇÃO DE ENTRADA — EVENTO")
print("=" * 40)

nome = input("Nome do visitante: ").strip().title()
idade_texto = input("Idade: ")
tem_convite_texto = input("Possui convite? (sim/não): ").strip().lower()

try:
    idade = int(idade_texto)
    tem_convite = tem_convite_texto == "sim"

    maior_de_idade = idade >= 18
    pode_entrar = maior_de_idade and tem_convite

    print()
    print(f"Visitante: {nome}")
    print(f"Maior de idade: {maior_de_idade}")
    print(f"Tem convite: {tem_convite}")
    print(f"Entrada autorizada: {pode_entrar}")

    if not pode_entrar and not maior_de_idade:
        print("Motivo do bloqueio: menor de idade.")
    elif not pode_entrar and not tem_convite:
        print("Motivo do bloqueio: sem convite.")

except ValueError:
    print(f"Idade inválida: '{idade_texto}'.")
