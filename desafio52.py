'''Faça um programa que leia um número inteiro e diga
se ele é ou não um número primo.'''
print('=' * 50)
print((' ' * 10), 'Programa \033[1;4mDESAFIO52\033[m iniciado.')
print('=' * 50)

num = int(input('Digite um número: '))
aux = 0
for cont in range(1, (num + 1)):
#    num % cont
    if (num % cont == 0):
        aux += 1
#esquema de contagem de quantas vezes o número foi múltiplo de alguém
if aux > 2:
    print('\033[35m{}\033[m não é um número primo.'.format(num))
else:
    print('\033[35m{}\033[m é um número primo.'.format(num))

print('=' * 50)
print('Fim do programa.')
