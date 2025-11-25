senha=1234
digite=int(input("Digite a senha: "))
while digite != senha:
    print("Senha incorrwta, tente novamente.")
    digite=int(input("Digite a senha:"))
print("Senha correta, acesso liberado.")