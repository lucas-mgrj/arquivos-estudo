def fibonnaci(quantidade):
    resultado = [0, 1]

    for _ in range(2, quantidade):
        # resultado.append(resultado[-2] + resultado[-1])
        resultado.append(sum(resultado[-2:]))
    return resultado


if __name__ == '__main__':
    for fib in fibonnaci(22):
        print(f'fib: {fib},')

