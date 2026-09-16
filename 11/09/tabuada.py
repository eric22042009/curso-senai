while True:
    numero = int(input("Digite um número: "))

    for i in range(1, 11):
        print(numero, "x", i, "=", numero * i)

    resposta = input("Quer outra tabuada? (sim/nao): ")

    if resposta == "nao":
        break
