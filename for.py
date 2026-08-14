maior = 0
menor = 0

for i in range(10):
  # Note os dois pontos (:) no final da linha do for acima
  numero = float(input(f"Digite o numero {i + 1}: "))

  if i == 0:
    maior = numero
    menor = numero
  else:
    if numero > maior:
      maior = numero
    if numero < menor:
      menor = numero

print("\n--- Resultados ---")
print(f"O maior valor digitado foi: {maior}")
print(f"O menor valor digitado foi: {menor}")