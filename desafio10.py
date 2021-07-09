'''Crie um programa que leia quanto dinheiro uma pessoa tem na
carteira e mostra quantos dólares ela pode comprar.
Considerar US$ 1,00 = R$ 3,27'''
print('=' * 50)
print((' ' * 10), 'Programa \033[1;4mDESAFIO10\033[m iniciado.')
print('=' * 50)

real = float(input('Quantos reais você têm?\n'
                   '\033[33mR$: \033[m'))
total = (real / 3.27)
print('Com \033[33mR$ {}\033[m você pode comprar '
      '\033[32mUS$ {:.2f}\033[m.'
      .format(real, total))

print('=' * 50)
print('Fim do programa.')
