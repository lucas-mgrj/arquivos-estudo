arquivo = open('pessoas.csv')
dados = arquivo.read()
arquivo.close()
for registro in dados.splitlines():
    print('Nome: {}, idade: {}'.format(*registro.split(',')))
