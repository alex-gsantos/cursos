'''Crie um programa que leia o nome de uma cidade e diga se ela
começa ou não com o nome "Santo".'''
print('=' * 50)
print((' ' * 10), 'Programa \033[1;4mDESAFIO24\033[m iniciado.')
print('=' * 50)

nome = str(input('Digite o nome de uma cidade: '))
nome2 = nome.split()
print('Existe a palavra "Santo" no nome da cidade? \n\033[33m', 'Santo' in nome2[0], '\033[m')

print('=' * 50)
print('Fim do programa.')
