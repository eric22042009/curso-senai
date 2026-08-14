secreto = 7
tentativas = 0

while True:
    n = int(input("Digite um número: "))
    tentativas += 1

    if n == secreto:
        break

print("Acertou!")
print("Tentativas:",)