valor = int(input("Digite o valor que deseja sacar: R$ "))

if valor <= 0 or valor % 10 != 0:
    print("Valor inválido! O valor deve ser positivo e múltiplo de 10.")
else:
    valor_restante = valor

    notas100 = valor_restante // 100
    valor_restante %= 100

    notas50 = valor_restante // 50
    valor_restante %= 50

    notas20 = valor_restante // 20
    valor_restante %= 20

    notas10 = valor_restante // 10


    print(f"\nPara o saque de valor: {valor}, serão entregues:")
    if notas100 > 0:
        print(f"- {notas100} notas de 100")
    if notas50 > 0:
        print(f"- {notas50} notas de 50")
    if notas20 > 0:
        print(f"- {notas20} notas de 20")
    if notas10 > 0:
        print(f"- {notas10} notas de 10")
