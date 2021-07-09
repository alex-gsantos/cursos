'''Faça um programa que calcule a soma entre todos os
números ímpares que são múltiplos de três e que se
encontram no intervalo de 1 até 500.'''
print('=' * 50)
print((' ' * 10), 'Programa \033[1;4mDESAFIO48\033[m iniciado.')
print('=' * 50)

soma = 0
for cont in range(1, 501):
    if (cont % 2 !=0) and (cont % 3 == 0):
        print(cont)
        soma += cont
print('Soma de todos os números ímpares múltiplos de 3: \033[33m', soma, '\033[m')

print('=' * 50)
print('Fim do programa.')
