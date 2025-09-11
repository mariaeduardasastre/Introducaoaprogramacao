maior_media= 0
menor_media=0
aprovados=0
reprovados=0
i = 0
while i < 10:
    print("Aluno" , {i+1})
    n1=float(input("Digite a primeira nota: "))
    n2=float(input("Digite a segunda nota: "))
    n3=float(input("Digite a terceira nota: "))
    media= (n1 + n2 + n3) / 3
    print("Média: " , media)
    if media > maior_media:
     maior_media=media
    if media < menor_media:
       menor_media=media
    if media >= 6:
       aprovados += 1
    else:
       reprovados += 1
    i += 1
print("Maior Média: " , maior_media)
print("Menor Média: " , menor_media)
print("Aprovados: " , aprovados)
print("Reprovados: " , reprovados)