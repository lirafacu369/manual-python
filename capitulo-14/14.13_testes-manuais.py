# Testes manuais
# Manual do Desenvolvedor Python - Capitulo 14

def testar_fluxo_cadastro():
    casos = [
        ("Andy Angel", "52", True),
        ("", "30", False),
        ("Gabi Moreira", "abc", False),
    ]
    for nome, idade_texto, deveria_passar in casos:
        nome_tratado = nome.strip().title()
        try:
            idade = int(idade_texto)
            sucesso = bool(nome_tratado) and 0 <= idade <= 120
        except ValueError:
            sucesso = False
        status = "OK" if sucesso == deveria_passar else "FALHOU"
        print(f"[{status}] nome='{nome}', idade='{idade_texto}' -> sucesso={sucesso}")

testar_fluxo_cadastro()
