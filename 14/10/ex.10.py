import json

supermecado = {}

while True:
    item = input("item (ou 'fim'): ")
    if item == "fim":
        break

    quantidade = int(input("quantidade: "))
    supermecado[item] = quantidade

with open("lista_de_compras.json", "w", encoding="utf-8") as arquivo:
    json.dump(supermecado, arquivo, indent=4, ensure_ascii=False)

print("lista salva")