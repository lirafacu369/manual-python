# Camada de validação completa (projeto prático do capítulo)
# Manual do Desenvolvedor Python - Capitulo 12

class ValidadorCadastro:
    def validar(self, dados):
        erros = []

        nome = dados.get("nome", "").strip()
        if not nome:
            erros.append("Nome é obrigatório.")

        idade_texto = dados.get("idade", "")
        try:
            idade = int(idade_texto)
            if idade < 0 or idade > 120:
                erros.append("Idade fora da faixa plausível.")
        except (ValueError, TypeError):
            erros.append("Idade inválida.")

        email = dados.get("email", "")
        import re
        if not re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", email):
            erros.append("E-mail inválido.")

        if erros:
            return False, erros
        return True, []


validador = ValidadorCadastro()
valido, erros = validador.validar({"nome": "Andy Angel", "idade": "25", "email": "andy@evento.com"})
print(f"Válido: {valido}, Erros: {erros}")

valido2, erros2 = validador.validar({"nome": "", "idade": "abc", "email": "invalido"})
print(f"Válido: {valido2}, Erros: {erros2}")
