# Relatórios formatados
# Manual do Desenvolvedor Python - Capitulo 5

visitantes = ["Andy Angel", "Gabi Moreira", "João P"]

print("=" * 30)
print("RELATÓRIO DE VISITANTES")
print("=" * 30)

for indice, nome in enumerate(visitantes, start=1):
    print(f"{indice:>2} | {nome:<20}")

print("=" * 30)
print(f"Total: {len(visitantes)} visitantes")
