soma_positivos=0
quantidade_negativos=0
i=0
while i<20:
  numero=int(input("Digite o número: "))
  if numero>0:
    soma_positivos += numero
  if numero > 0:
    quantidade_negativos += numero
i += 1
print("soma dos positivos: ", soma_positivos)
print("Quantidade de números negativos", quantidade_negativos)