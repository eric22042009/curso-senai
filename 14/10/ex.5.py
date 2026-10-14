import json

try:
    with open("clientes.json", "r", encoding="utf-8") as arquivo:
        clientes = json.load(arquivo)
except (FileNotFoundError, json.JSONDecodeError):
    clientes = []

nome = input("Nome: ")
email = input("E-mail: ")
idade = int(input("Idade: "))


novo_cliente = {"nome": nome, "email": email, "idade": idade}
clientes.append(novo_cliente)


with open("clientes.json", "w", encoding="utf-8") as arquivo:
    json.dump(clientes, arquivo, indent=4, ensure_ascii=False)

print("Cliente cadastrado com sucesso!")

