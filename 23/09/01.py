nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")
 
with open("usuario.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write(f"Nome: {nome}\n")
    arquivo.write(f"Idade: {idade}\n")
 
    print("Dados salvos com sucesso!")

