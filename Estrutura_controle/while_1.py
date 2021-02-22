from random import randint


numero_informado = -1
numero_random = randint(0, 9)

while numero_random != numero_informado:
    numero_informado = int(input('Informe um numero'))

print('Numero secreto {} foi encontrado!'.format(numero_random))