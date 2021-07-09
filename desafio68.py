'''Faça um programa que jogue par ou ímpar com o
computador. O jogo só será interrompido quando o
jogador perder, mostrando o total de vitórias
consecutivas que ele conquistou no final do jogo.'''
print('=' * 50)
print((' ' * 10), 'Programa \033[1;4mDESAFIO68\033[m iniciado.')
print('=' * 50)

import random

vitorias = 0
aux = 1
while aux == 1:
    resposta = str(input('Escolha par ou ímpar: \n'))
    usuario = int(input('Digite um número: '))
    pc = random.randint(0, 101)
    if (usuario + pc) % 2 == 0 and resposta == 'par':
        print(f'Eu escolhi \033[33m{pc}\033[m e você \033[33m{usuario}\033[m. Deu \033[34mpar\033[m, você \033[34mganhou\033[m.')
        vitorias += 1
    elif (usuario + pc) % 2 != 0 and resposta == 'impar':
        print(f'Eu escolhi \033[33m{pc}\033[m e você \033[33m{usuario}\033[m. Deu \033[34mímpar\033[m, você \033[34mganhou\033[m.')
        vitorias += 1
    else:
        print(f'Eu escolhi \033[33m{pc}\033[m e você \033[33m{usuario}\033[m ({pc + usuario}). Você \033[31mperdeu\033[m.')
        aux = 0
print(f'O seu total de vitórias é \033[32m{vitorias}\033[m.')

print('=' * 50)
print('Fim do programa.')
