# Serialização de tipos não nativos
# Manual do Desenvolvedor Python - Capitulo 13

import json
from datetime import datetime

def serializar_data(obj):
    if isinstance(obj, datetime):
        return obj.strftime("%Y-%m-%d %H:%M:%S")
    raise TypeError(f"Tipo não serializável: {type(obj)}")

dados = {"nome": "Andy Angel", "cadastrado_em": datetime(2026, 1, 15, 10, 30)}
texto = json.dumps(dados, default=serializar_data, ensure_ascii=False)
print(texto)
