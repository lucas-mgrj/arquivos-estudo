PALAVRAS_PROIBIDAS = {'futebol', 'religião', 'política'}
textos = [
    'João gosta de futebol e política!',
    'A praia foi divertida!'
]
for texto in textos:
    intersecao = PALAVRAS_PROIBIDAS.intersection(set(texto.lower().split()))
    if intersecao:
        print(f'O texto possui pelo meno suma palavra proibida, que é: {intersecao}.')
    else:
        print(f'Texto autorizado é: "{texto}"')