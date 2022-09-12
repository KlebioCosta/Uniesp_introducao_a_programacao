#ordenar os valores digitados  em forma crescente
valor1 = int(input("Digite um valor: "))
valor2 = int(input("Digite outro valor: "))
valor3 = int(input("Digite o ultimo valor: "))

if valor1 < valor2 < valor3:
    print(f"Ordem crescente: {valor1}, {valor2}, {valor3}")
    
if valor1 < valor2 > valor3:
    print(f"Ordem crescente: {valor1}, {valor3}, {valor2}")
    
if valor2 < valor1 < valor3:
    print(f"Ordem crescente: {valor2}, {valor1}, {valor3}")

if valor2 < valor3 < valor1:
    print(f"Ordem crescente: {valor2}, {valor3}, {valor1}")
    
if valor3 < valor1 < valor2:
    print(f"Ordem crescente: {valor3}, {valor1}, {valor2}")

if valor3 < valor2 < valor1:
    print(f"Ordem crescente: {valor3}, {valor2}, {valor1}")

elif valor1 == valor2 or valor3:
    print(f"Valores iguais não será valido ")


    #COM ESSE METODO EU NAO CONSEGUI FAZER ACUSAR QUANDO FOREM NÚMEROS IGUAIS!!!
#from timeit import repeat

#list = []
#i = 0
#while i < 5:
#
#    valor = int(input("digite um numero: "))
#    list.append(valor)
#    i += 1
#    
#list.sort()
#print(list)