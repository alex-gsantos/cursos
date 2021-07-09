'''Crie um programa que leia dois números e mostre a soma
entre eles.'''
print('=' * 50)
print((' ' * 10), 'Programa \033[1;4mDESAFIO03\033[m iniciado.')
print('=' * 50)

num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
print('_' * 50)
#dentro do PRINT eu também posso inserir variáveis e realizar operações com elas
print('A soma deles é:', '\033[35m',(num1 + num2), '\033[m')

print('=' * 50)
print('Fim do programa.')
