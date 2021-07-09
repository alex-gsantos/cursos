'''Faça um programa que leia três números e mostre qual
é o maior e qual é o menor.'''
print('=' * 50)
print((' ' * 10), 'Programa \033[1;4mDESAFIO33\033[m iniciado.')
print('=' * 50)

n1 = int(input('Digite o \033[4mprimeiro\033[m número: '))
maior = n1
menor = n1
n2 = int(input('Digite o \033[4msegundo\033[m número: '))
if n2 >= n1:
    maior = n2
else:
    menor = n2
n3 = int(input('Digite o \033[4mterceiro\033[m número: '))
if n3 >= maior:
    maior = n3
else:
    if n3 <= menor:
        menor = n3
print('_' * 50)

print('O \033[32mmaior\033[m número entre os 3 é: '
      '\033[32m{}\033[m.'.format(maior))
print('O \033[31mmenor\033[m número entre os 3 é: '
      '\033[31m{}\033[m.'.format(menor))

print('=' * 50)
print('Fim do programa.')