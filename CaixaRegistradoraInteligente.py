total = 0
quantidade = 0
mais_caro = 0

continuar = "s"

while continuar == "s":
    preco = -1

    
    while preco < 0:
        preco = float(input("Digite o preço do produto: "))
        if preco < 0:
            print("Preço inválido! Digite novamente.")

    
    total += preco
    quantidade += 1

    if preco > mais_caro:
        mais_caro = preco


    resposta = ""
    while resposta != "s" and resposta != "n":
        resposta = input("Deseja adicionar outro produto? (s/n): ").lower()
        if resposta != "s" and resposta != "n":
            print("Resposta inválida!")

    continuar = resposta

media = total / quantidade

print("------ RESULTADO ------")
print("Quantidade de produtos:", quantidade)
print("Total da compra: R$", total)
print("Valor médio: R$", media)
print("Produto mais caro: R$", mais_caro)
