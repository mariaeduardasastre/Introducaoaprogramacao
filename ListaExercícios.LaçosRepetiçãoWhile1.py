soma_positivos = 0
qtd_negativos = 0
i = 0
while 1 < 20:
    numero=int(input("Digite um número"))
    if numero > 0:
        soma_positivos += numero
    elif numero < 0:
        qtd_negativos += 1
     i += 1
print("Soma dos positivos:" , soma_positivos)
print("Quantidade de negativos:" , qtd_negativos)