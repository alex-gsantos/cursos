'''Escreva um programa que leia um valor em metros e exiba
convertido em centímetros e milímetros.'''
print('=' * 50)
print((' ' * 10), 'Programa \033[1;4mDESAFIO08\033[m iniciado.')
print('=' * 50)

metro = float(input('Digite o tamanho em metros: '))
cent = metro * 100
mili = metro * 1000
print('_' * 50)
print('Tamanho: \033[4m{}\033[m metros\n'
      'Convertido em centímetros: \033[4;35m{}\033[m\n'
      'Convertido em milimetros: \033[4;35m{}\033[m'
      .format(metro, cent, mili))

print('=' * 50)
print('Fim do programa.')
