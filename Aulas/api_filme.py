import requests
import json

def requisicao(titulo):
    req = None

    try:
        #req = requests.get('https://www.omdbapi.com/?apikey=4b421c06&t=venom&r')
        req = requests.get('https://www.omdbapi.com/?apikey=4b421c06&t='+titulo)
        dicionario = json.loads(req.text)
        #print(dicionario)
        if dicionario['Response'] == 'True':
            print('Title:', dicionario['Title'])
            print('Year:', dicionario['Year'])
            print('Genre:', dicionario['Genre'])
        else:
            print('Filme não encontrado')
        return dicionario
    except:
        print('erro de conexão')
        exit()
        return None
#print('informações do Filme')
#print(req.text)

def main():
    filme = None
    sair = False
    while not sair:

        filme = input('Digite o nome do Filme')
        if filme != 'sair':
            requisicao(filme)
        else:
            sair = True
            print('Fim do programa')

main()