def soma(a, b):
    return a + b


def soma_2(a, b, c):
    return a + b + c


def soma_n(*numeros):
    print(type(numeros))
    soma = 0
    for n in numeros:
        soma += n
    return soma


if __name__ == '__main__':
    print(soma(2, 3))
    print(soma_2(2, 3, 4))
    # packing
    print(soma_n(1, 2, 3, 4, 5, 6, 7, 8))

    # unpacking
    tupla = (1, 2, 3)
    lista = [1, 2, 3]
    print(f'{soma_2(*tupla)} tupla')
    print(f'{soma_2(*lista)} lista')
