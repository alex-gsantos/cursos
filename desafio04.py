'''Faça um programa que leia algo pelo teclado e mostre
na tela o seu tipo primitivo e todas as informações
possíveis sobre ele.'''
print('=' * 50)
print((' ' * 10), 'Programa \033[1;4mDESAFIO04\033[m iniciado.')
print('=' * 50)

info = input('Digite \033[4malgo\033[m: ')
print(info.isalnum())
print(info.isalpha())
print(info.isdecimal())
print(info.islower())
print(info.isnumeric())
print(info.isupper())
print(info.istitle())

print('=' * 50)
print('Fim do programa.')
