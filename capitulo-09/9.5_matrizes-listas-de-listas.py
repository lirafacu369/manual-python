# Matrizes (listas de listas)
# Manual do Desenvolvedor Python - Capitulo 9

mapa_assentos = [
    ["livre", "ocupado", "livre"],
    ["ocupado", "ocupado", "livre"],
]

for linha_idx, linha in enumerate(mapa_assentos):
    for coluna_idx, assento in enumerate(linha):
        print(f"Fileira {linha_idx}, Assento {coluna_idx}: {assento}")
