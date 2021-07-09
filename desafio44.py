'''Elabore um programa que calcule o valor a ser pago por
um produto, considerando o seu preço normal e condição
de pagamento:
- à vista dinheiro/cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preço normal
- 3x ou mais no cartão: 20% de juros'''
print('=' * 50)
print((' ' * 10), 'Programa \033[1;4mDESAFIO44\033[m iniciado.')
print('=' * 50)

valor = float(input('Digite o valor do produto: R$ '))
print('Informe qual a forma de pagamento:\n'
      '1 - à vista dinheiro/cheque\n'
      '2 - à vista no cartão\n'
      '3 - até 2x no cartão\n'
      '4 - 3x ou mais no cartão')
forma = int(input())
if forma == 1:
    print('O total a pagar pelo item é de \033[32mR$ {:.2f}\033[m.'.format(valor * 0.9))
elif forma == 2:
    print('O total a pagar pelo item é de \033[32mR$ {:.2f}\033[m.'.format(valor * 0.95))
elif forma == 3:
    print('O total a pagar pelo item é de \033[33mR$ {:.2f}\033[m.'.format(valor))
elif forma == 4:
    print('O total a pagar pelo item é de R$ \033[31m{:.2f}\033[m.'.format(valor * 1.2))
else:
    print('Operação inválida. Fim da operação.')

print('=' * 50)
print('Fim do programa.')
