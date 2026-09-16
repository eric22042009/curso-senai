
fila = ["Ana", "Carlos", "Beatriz", "Daniel"]

fila.append("Eduardo")
print(f"Fila após chegada de Eduardo: {fila}")

atendido = fila.pop(0)
print(f"Atendendo o aluno: {atendido}")

fila.remove("Beatriz")

print(f"\nEstado final da fila de espera: {fila}")