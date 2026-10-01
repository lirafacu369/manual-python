# Guard clauses (cláusulas de guarda)
# Manual do Desenvolvedor Python - Capitulo 4

def autorizar_entrada(idade, tem_responsavel, tem_ingresso):
    # guard clauses: trata os bloqueios primeiro e sai cedo
    if idade < 0:
        return "Erro: idade inválida."
    if not tem_ingresso:
        return "Entrada negada: sem ingresso."
    if idade < 18 and not tem_responsavel:
        return "Entrada negada: menor sem responsável."

    # se chegou até aqui, está tudo certo — "caminho feliz" sem aninhamento
    return "Entrada autorizada."


print(autorizar_entrada(16, False, True))
print(autorizar_entrada(16, True, True))
print(autorizar_entrada(25, False, True))
print(autorizar_entrada(25, False, False))
