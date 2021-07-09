'''Desenvolva um programa que leia seis números inteiros
e mostre a soma apenas daqueles que forem pares. Se o
valor digitado por ímpar, desconsidere-o.'''
print('=' * 50)
print((' ' * 10), 'Programa \033[1;4mDESAFIO50\033[m iniciado.')
print('=' * 50)

soma = 0
for i in range(1, 7):
    num = int(input('Digite um número inteiro: '))
    if num % 2 == 0:
        soma += num
print('_' * 50)

print('A soma dos números pares é: \033[36m', soma, '\033[m')

print('=' * 50)
print('Fim do programa.')
