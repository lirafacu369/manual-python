# Type hints
# Manual do Desenvolvedor Python - Capitulo 10

def calcular_total(preco: float, quantidade: int) -> float:
    return preco * quantidade

def formatar_nome(nome: str) -> str:
    return nome.strip().title()

total = calcular_total(89.90, 3)
nome = formatar_nome("  andy angel  ")
print(f"Total: {total}")
print(f"Nome: {nome}")
