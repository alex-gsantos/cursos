'''Escreva um programa que leia dois números inteiros e
compare-os, mostrando na tela alguma destas mensagens:
- O primeiro valor é maior
- O segundo valor é maior
- Não existe valor maior, os dois são iguais'''
print('=' * 50)
print((' ' * 10), 'Programa \033[1;4mDESAFIO38\033[m iniciado.')
print('=' * 50)

print('Digite dois números \033[1minteiros\033[m:')
n1 = int(input('Primeiro - '))
n2 = int(input('Segundo - '))
print('_' * 50)

if n1 > n2:
    print('O \033[4mprimeiro\033[m é maior.')
elif n1 < n2:
    print('O \033[4msegundo\033[m é maior.')
else:
    print('Não existe valor maior, os dois são \033[4miguais\033[m.')

print('=' * 50)
print('Fim do programa.')