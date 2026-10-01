# Requisitos
# Manual do Desenvolvedor Python - Capitulo 14

requisitos_sistema = {
    "cadastrar_visitante": "nome, idade e status de ingresso",
    "autorizar_entrada": "idade minima, ingresso valido, perfil nao bloqueado",
    "gerar_relatorio": "lista de visitantes com totais e percentuais",
    "persistir_dados": "sobreviver ao fechamento do programa",
}

for funcionalidade, descricao in requisitos_sistema.items():
    print(f"{funcionalidade}: {descricao}")
