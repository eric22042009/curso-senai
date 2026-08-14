n1 = float(input("Digite sua media 1:"))
n2 = float(input("Digite sua media 2:"))
n3 = float(input("Digite sua media 3:"))

media = (n1 + n2 + n3) / 3

print(media)

if media >= 7:
    print("Aprovado")
elif media >= 5:
    print("Recuperaçao")
else:
    print("Reprovado"