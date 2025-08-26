maior_media=0
menor_media=10
alunos_aprovados=0
alunos_reprovados=0
for i in range(1,11):
 print("f/nAlunos", {i})
n1= float(input("Digite a primeira nota:"))
n2 = float(input("Digite a segunda nota:"))
n3 = float(input("Digite a terceira nota:"))
media = (n1+n2+n3)/3
print("Média do aluno" , media)
if media > maior_media:
 maior_meida=media
if media < menor_media:
 menor_media=media
if media >= 6:
 alunos_aprovados += 1
else:
 alunos_reprovados +=1