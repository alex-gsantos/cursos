'''Faça um programa que leia um número Inteiro e mostre na tela
o seu sucessor e o seu antecessor.'''
print('=' * 50)
print((' ' * 10), 'Programa \033[mDESAFIO05\033[m iniciado.')
print('=' * 50)

num = int(input('Digite um número: '))
print('_' * 50)
print('O número é \033[4;34m{}\033[m. Seu antecessor é '
      '\033[32m{}\033[m, e seu sucessor é \033[32m{}\033[m.'
      .format(num, (num - 1), (num + 1)))

print('=' * 50)
print('Fim do programa.')
