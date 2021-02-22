# import csv
#
# with open('Pag1.csv') as entrada:
#     for item in csv.reader(entrada):
#
#         print('Item: {}, Preço: {}'.format(*item))
#
#
# with open('Pag2.csv') as entrada2:
#     for item2 in csv.reader(entrada2):
#         print('Item: {}, Preço: {}'.format(*item2))
#         print(item[2] + item2[2])

arquivo = open('Pag1.csv')
for Item in arquivo:
    qtd_Item = len(Item[-5:])
    preco_Item = len(Item[5:])
    print(Item[0: preco_Item])
    # print('Item: {}, Preço: R${}'.format(*Item.strip().split(',')))

arquivo2 = open('Pag2.csv')
for Item2 in arquivo2:
    qtd_Item2 = len(Item2[:-6])
    print(Item2[0: qtd_Item])
    # print('Item: {}, Preço: R${}'.format(*Item2.strip().split(',')))

print(f'Combo: {Item[0: qtd_Item]} & {Item2[0: qtd_Item2]} por apenas'
      f'')

arquivo.close()
arquivo2.close()
