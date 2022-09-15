#cauculo de quantidade de produtos em estoque!!
atual_em_estoque = int(input("Quantidade atual em estoque: "))
quantidade_max = int(input("Quantidade Máxima em Estoque: "))
quantidade_min = int(input("Quantidade Mínima em Estoque: "))
quantidade_media = (quantidade_max + quantidade_min)/ 2

if atual_em_estoque >= quantidade_media:
    print("Não efetuar a compra")
else:
    print("Efetuar Compra")