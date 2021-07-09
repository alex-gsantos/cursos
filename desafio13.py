'''Faça um algoritmo que leia o salário de um funcionário e
mostre seu novo salário com 15% de aumento.'''
print('=' * 50)
print((' ' * 10), 'Programa \033[1;4mDESAFIO13\033[m iniciado.')
print('=' * 50)

sal = float(input('Digite quanto você ganha: \033[33mR$ '))
print('\033[m')
aumento = sal + (sal * 0.15)
print('\033[1mParabéns!!!\033[m Você ganhou \033[33m15%\033[m de '
      '\033[4;34maumento!\033[m Seu novo salário '
      'é \033[32mR$ {:.2f}\033[m.'.format(aumento))

print('=' * 50)
print('Fim do programa.')
