'''Crie um programa que leia um número inteiro e mostre na
tela se ele é PAR ou ÍMPAR.'''
print('=' * 50)
print((' ' * 10), 'Programa \033[1;4mDESAFIO30\033[m iniciado.')
print('=' * 50)

num = int(input('Digite um número: '))
if (num % 2 == 0):
    print('Você digitou um número \033[1;4mpar\033[m.')
else:
    print('Você digitou um número \033[1;4mímpar\033[m.')

print('=' * 50)
print('Fim do programa.')
