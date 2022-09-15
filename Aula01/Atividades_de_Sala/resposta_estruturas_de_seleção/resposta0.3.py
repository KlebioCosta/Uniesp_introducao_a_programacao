#calcular o valor da fruta e dar desconto acima de 12 unidades
volume = int(input("quantidade de maçã: " ))
# o valor cauculado será feito a partir de 12 unidades e não a cada 12 unidades!!
if volume <= 11:
   print(f"Total de {volume} maçã\nValor final R$: {volume * 1.30:.2f} ")
    
if volume > 11:
   print(f"Total de {volume} maçã\nValor final R$: {volume * 1.00:.2f} ")