'''Faça um programa que mostre na tela uma contagem
regressiva para o estouro de fogos de artifício,
indo de 10 até 0, com uma pausa de 1 segundo entre eles.'''
print('=' * 50)
print((' ' * 10), 'Programa \033[1;4mDESAFIO46\033[m iniciado.')
print('=' * 50)

import time, sys

print('Contagem regressiva:')
for i in range(10, -1, -1):
    time.sleep(1)
    print('\033[31m', i, '\033[m')
print('\033[1mBADA BOOM!!!')
