qtd_jogadora = int(input("Digite o número de jogadores: "))
soma_altura=0
for i in range(qtd_jogadora):
    altura = float(input("Digite a altura do jogador", {i+1}, ":" ))
    soma_altura += altura
    media= soma_altura/qtd_jogadora