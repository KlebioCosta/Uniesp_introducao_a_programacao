numero_conta = int(input("Digite o numero da conta: "))

saldo_atual = int(input("Digite seu saldo: "))
debito= int(input("Digite sua divida: "))
credito = int(input("Digite seu credito : ")) 


valorFinal = saldo_atual - debito + credito

if valorFinal >= 0:
    print(f"Conta número: {numero_conta} possui R$:{valorFinal:,.2f}\n     ...Saldo Positivo... ")
if valorFinal < 0:
    print(f"Conta número: {numero_conta} possui R$:{valorFinal:,.2f}\n     ...Saldo Negativo... ")
