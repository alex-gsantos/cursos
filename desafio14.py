'''Escreva um programa que converta uma temperatura digitada
em ºC e converta para ºF.'''
print('=' * 50)
print((' ' * 10), 'Programa \033[1;4mDESAFIO14\033[m iniciado.')
print('=' * 50)

temp = float(input('Digite a temperatura em \033[31mºC\033[m: '))
f = (temp * 1.8) + 32
print('A temperatura de \033[31m{}ºC\033[m equivale a '
      '\033[34m{}ºF\033[m.'
      .format(temp, f))

print('=' * 50)
print('Fim do programa.')
