'''Faça um programa que leia o comprimento do cateto oposto
e do cateto adjacente de um triângulo retângulo, calcule
e mostre o comprimento da hipotenusa...'''
print('=' * 50)
print((' ' * 10), 'Programa \033[1;4mDESAFIO17\033[m iniciado.')
print('=' * 50)

import math
cateto_oposto = float(input('Digite o cateto \033[4moposto\033[m: '))
cateto_adjacente = float(input('Digite o cateto \033[4madjacente\033[m: '))
#hipotenusa² = cateto_oposto² + cateto_adjacente²
#hipotenusa = (cateto_oposto ** 2 + cateto_adjacente ** 2) ** (1/2)
hipotenusa = math.hypot(cateto_oposto, cateto_adjacente)
print('O valor da hipotenusa é \033[7m{:.2f}\033[m.'.format(hipotenusa))

print('=' * 50)
print('Fim do programa.')
