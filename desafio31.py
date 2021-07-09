'''Desenvolva um programa que pergunte a distância de uma
viagem em Km. Calcule o preço da passagem, cobrando R$ 0,50
por Km para viagens de até 200Km e R$ 0,45 para viagens mais
longas.'''
print('=' * 50)
print((' ' * 10), 'Programa \033[1;4mDESAFIO31\033[m iniciado.')
print('=' * 50)

distancia = float(input('Digite a distância a percorrer\033[32m(em Km)\033[m: '))
if distancia <= 200:
    total = distancia * 0.5
    print('A distância da viagem é de \033[32m{} Km\033[m, o custo da passagem será de \033[31mR$ 0,50\033[m por Km. '
          'Total de \033[33mR$ {:.2f}\033[m.'.format(distancia, total))
else:
    total = distancia * 0.45
    print('A distância da viagem é de \033[32m{} Km\033[m, o custo da passagem será de \033[31mR$ 0,45\033[m por Km.'
          'Total de \033[33mR$ {:.2f}\033[m.'.format(distancia, total))

print('=' * 50)
print('Fim do programa.')
