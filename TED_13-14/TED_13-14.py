'''
    Turma: P1B 
    Aluno(s): Analicia Fernandes Aquino
          Douglas Manuel Guedes
          Luiz Carlos Lima
          Edinailton Klébio Costa
    
    - Selecione a Longitude e Latitude das capitais de Portugal, Espanha, Itália, França e Inglaterra;
    - Crie um arquivo TXT organizando as informações: País, Capital, Logintude, Latitude (modelo abaixo);
    - Seu programa deve utilizar o arquivo como fonte de dados para consumir uma API;
    - Utilize uma estrutura de repetição para chamar a API até o final dos dados;
    - Imprima o resultado em arquivos JSON separados, e cada um deve conter o nome do país específico;
'''
from json import dumps
from requests import get



API_KEY = input("Digite sua chave API: ")
nome_arquivo = input("Digite o arquivo com os dados para consuta: ")

pontos = []
with open(nome_arquivo , 'r', encoding='UTF-8') as arquivo:
    for linha in arquivo.readlines():
        linha = linha.replace('\n','').replace(' ','')
        novo_formato = linha.split(',')
        pontos.append(novo_formato)

for info in pontos:
    url = f'https://api.openweathermap.org/data/2.5/weather?lat={info[3]}&lon={info[2]}&appid={API_KEY}'   
    resposta = get(url)

    if resposta.status_code == 200:
        print(f'Criando arquivo: {info[0]}.json')
        with open(info[0] + '.json', 'w', encoding='UTF-8') as arquivo:
            pontos_json = dumps({info[1]:resposta.json()}, indent=4)
            arquivo.write(pontos_json)
    else:
        print(f'Ocorreu um erro ao consultar as informações para: {info}')
