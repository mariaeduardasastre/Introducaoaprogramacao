import os
print("------Operações Matemáticas------")
print("Escolha uma das opções abaixo. Para encerrar, digite <SAIR>")
print("1- soma")
print("2- subtração")
print("3- multiplicação")
print("4- divisão")
print("5- Par ou impar")
print("6- Primo")
print("7- fatorial")
opcao=input("Digite a opção desejada ou <SAIR> para encerrar:")
opcaoMaiusc=opcao.upper()
while opcaoMaiusc !="Sair": 
    if opcao=="1": 
        n1=float(input("Digite o primeiro número: "))
        n2=float(input("Digite o segundo número:"))
        soma=n1+n2
        print("A soma entre" , n1 , "e" , n2 , "e igual a: " , soma)
    if opcao=="2":
        n1=float(input("Digite o primeiro número: "))
        n2=float(input("Digite o segundo número: "))
        subtracao=n1-n2
        print("A subtração entre" , n1, "e" , n2 , "é: " , subtracao)
    if opcao=="3": 
        n1=int(input("Digite o primeiro número: "))
        n1=int(input("Digite o segundo número: "))
        print("O resultado do produto entre " , n1 , "e" , n2 , "é: " , n1*n2)
    if opcao=="4": 
        n1=int(input("Digite o primeiro número:"))
        n2=int(input("Digite o segundo número: "))
        print("O resultado da divisão entre" , n1 , "e" , n2 , "é: " , n1/n2)
    if opcao =="5":
        n1=int(input("Digite um número: "))
        if n1%2==0:
            print("O número" , n1, "é par.")
        else:
            print("O número" , n1 , "é impar.")
    input("Pressione ENTER tecla para voltar ao menu")
    os.system("c1s")
    print("------Operações Matemáticas------")
    print("Escolha uma das opções abaixo. Para encerrar, digite <SAIR>")
    print("1- soma")
    print("2- subtração")
    print("3- multiplicação")
    print("4- divisão")
    print("5- Par ou impar")
    print("6- Primo")
    print("7- fatorial")
    opcao=input("Digite a opção desejada ou <SAIR> para encerrar:")