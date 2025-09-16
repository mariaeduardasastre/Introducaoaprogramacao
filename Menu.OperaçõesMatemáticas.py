while True:
    print("-- MENU DE INTERAÇÕES --")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Par ou Ímpar")
    print("6 - Número Primo")
    print("7 - Fatorial")
    print("Digite 'Sair' para encerrar.")
opcao=input("Selecione uma opção de equação:")
if opção == "Sair":
    print("Encerrando programa...")
if opcao == 1:
 n1 =int(input("Digite um número: "))
 n2 =int(input("Digite outro número: "))
 print("Resultado da soma: " , n1 + n2 )
if opcao == 2:
   n1= int(Input("Digite um número: "))
   n2 = int(input("Digite outro número: "))
   print("A subttração dos números é: " , n1 - n2)
if opcao == 4:
   n1 = int(input("Digite um número: "))
   n2 = int(input("Digite outro número: "))
print("O produto entre os números é: " , n1*n2)
if opcao == 5:
   num=int(input("Digite o número"))
   if num // 2 == 0:
      print("O número" , num , "é par.")
   else: print("O número é impar.")
   