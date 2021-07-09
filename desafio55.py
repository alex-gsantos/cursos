'''Faça um programa que leia o peso de cinco pessoas.
No final, mostre qual foi o maior e o menor peso lidos.'''
print('=' * 50)
print((' ' * 10), 'Programa \033[1;4mDESAFIO55\033[m iniciado.')
print('=' * 50)

print('Digite o peso de 5 pessoas:')
for cont in range(1, 6):
    peso = float(input('Peso da pessoa {} = '.format(cont)))
    if cont == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('_' * 50)

print('O maior peso é: \033[1;31m{:.2f}\033[m'.format(maior))
print('O menor peso é: \033[1;32m{:.2f}\033[m'.format(menor))
# INSERIR CONDICIONAIS DENTRO DO LAÇO. INSERIR EXCEÇÃO.

print('=' * 50)
print('Fim do programa.')
