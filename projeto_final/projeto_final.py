'''
PROJETO FINAL
Prof: Messias
Equipe: Analicia Aquino
        Douglas
        Luiz Lima
        Rafael Dias
        Silvano
        Edinailton Klébio
'''
from requests import get
from json import dumps


API_KEY = 'ebcb4ab68389bee0a8fec08d27bdd353'
dados = []

while True:
    menu = input('\nEscolha uma opção:\n\
\n1 - Adicionar uma nova cidade\n\
2 - Ver as cidades já registradas\n\
3 - Gerar dados das cidades\n\
0 - Para sair\n\
\nDigite a opção desejada: ')

    if menu == "1":
        try:
            cidade = str(input('\nDigite o nome da cidade: '))
            latitude = float(input('Digite a latitude da cidade: '))
            longitude = float(input('Digite a longitude da cidade: '))
            lista_cid = [cidade,latitude,longitude]
            dados.append(lista_cid)
        except TypeError:
            print('O tipo de dado digitado não confere ')
        except Exception as erro:
            print(f'Erro encontrado, {erro.__class__}')
        

        try:
            with open('dados.txt','w') as arquivo:
                for cidade in dados:
                    arquivo.write(str(cidade)+'\n')
        except:
            print('Ocorreu um erro. ')
    
    elif menu == "2":
        try:
            with open('dados.txt','r') as arquivo:
                for dado in dados:
                    print(dado)
        except Exception as error:
            print(f'Foi encontrado um erro {error.__class__}')
    
    elif menu == "3":
        for infor in dados:
        
            url = f'https://api.openweathermap.org/data/2.5/weather?lat={infor[1]}&lon={infor[2]}&appid={API_KEY}'
            resposta = get(url)
    
            if resposta.status_code == 200:
                print(f'Criando arquivo: {infor[0]}.json')
                with open(infor[0] + '.json', 'w', encoding='UTF-8') as arquivo:
                    dados_json = dumps({infor[0]:resposta.json()}, indent=4)
                    arquivo.write(dados_json)
            else:
                print(f'Ocorreu um erro ao consultar as informações para: {infor}')
                               
    elif menu == "0":
        break
    
    else:
        print('Opção inválida.')