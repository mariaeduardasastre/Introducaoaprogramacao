qtd = int(input("Digite a quantidade de jogadores:"))
soma=0
i=0
while i < qtd:
    altura=float(input("Digite a altura do jogador"))
    soma+=altura
    i += 1

media= soma / qtd
print("A média da altura dos jogadores é: " , media)
