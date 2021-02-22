palavra = 'paralelepipedo'
for letra in palavra:
    print(letra, end = ',')
print(' Fim!')

aprovados = ['Anna','Carlos', 'Maria', 'Cleber']
for posicao, nome in enumerate(aprovados):
    print(f'{posicao + 1})', nome, end='\n')

dias_semana = ('Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sabado')
for dia in dias_semana:
    print(f'Hoje o dia da semana é:{dia}.',)

for numero in {1, 2, 3 , 4, 5, 6}:
    print(f'O numero é: {numero}.d')