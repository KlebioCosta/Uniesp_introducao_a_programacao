'''Dupla:
    Edinaliton Klébio da Costa Ferreira
    Luiz Carlos da Sila Lima'''

# Atividade Avaliativa - Questão 1
import math

a = float(input("Digite o valor A: "))
b = float(input("Digite o valor B: "))
c = float(input("Digite o valor C: "))

delta = math.pow(b, 2) - 4 * a * c
if delta > 0:
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)

    print(f"X1 -> {x1:.2f}")
    print(f"X2 -> {x2:.2f}")
    print(f"Delta -> {delta}")
else:
    print("Reduza os valores de A e C!")
    
    
    
#Atividade Avaliativa Questão - 2
import math
x1 = float(input("Entre com um número:\n"))
x2 = float(input("Entre com um número:\n"))
y1 = float(input("Entre com um número:\n"))
y2 = float(input("Entre com um número:\n"))
raiz = math.sqrt(((x2-x1)**2+(y2-y1)**2))

print(f"Sua distância entre os pontos sao: {raiz:.2f}")


#Atividade Avaliativa Questão - 3
while True:
    print("\n*** ESCOLHA A OPÇÃO DESEJADA ***\n")
    
    opcao = int(input("1 Para Adição \n2 Para Subtração \n3 Para Multiplicação\n4 Para Divisão \n5 Para Potenciação \n0 Para parar a execução\n "))
    if 1<= opcao <=5:
        n1 = int(input("digite seu primerio valor: "))
        n2 = int(input("digite seu segundo valor: "))
    
    if opcao == 1:
        soma = n1 + n2
        print(f"SOMA de {n1} + {n2} : {soma} \n")
        
    elif opcao == 2:

        soma = n1 - n2
        print(f"SUBTRAÇÂO de {n1} + {n2} : {soma} \n")
    elif opcao == 3:

        soma = n1 * n2
        print(f"MULTIPLICAÇÂO de {n1} + {n2}: {soma} ")
    elif opcao == 4:

        soma = n1 / n2
        print(f"DIVISÂO de {n1} + {n2} : {soma} ")
    elif opcao == 5:

        soma =n1**n2
        print(f"POTENCIAÇÂO de {n1} + {n2} : {soma} ")
    elif opcao ==0:
        break
    else:
        print("Nenhuma das opções escolhidas\n")


#Atividade Avaliativa Questão - 4
peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))
IMC = peso/(altura**2)
print(IMC)
if IMC <= 18.4:
    print(f"Seu IMC: {IMC:.2f}, Você está abaixo do peso.")
elif 18.4 < IMC <= 25:
    print(f"Seu IMC: {IMC:.2f}, Você está no peso ideal. ")
elif 25 < IMC <= 30:
    print(f"Seu IMC: {IMC:.2f}, Você está acima do peso. ")
else:
    print(f"Seu IMC: {IMC:.2f}, Você está obeso ")
    
    

#Atividade Avaliativa Questão - 5
print("DIGITE SEUS VALORES NO CAMPO ABAIXO \n")
a=0; b=0; c=0; d=0
while True:
    v = int(input("Digite seus valores: "))
    if 0<=v<=25:
        a+=1
    elif 26<=v<=50:
        b+=1
    elif 51<=v<=75:
        c+=1
    elif 76<=v<=100:
        d+=1
    elif v>100:
        print("Valor maximo 100")
    elif v<0:
        break
print(f"entre os valores 0 e 25 foram digitados: {a}\nentre os valores 26 e 50 foram digitados: {b}\nentre os valores 51 e 75 foram digitados: {c}\nentre os valores 76 e 100 foram digitados: {d}")


##Atividade Avaliativa Questão - 6
A = int(input("Digite o valor de 'A': " ))

i = A-1
total = 0
pos = 0
lista = []
lista.append(A)
resultado = f"{A}!="
while i<A and i>=1:
    if pos == 0:
        total = A*i
        lista.append(i)
        i-=1
        pos+=1
    else:
        total = total * i
        lista.append(i)
        i-=1
for x in lista:
    if x == lista[-1]:
        resultado+= f"{x}"
    else:
        resultado+= f"{x}x"
               
resultado+= f"={total}"
print("Resultado: ", resultado)