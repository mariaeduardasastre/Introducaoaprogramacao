somaValor=0
qtdNegativo=0
for i in range(20):
 valor=int(input("Digite o valor: "))
 if valor>=0:
    SomaValor+=valor
 else:
   qtdNegativo+=1
print("A soma dos valores positivos é: ", somaValor)
print("A quantidade de valores negativos é: ", qtdNegativo)