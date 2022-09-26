nascimento = int(input("Digite seu ano de nascimento:"))
ano_atual = 2022
idade = ano_atual - nascimento

if idade < 16:
    print(f"Idade atual {idade}, Você não pode votar esse ano!")
if idade >= 16:
    print(f"Idade atual {idade}, você pode votar esse ano!")