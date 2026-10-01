# Validação de e-mail
# Manual do Desenvolvedor Python - Capitulo 12

import re

def validar_email(email):
    padrao = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    if not re.match(padrao, email):
        return None, "Formato de e-mail inválido."
    return email.strip().lower(), None

print(validar_email("andy.angel@evento.com"))
print(validar_email("email_invalido"))
print(validar_email("  Gabriella@Evento.COM  ".strip()))
