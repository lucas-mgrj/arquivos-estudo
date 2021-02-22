import csv
from urllib import request


# with open('desafio-ibge.csv') as entrada:
#     for campos in csv.reader(entrada):
#         Lista_Campos = '{9},{4},{1},{2},{3},{5},{6},{7},{8}'.format(*campos)
#         print(Lista_Campos[0].strip().split(), Lista_Campos[1].strip().split())
#
#
#
#
def read(url):
    with request.urlopen(url) as entrada:
        print('Baixando csv...')
        dados = entrada.read().decode('latin1')
        print('Download completo.')
        for cidade in csv.reader(dados.splitlines()):
            print(f'{cidade[8]}: {cidade[3]}')


if __name__ == '__main__':
    read(r'http://files.cod3r.com.br/curso-python/desafio-ibge.csv')
