# Construa uma matriz A de tamanho 10 x 10 com valores inteiros e randômicos.
# Depois:Imprima o resultado da soma de todos os valores da matriz no terminal;E,
# criei uma nova matriz B, no qual cada item seja o valor da matriz A * 3;

from random import randint


A = []
B = []

for l in range(10):
    linha = []

    for c in range(10):
        linha.append(randint(0, 15))

    A.append(linha)

for linha_matriz in A:
    print(linha_matriz)

for linha in A:
    soma = sum(linha)
    print(soma)
    B.append(soma * 3)

print(B)