#Questão 01
clubs = []

for time in range(10):
    clubs.append(input("Digite os Clubs: "))

print("Digite o nome de seu clube para conferir se está na lista !! ")
print("*#"*23)

x = input("Verificar Time digite aqui: ")
if x in clubs:
    print(f"Achei !!! O Club, {x} foi selecionado. ")
else:
    print(f"NÂO Achei :( O Time, {x}, não foi selecionado. ")


"""--------------------------------------------------------------------"""

#Questão 02

import random
list=[]

for x in range(30):
    x = random.randint(1, 15)
    list.append(x)

meu_numero = int(input("Digite um número de de 1 à 15: "))
contador = 0
for x in list:
    if x == meu_numero:
        contador += 1
print(f"Eu escolhi o número: {meu_numero}. ")
print(f"Meu número repetiu, {contador} vezes. ")
print(f"Os números sorteados são: {list}.")