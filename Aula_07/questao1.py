volume = int(input("Quantidade de maçã: "))
if volume <= 11:
    print(f"Total de {volume} maçã Valor final R$: {volume * 1.30:.2f}")
if volume > 11:
    print(f"total de {volume} maçã Valor final R$: {volume * 1.00:.2f}")
