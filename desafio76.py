'''Crie um programa que tenha uma tupla única com nomes
de produtos e seus respectivos preços na sequência. No
final, mostre uma listagem de preços, organizando os
dados em forma tabular.'''
print('=' * 50)
print(' ' * 10, 'Programa \033[1;4mDESAFIO76\033[m iniciado.')
print('=' * 50)

print('Lista de itens:')

#Lista com nomes e preços
produtos = ('Batata', 50.00, 'Morango', 20.00, 'Pêssego', 35.00, 'Refrigerante', 5.00, 'Esfihas', 0.50)

aux = 40 - len(produtos)
#print(produtos, '-' * aux)
#PRODUTO.................R$ 10.00
#nome + (len(produto) - (qntde de pontos) + R$ produtos[cont]
aux2 = len(produtos)
cont1 = 0
cont2 = 1
while cont1 <= aux2:
    print(produtos[cont1], ('.' * (20-len(produtos[cont1]))), f'\033[33mR$ {produtos[cont2]}\033[m')
    cont1 += 2
    cont2 += 2
    if cont1 >= aux2 and cont2 > aux2:
        break

print('=' * 50)
print('Fim do programa.')
