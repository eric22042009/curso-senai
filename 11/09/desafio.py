
numero_secreto = 42 
palpite = -1
tentativas = 0

while palpite != numero_secreto:
    palpite = int(input("Tente adivinhar o número: "))
    tentativas += 1

    if palpite == numero_secreto:
        print(f"Parabéns! Você acertou em {tentativas} tentativa(s).")
    elif palpite > numero_secreto:
        print("O número secreto é menor.")
    else:
        print("O número secreto é maior.")

