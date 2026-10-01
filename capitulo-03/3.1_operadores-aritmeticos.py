# Operadores aritméticos
# Manual do Desenvolvedor Python - Capitulo 3

total_ingressos_vendidos = 137
ingressos_por_lote = 20

lotes_completos = total_ingressos_vendidos // ingressos_por_lote
ingressos_avulsos = total_ingressos_vendidos % ingressos_por_lote

print(f"Lotes completos: {lotes_completos}")
print(f"Ingressos avulsos no lote parcial: {ingressos_avulsos}")

# potenciação: capacidade de um espaço que dobra a cada andar
capacidade_por_andar = 50
andares = 3
capacidade_teorica_maxima = capacidade_por_andar ** andares
print(f"Capacidade teórica (exemplo ilustrativo): {capacidade_teorica_maxima}")
