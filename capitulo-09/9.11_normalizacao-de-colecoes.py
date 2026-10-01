# Normalização de coleções
# Manual do Desenvolvedor Python - Capitulo 9

def normalizar_visitante(dado_bruto):
    return {
        "nome": dado_bruto.get("nome", "").strip().title(),
        "idade": dado_bruto.get("idade", 0),
        "local": dado_bruto.get("local", "não informado").strip(),
    }


dados_brutos = [
    {"nome": "  andy angel  ", "idade": 25, "local": "salão principal"},
    {"nome": "lu brandão", "idade": 17},
]

normalizados = [normalizar_visitante(d) for d in dados_brutos]
for n in normalizados:
    print(n)
