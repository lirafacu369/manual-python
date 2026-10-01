# Mensagens de erro seguras
# Manual do Desenvolvedor Python - Capitulo 11

def processar_pagamento(dados_cartao):
    try:
        numero = dados_cartao["numero"]
        resultado = 100 / dados_cartao.get("parcelas", 0)
    except ZeroDivisionError:
        return "Erro: número de parcelas inválido."
    except KeyError as erro:
        return f"Erro: campo obrigatório ausente ({erro})."
    except Exception:
        return "Erro inesperado. Contate o suporte técnico."
    return f"Pagamento processado: R$ {resultado:.2f} por parcela."


print(processar_pagamento({"numero": "1234", "parcelas": 2}))
print(processar_pagamento({"numero": "1234", "parcelas": 0}))
print(processar_pagamento({"numero": "1234"}))
