import json

produtos = [
    {"nome": "notebook", "categoria": "eletronico", "preco": 2000},
    {"nome": "vestido", "categoria": "roupa", "preco": 100},
    {"nome": "fone de ouvido", "categoria": "eletronico", "preco": 50},
    {"nome": "cafe", "categoria": "comida", "preco": 10},
    {"nome": "celular", "categoria": "eletronico", "preco": 1000}
]

arquivo = open("produtos.json", "w")
json.dump(produtos, arquivo)
arquivo.close()

arquivo = open("produtos.json", "r")
dados = json.load(arquivo)
arquivo.close()

for p in dados:
    if p["categoria"] == "eletronico" and p["preco"] > 100:
        print(p["nome"], p["preco"])