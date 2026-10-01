# Senhas e segredos
# Manual do Desenvolvedor Python - Capitulo 12

def validar_forca_senha(senha):
    erros = []
    if len(senha) < 8:
        erros.append("mínimo de 8 caracteres")
    if not any(c.isupper() for c in senha):
        erros.append("pelo menos uma letra maiúscula")
    if not any(c.isdigit() for c in senha):
        erros.append("pelo menos um número")
    if erros:
        return False, f"Senha fraca: falta {', '.join(erros)}."
    return True, None

print(validar_forca_senha("abc123"))
print(validar_forca_senha("Portaria2026"))
