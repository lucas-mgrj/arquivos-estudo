#
#
#
arquivo = open('pessoas.csv')
for registro in arquivo:
    print('Nome: {}, idade: {}'.format(*registro.split(',')))
arquivo.close()