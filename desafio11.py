'''Faça um programa que leia a largura e a altura de uma parede
em metros, calcule a sua área e a quantidade de tinta
necessária para pintá-la, sabendo que cada litro de tinta
pinta uma área de 2m².'''
print('=' * 50)
print(('' * 10), 'Programa \033[1;4mDESAFIO11\033[m iniciado.')
print('=' * 50)

largura = float(input('Digite a \033[4mlargura\033[m da parede: '))
altura = float(input('Digite a \033[4maltura\033[m da parede: '))
area = largura * altura
tinta = area * 0.5
print('_' * 50)

print('A parede tem \033[31m{}\033[m\033[33mm²\033[m. '
      'Serão necessários \033[31m{}\033[m \033[33mlitros\033[m '
      'de tinta para pintar a parede.'.format(area, tinta))

print('=' * 50)
print('Fim do programa.')
