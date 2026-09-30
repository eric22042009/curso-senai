numeros = [12, 7, 33, 48, 5, 90, 21, 64, 15, 100]
pares = [n for n in numeros if n % 2 == 0]
 
with open("numeros_pares.txt", "w", encoding="utf-8") as arquivo:
    for n in pares:
        arquivo.write(f"{n}\n")
 
print(f"{len(pares)} números pares foram salvos no arquivo.")
 

