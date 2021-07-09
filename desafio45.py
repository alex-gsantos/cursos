'''Crie um programa que faça o computador jogar jokenpo com
você.'''
print('=' * 50)
print((' ' * 10), 'Programa DESAFIO45 iniciado.')
print('=' * 50)

import random
print('Olá! Vamos jogar Jokênpo?\n'
      '1 - Sim\n'
      '2 - Não')
a = int(input())
if a == 1:
    print('Informe o número da sua jogada:\n'
          '1 - Pedra\n'
          '2 - Papel\n'
          '3 - Tesoura')
    a = int(input())
    pc = random.randint(1, 3)
    print('_' * 50)
    if a == pc:
        print('Escolhemos a mesma opção. Deu empate. ~.~')
    else:
        if a == 1 and pc == 2:
            print('Escolhi papel e você pedra. \033[7mGanhei!\033[m *_*')
        elif a == 1 and pc == 3:
            print('Escolhi tesoura e você pedra. Você ganhou... :(')
        elif a == 2 and pc == 1:
            print('Escolhi pedra e você papel. Você ganhou... :(')
        elif a == 2 and pc == 3:
            print('Escolhi tesoura e você papel. \033[7mGanhei!\033[m *_*')
        elif a == 3 and pc == 1:
            print('Escolhi pedra e você tesoura. \033[7mGanhei!\033[m *_*')
        elif a == 3 and pc == 2:
            print('Escolhi papel e você tesoura. Você ganhou... :(')
elif a == 2:
    print('Que pena...')
else:
    print('Opção inválida. Programa terminado.')

print('=' * 50)
print('Fim do programa.')
