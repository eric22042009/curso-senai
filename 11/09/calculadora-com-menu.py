opcao = ""

while opcao != "5":
    print("\nMenu:")
    print("1 - Somar")
    print("2 - Subtrair")
    print("3 - Multiplicar")
    print("4 - Dividir")
    print("5 - Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "5":
        print("Encerrando a calculadora.")
    elif opcao in ("1", "2", "3", "4"):
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        if opcao == "1":
            print(f"Resultado: {num1 + num2}")
        elif opcao == "2":
            print(f"Resultado: {num1 - num2}")
        elif opcao == "3":
            print(f"Resultado: {num1 * num2}")
        elif opcao == "4":
            if num2 == 0:
                print("Erro: divisão por zero não é permitida.")
            else:
                print(f"Resultado: {num1 / num2}")
    else:
        print("Opção inválida! Tente novamente.")