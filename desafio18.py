'''Faça um programa que leia um ângulo qualquer e mostre na
tela o valor do seno, cosseno e tangente desse angulo.'''
print('=' * 50)
print((' ' * 10), 'Programa \033[1;4mDESAFIO18\033[m iniciado.')
print('=' * 50)

import math
angulo = float(input('Digite um ângulo: '))
#O método MATH faz a conta com base radianos, então é
#preciso converter GRAUS em RADIANOS
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print('O \033[4mseno\033[m de \033[32m{}º\033[m é '
      '\033[34m{:.2f}\033[m'.format(angulo, seno))
print('O \033[4mcosseno\033[m de \033[32m{}º\033[m é '
      '\033[34m{:.2f}\033[m'.format(angulo, cosseno))
print('A \033[4mtangente\033[m de \033[32m{}º\033[m é '
      '\033[34m{:.2f}\033[m'.format(angulo, tangente))

print('=' * 50)
print('Fim do programa.')
