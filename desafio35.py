'''Desenvolva um programa que leia o comprimento de três retas
e diga ao usuário se elas podem ou não formar um triângulo.'''
print('=' * 50)
print((' ' * 10), 'Programa \033[1;4mDESAFIO35\033[m iniciado.')
print('=' * 50)

l1 = int(input('Digite a reta 1: '))
l2 = int(input('Digite a reta 2: '))
l3 = int(input('Digite a reta 3: '))

if l2 >= l3:
    maior = l2
    menor = l3
else:
    maior = l3
    menor = l2
if (maior - menor) < l1:
    if l1 < (maior + menor):
        aux1 = 1
    else:
        aux1 = 0
else:
    aux1 = 0

if l1 >= l3:
    maior = l1
    menor = l3
else:
    maior = l3
    menor = l1
if (maior - menor) < l2:
    if l2 < (maior + menor):
        aux2 = 1
    else:
        aux2 = 0
else:
    aux2 = 0

if l1 >= l2:
    maior = l1
    menor = l2
else:
    maior = l2
    menor = l1
if (maior - menor) < l3:
    if l3 < (maior + menor):
        aux3 = 1
    else:
        aux3 = 0
else:
    aux3 = 0
print('_' * 50)

if aux1 == 1:
    if aux2 == 1:
        if aux3 == 1:
            print('\033[1;32mPodem\033[m formar triângulo.')
        else:
            print('\033[1;31mNão podem\033[m formar triângulo.')
    else:
        print('\033[1,31mNão podem\033[m formar triângulo.')
else:
    print('\033[1;31mNão podem\033[m formar triângulo.')

print('=' * 50)
print('Fim do programa.')
