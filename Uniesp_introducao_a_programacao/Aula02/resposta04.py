valor = int(input('Entre com um número para saber a tabuada: '))  
i = 0  
print('*' * 18)  
print(f"Tabuada de {valor}")  
print('*' * 18)  
while(i <= 10):  
  print(f"{valor} X {i} = {i*valor}")  
  i+= 1 