def gerar():
    generator = (i ** 2 for i in range(int(101)) if i % 2 == 0)
    while True:
        print(next(generator))
gerar()

