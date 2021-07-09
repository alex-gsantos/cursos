'''Crie um programa que leia o nome e o preço de vários
produtos. O programa deverá perguntar se o usuário vai
continuar. No final, mostre:
A) qual é o total gasto na compra
B) quantos produtos custam mais de R$ 1,000.00
C) qual é o nome do produto mais barato'''
print('=' * 50)
print(('_' * 10), 'Programa \033[1;4mDESAFIO70\033[m iniciado.')
print('=' * 50)

cont_mais = 0
total = 0.0
nome_mais_barato = 'n'
mais_barato = 0.0
continuar = 'S'

while continuar == 'S':
    nome = str(input('Digite o nome do produto: '))
    preco = float(input('Digite o preço do produto: \033[33mR$\033[m '))
    if nome_mais_barato == 'n' and mais_barato == 0.0:
        nome_mais_barato = nome
        mais_barato = preco
    else:
        if preco > 1000:
            cont_mais += 1
        if preco < mais_barato:
            mais_barato = preco
            nome_mais_barato = nome
    total += preco
    continuar = str(input('Deseja continuar as compras? [S/N]\n')).upper()
    print('_' * 50)

print(f'A) O total gasto na compra é de \033[33mR$ {total}\033[m\n'
      f'B) A quantidade de produtos acima de \033[33mR$ 1,000.00\033[m é de \033[33m{cont_mais}\033[m item(ns)\n'
      f'C) O nome do produto mais barato é \033[33m{nome_mais_barato}\033[m')

print('=' * 50)
print('Fim do programa.')
