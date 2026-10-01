# Manual do Desenvolvedor Python — Código-fonte

Código-fonte completo do livro **"Manual do Desenvolvedor Python: Do Zero ao Sistema Comercial"**, de Anderson Lira (ISBN 978-65-02-39876-0).

Todos os exemplos foram testados individualmente antes da publicação — nenhum código deste repositório é ilustrativo ou incompleto.

## Estrutura

```
manual-python-anderson-lira/
├── capitulo-01/   até   capitulo-15/
│   └── um arquivo .py por exemplo prático do livro,
│       nomeado pelo número da seção (ex: 3.7_o-operador-or.py)
└── projeto-final/
    └── o sistema de portaria completo (Capítulo 15), pronto para rodar:
        main.py, config.py, models.py, services.py, repositories.py, menu.py
```

## Como usar os exemplos dos capítulos

Cada arquivo em `capitulo-XX/` corresponde a um exemplo prático específico do livro. Basta rodar:

```bash
python capitulo-03/3.7_o-operador-or.py
```

(ou abrir o arquivo no VS Code e usar `Ctrl+F5`, como ensinado no Capítulo 1)

## Como rodar o projeto final

```bash
cd projeto-final
python main.py
```

Na primeira execução, o sistema cria automaticamente o arquivo `visitantes.json` com a lista de visitantes cadastrados — ele não vem incluído no repositório de propósito, para que você comece com uma base de dados limpa.

## Requisitos

- Python 3.10 ou superior
- Nenhuma biblioteca externa é necessária (tudo usa apenas a biblioteca padrão do Python)

## Sobre o livro

Este repositório acompanha o livro, mas cada capítulo também pode ser lido e seguido de forma independente. Consulte o **Apêndice C** do livro para o guia completo de instalação de todas as ferramentas usadas (Python, VS Code, Google Colab, Git).

## Licença

O código-fonte deste repositório está disponível para fins de estudo e aprendizado, acompanhando o conteúdo do livro.
