# Erros de sintaxe versus erros de execução
# Manual do Desenvolvedor Python - Capitulo 11

codigo_com_erro = """
print("teste"
"""
try:
    compile(codigo_com_erro, "<string>", "exec")
except SyntaxError as erro:
    print(f"Erro de sintaxe detectado: {erro}")

codigo_correto = 'print("teste")'
compile(codigo_correto, "<string>", "exec")
print("Código correto compilado sem erro.")
