'''Faça um programa que leia um número qualquer emostre o
seu fatorial. Faça duas versões, uma com WHILE e outra FOR.'''
print('=' * 50)
print((' ' * 10), 'Programa \033[1;4mDESAFIO60\033[m iniciado.')
print('=' * 50)

soma = 0
aux = 1
num = int(input('Digite um número: '))
print(num, '! = ', end='')
for cont in range(1, (num + 1)):
    if cont == 1:
        soma = 1
        print(f'{cont} x ', end='')
    else:
        if cont == num:
            print(f'{cont}')
            soma = cont * soma
        else:
            print(f'{cont} x ', end='')
            soma = cont * soma
print()
print('Total = \033[33m', soma, '\033[m')
print('_' * 50)

soma = 0
aux = 1
num = int(input('Digite um número: '))
cont = 1
print(num, '! = ', end='')
while cont <= num:
    if cont == num:
        print(f'\033[33m{cont}\033[m')
        aux = aux * cont
        cont += 1
    else:
        print(f'\033[33m{cont}\033[m', 'x ', end='')
        aux = aux * cont
        cont += 1
print()
print(f'Total: \033[33m{aux}\033[m')

print('=' * 50)
print('Fim do programa.')

