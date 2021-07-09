'''Faça um algoritmo que leia o preço de um produto e mostre
seu novo preço com 5% de desconto.'''
print('=' * 50)
print((' ' * 10), 'Programa \033[1;4mDESAFIO12\033[m iniciado.')
print('=' * 50)

preco = float(input('Insira o preço do item: \033[33mR$ '))
print('\033[m')
desc = preco - (preco * 0.05)
print('O preço do item com \033[31m5%\033[m de desconto fica '
      '\033[33mR$ {:.2f}.\033[m'
      .format(desc))

print('=' * 50)
print('Fim do programa.')
