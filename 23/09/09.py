
def exercicio_09():
    numero = int(input("Digite um número inteiro: "))
 
    with open("tabuada.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write(f"Tabuada do {numero}:\n")
        for i in range(1, 11):
            arquivo.write(f"{numero} x {i} = {numero * i}\n")
 
    print("Tabuada salva no arquivo tabuada.txt!")