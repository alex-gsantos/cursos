'''Crie um programa que simule o funcionamento de um
caixa eletrônico. No início, pergunte ao usuário qual
será o valor a ser sacado (número inteiro) e o programa
vai informar quantas cédulas de cada valor serão
entregues.
OBS.: Considere que o caixa possui cédulas de R$ 50,
R$ 20, R$ 10 e R$ 1.'''
print('=' * 50)
print((' ' * 10), 'Programa \033[1;4mDESAFIO71\033[m iniciado.')
print('=' * 50)

valor = int(input('Digite qual o valor a ser sacado: R$ '))
n50 = valor // 50
aux1 = valor - (50 * n50)
n20 = aux1 // 20
aux2 = aux1 - (20 * n20)
n10 = aux2 // 10
n1 = aux2 - (10 * n10)
print('Serão \033[35m{}\033[m notas de \033[32mR$ 50\033[m, '
      '\033[35m{}\033[m de \033[32mR$ 20\033[m, '
      '\033[35m{}\033[m de \033[32mR$ 10\033[m, '
      '\033[35m{}\033[m de \033[32mR$ 1\033[m.'
      .format(n50, n20, n10, n1))

print('=' * 50)
print('Fim do programa.')
