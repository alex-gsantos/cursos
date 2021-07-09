'''Escreva um programa que faça o computador "pensar" em um
número inteiro entre 0 e 5 e peça para o usuário tentar
descobrir qual foi o número escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu
ou perdeu.'''
print('=' * 50)
print((' ' * 10), 'programa \033[1;4mDESAFIO28\033[m iniciado.')
print('=' * 50)

import random
num = random.randint(1, 5)
print('O computador gerou um número entre \033[36m1\033[m e \033[36m5\033[m. Adivinhe '
      'qual número ele gerou.')
resposta = int(input(''))
if resposta == num:
    print('Você adivinhou o número. '
          '\033[1mParabéns, você ganhou!\033[m '
          '\033[33m:)\033[m')
else:
    print('Você errou o número. '
          'Mais sorte na próxima. \033[31m:(\033[m')

print('=' * 50)
print('Fim do programa.')
