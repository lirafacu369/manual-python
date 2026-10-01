# Processamento em lote (projeto prático do capítulo)
# Manual do Desenvolvedor Python - Capitulo 5

visitantes_brutos = [
    {"nome": "  andy angel  ", "idade_texto": "25"},
    {"nome": "gabriella santiago", "idade_texto": "abc"},
    {"nome": "lu brandão", "idade_texto": "16"},
]

processados = []
erros = []

for dado in visitantes_brutos:
    nome = dado["nome"].strip().title()
    try:
        idade = int(dado["idade_texto"])
        processados.append({"nome": nome, "idade": idade})
    except ValueError:
        erros.append(f"{nome}: idade inválida ('{dado['idade_texto']}')")

print("Processados com sucesso:")
for p in processados:
    print(f"  {p['nome']}, {p['idade']} anos")

print("Erros encontrados:")
for e in erros:
    print(f"  {e}")
