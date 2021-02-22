with open('pessoas.csv') as entry:
    print('Writing...')
    print('')
    with open('pessoas.txt', 'w') as exit:
        for register in entry:
            pessoa = register.strip().split(',')
            print('Name: {} | Age: {}'.format(*pessoa), file=exit)
        print('Name/Age has been registered.')
# if entry.close():
#     print('Exit was closed.')
# if exit.close():
#     print('Exit was closed.')
