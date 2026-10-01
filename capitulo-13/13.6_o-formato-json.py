# O formato JSON
# Manual do Desenvolvedor Python - Capitulo 13

import json

dados = {"nome": "Andy Angel", "idade": 25, "vip": True}
texto_json = json.dumps(dados, ensure_ascii=False)
print(texto_json)
print(type(texto_json))

dados_de_volta = json.loads(texto_json)
print(dados_de_volta)
print(type(dados_de_volta))
