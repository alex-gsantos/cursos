'''Escreva um programa que pergunte a quantidade de Km
percorridos por um carro alugado e a quantidade de dias
pelos quais ele foi alugado. Calcule o preço a pagar,
sabendo que o carro custa R$ 60 por dia e R$0,15 por Km rodado.'''
print('=' * 50)
print((' ' * 10), 'Programa \033[1;4mDESAFIO15\033[m iniciado.')
print('=' * 50)

kmrodado = float(input('Informe a quantidade de quilômetros rodados: '))
dias = int(input('Informe a quantidade de dias que você está com o carro: '))
totalapagar = (kmrodado * 0.15) + (dias * 60)
print('_' * 50)

print('Você está com o carro há \033[4;34m{} dias\033[m e '
      'andou \033[4;34m{} quilômetros\033[m.\n'
      'O total a pagar pelo aluguel do carro é de '
      '\033[33mR$ {:.2f}\033[m.'
      .format(dias, kmrodado, totalapagar))

print('=' * 50)
print('Fim do programa.')
