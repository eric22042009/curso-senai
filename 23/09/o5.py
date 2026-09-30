notas = [7.5, 8.0, 6.0, 9.5]
media = sum(notas) / len(notas)
 
with open("boletim.txt", "w", encoding="utf-8") as arquivo:
        
    arquivo.write(",".join(str(nota) for nota in notas) + "\n")
    arquivo.write(f"Média Final: {media:.2f}\n")
 
    print("Boletim salvo em boletim.txt!")
 