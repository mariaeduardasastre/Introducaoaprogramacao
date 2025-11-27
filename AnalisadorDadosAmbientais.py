N = int(input("Quantas leituras de temperatura serão analisadas? "))
maior = 0
menor = 0
soma = 0
acima30 = 0
abaixo15 = 0
for i in range(N):
    temp = float(input("Digite a temperatura " + str(i+1) + ": "))
    if i == 0:
        maior = temp
        menor = temp
    else:
        if temp > maior:
            maior = temp
        if temp < menor:
            menor = temp
    soma += temp
    if temp > 30:
        acima30 += 1
    if temp < 15:
        abaixo15 += 1
media = soma / N
print("Maior temperatura:", maior)
print("Menor temperatura:", menor)
print("Média das temperaturas:", round(media, 2))
print("Acima de 30°C:", acima30)
print("Abaixo de 15°C:", abaixo15)
diferenca = maior - menor
if diferenca > 20:
    print("ALERTA: Variação térmica extrema!")
else:
    print("Variação dentro do esperado.")
