#
#
#
try:
    arquivo = open('pessoas.csv')
    for registro in arquivo:
        print('Nome: {}, idade: {}'.format(*registro.strip().split(',')))
except IndexError:
    pass
finally:
    print('Arquivo fechado.')
    arquivo.close()
