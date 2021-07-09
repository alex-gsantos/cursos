'''Faça um programa que leia um numero de 0 a 9999 e  mostre
na tela cada um dos digitos separados
ex.: 1834
unidade: 4
dezena: 3
centena: 8
milhar: 1'''
print('=' * 50)
print((' ' * 10), 'Programa \033[1;4mDESAFIO23\033[m iniciado.')
print('=' * 50)

numero = int(input('Digite um número entre 0 e 9999: '))
num1 = numero % 10
num2 = numero // 10
print('\033[31mUnidade\033[m:', num1)
num1 = num2 % 10
print('\033[32mDezena\033[m:', num1)
num2 = num2 // 10
num1 = num2 % 10
print('\033[33mCentena\033[m:', num1)
num2 = num2 // 10
num1 = num2 % 10
print('\033[34mMilhar\033[m:', num1)

print('=' * 50)
print('Fim do programa.')
