controle = True
while controle:
    print("Digite 0 para sair")
    print("Digit outro numero escolhido")
    num = input("Digite o número: ")

    if num == 0:
        controle = False
    elif num > 10:
        print(f"{num} é maior que 10")
    elif num < 10 and num != 0:
        print (f"{num} é menor que 10")