#dentre os valores digitados apresentar o maior valor
valor1 = int(input("Digite o primeiro valor: "))
valor2 = int(input("Digite o segunddo valor: "))
#o calculo será resolvido apenas com numeros inteiros
if valor1 > valor2:
    print(f"Maior valor, {valor1}")
if valor1 < valor2:
    print(f"Maior valor, {valor2}")
elif valor1 == valor2:
    print("Por favor digitar valores diferentes")
    