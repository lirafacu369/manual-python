# Separação de arquivos do projeto
# Manual do Desenvolvedor Python - Capitulo 14

estrutura_projeto = {
    "main.py": "ponto de entrada, chama Menu",
    "models.py": "classes Usuario, Visitante, Evento",
    "services.py": "ServicoValidacao, ServicoAcesso",
    "repositories.py": "RepositorioJSON",
    "menu.py": "classe Menu (interface de terminal)",
    "config.py": "configuracoes centralizadas",
}

for arquivo, responsabilidade in estrutura_projeto.items():
    print(f"{arquivo}: {responsabilidade}")
