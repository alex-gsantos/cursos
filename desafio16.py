'''Crie um programa que leia um número Real qualquer pelo
teclado e mostre na tela a sua porção inteira.
ex.: 6.127 -> mostrará apenas o 6.'''
print('=' * 50)
print((' ' * 10), 'Programa \033[1;4mDESAFIO16\033[m iniciado.')
print('=' * 50)

import math
num = float(input('Digite um número com casas decimais: '))
inteiro = math.trunc(num)
print('A função \033[1;36m"math.trunc()"\033[m tira as casas '
      '\033[4mdecimais\033[m de um número e fica só com a '
      'parte \033[4minteira\033[m: '
      '\033[7;31;43m', inteiro, '\033[m')

print('=' * 50)
print('Fim do programa.')
