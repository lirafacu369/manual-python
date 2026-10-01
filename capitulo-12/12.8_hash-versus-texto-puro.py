# Hash versus texto puro
# Manual do Desenvolvedor Python - Capitulo 12

import hashlib

def gerar_hash_senha(senha, sal="sal_fixo_para_exemplo_didatico"):
    texto_combinado = senha + sal
    return hashlib.sha256(texto_combinado.encode()).hexdigest()

senha_usuario = "Portaria2026"
hash_armazenado = gerar_hash_senha(senha_usuario)
print(f"Hash armazenado: {hash_armazenado}")

tentativa_login = "Portaria2026"
hash_tentativa = gerar_hash_senha(tentativa_login)
print(f"Senha confere: {hash_tentativa == hash_armazenado}")

tentativa_errada = "senha_errada"
print(f"Senha errada confere: {gerar_hash_senha(tentativa_errada) == hash_armazenado}")
