PALAVRAS_PROIBIDAS = ('futebol', 'religião', 'política')
textos = [
    'João gosta de futebol e política!',
    'A praia foi divertida!'
]

for texto in textos:
    found = False
    for palavra in texto.lower().split():
        if palavra in PALAVRAS_PROIBIDAS:
            print(f'O texto possui pelo meno suma palavra proibida, que é: {palavra}.')
            found = True
            break

    if not found:
        print(f'Texto autorizado é: "{texto}"')