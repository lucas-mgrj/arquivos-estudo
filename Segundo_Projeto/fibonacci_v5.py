def fibonnaci(limite):
    resultado = [0, 1]

    while resultado[-1] < limite:
        # resultado.append(resultado[-2] + resultado[-1])
        resultado.append(sum(resultado[-2:]))
    return resultado


if __name__ == '__main__':
    for fib in fibonnaci(10000):
        print(fib)

