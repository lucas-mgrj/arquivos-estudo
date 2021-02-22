def verificar_conceito():
    print('Digite "sim" para sair. ')

    nota = input("Insira a nota: ")
    aviso_sair = 'sim'

    list_notes = ['A', 'A-', 'B', 'B-', 'C', 'C-', 'D', 'D-', 'E', 'E-']

    def print_Conceit(nota):
        print('Sua nota é: ', nota)

    if not nota.isnumeric():
        return 'Digite apenas numeros.'
        verificar_conceito()

    elif aviso_sair.lower() == nota == aviso_sair.upper():
        return exit()

    elif nota == '' or float(nota) > 10:
        return 'Nota Inválida.'
        verificar_conceito()

    elif 0 <= float(nota) <= 1:
        print_Conceit(nota + '. Com o conceito: ' + list_notes[9])
        verificar_conceito()

    elif 2 >= float(nota) >= 1.1:
        print_Conceit(nota + '. Com o conceito: ' + list_notes[8])
        verificar_conceito()

    elif 3 >= float(nota) >= 2.1:
        print_Conceit(nota + '. Com o conceito: ' + list_notes[7])
        verificar_conceito()

    elif 4 >= float(nota) >= 3.1:
        print_Conceit(nota + '. Com o conceito: ' + list_notes[6])
        verificar_conceito()

    elif 5 >= float(nota) >= 4.1:
        print_Conceit(nota + '. Com o conceito: ' + list_notes[5])
        verificar_conceito()

    elif 6 >= float(nota) >= 5.1:
        print_Conceit(nota + '. Com o conceito: ' + list_notes[4])
        verificar_conceito()

    elif 7 >= float(nota) >= 6.1:
        print_Conceit(nota + '. Com o conceito: ' + list_notes[3])
        verificar_conceito()

    elif 8 >= float(nota) >= 7.1:
        print_Conceit(nota + '. Com o conceito: ' + list_notes[2])
        verificar_conceito()

    elif 9 >= float(nota) >= 8.1:
        print_Conceit(nota + '. Com o conceito: ' + list_notes[1])
        verificar_conceito()

    elif 10 >= float(nota) >= 9.1:
        print_Conceit(nota + '. Com o conceito: ' + list_notes[0])
        verificar_conceito()


verificar_conceito()
