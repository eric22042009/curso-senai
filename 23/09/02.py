mensagem = input("Digite a mensagem do dia: ")
 
with open("diario.txt", "a", encoding="utf-8") as arquivo:
    arquivo.write(mensagem + "\n")
 
print("Anotação adicionada ao diário!")