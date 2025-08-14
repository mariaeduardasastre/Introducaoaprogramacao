media_final= 6.0
nota1= float(input("nota primeiro bimestre"))
nota2= float(input("nota segundo bimestre"))
soma_atual= nota1 + nota2
total_necessário= media_final *4
faltam= total_necessário - soma_atual
if faltam <= 0:
    print("você ja possui média o suficiente para passar!")
else:
    nota_por_bimestre= faltam / 2
    print("Você precisa de um total de", faltam , "para passar")
    print("Ou seja, precisa pelo menos" , nota_por_bimestre, "em cada bimestre")