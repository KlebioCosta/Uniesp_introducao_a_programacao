#verificar o valor mostrado que quando divididos por 11, produzam resto igual a 5.
for num in range(1000, 2000):

    if (num % 11) == 5:
        print(num)