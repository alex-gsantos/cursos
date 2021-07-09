'''Desenvolva um programa que leia quatros valores
pelo teclado e guarde-os em uma tupla. No final, mostre:
A) quantas vezes apareceu o valor 9
B) em que posição foi digitado o primeiro valor 3
C) quais foram os números pares'''
print('=' * 50)
print((' ' * 10), 'Programa \033[1;4mDESAFIO75\033[m iniciado.')
print('=' * 50)

print('Digite 4 valores:')
n1 = int(input('N1 = '))
n2 = int(input('N2 = '))
n3 = int(input('N3 = '))
n4 = int(input('N4 = '))
tupla = (n1, n2, n3, n4)
print('_' * 50)

print(f'O número \033[36m9\033[m apareceu \033[33m{tupla.count(9)}\033[m vez(es).')
print('_' * 50)

num = tupla.count(3)
if num > 0:
    print(f'O número \033[36m3\033[m apareceu por primeiro na posição \033[33m{tupla.index(3)}\033[m.')
else:
    print('\033[31mNão\033[m existe número \033[36m3\033[m na tupla.')

print('_' * 50)
cont = 0
aux2 = 0
print('Números pares:')

for cont in range(0, 4):
    if (tupla[cont] % 2 == 0):
        print(f'\033[36m{tupla[cont]}\033[m')
        aux2 += 1
if aux2 == 0:
    print('\033[31mNão\033[m existe números pares na tupla.')

print('=' * 50)
print('Fim do programa.')
