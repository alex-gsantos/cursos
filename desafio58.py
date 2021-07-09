'''Melhore o jogo do DESAFIO28  onde o computador vai
pensar em um número entre 0 e 10. Só que agora o jogador
vai tentar adivinhar até acertar, mostrando no final
quantos palpites foram necessários para vencer.'''
print('=' * 50)
print((' ' * 10), 'Programa \033[1;4mDESAFIO58\033[m iniciado.')
print('=' * 50)

import random

print('Vou pensar em um número entre 1 e 10. Tente adivinhar!')
r = int(input('\033[36mResposta:\033[m '))
pc = random.randint(1, 11)
cont = 1
while r != pc:
    r = int(input('Número errado. Tente novamente: '))
    cont += 1
print('_' * 50)
print('Acertou, eu escolhi o \033[33m{}\033[m! Você levou \033[33m{}\033[m tentativa(s) para adivinhar.'
      .format(pc, cont))

print('=' * 50)
print('Fim do programa.')
