# for i in range(1,11):
#     if i == 6:
#         break
#     print(i)
# else:
#     print('Fim!')
from random import randint

def sortear_dado():
    numero_random = randint(0, 6)
    print(f'numero sorteado: {numero_random}.')

    for numero_1_6 in range(1, 7):
        if numero_1_6 % 2 == 1:
            continue

        elif numero_random == numero_1_6:
            print(f'Acertou!, o numero é: {numero_1_6}')
            break
    else:
        print('Errou!')

sortear_dado()
