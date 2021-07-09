'''Escreva um programa para aprovar o empréstimo bancário
para a compra de uma casa. O programa vai perguntar o
valor da casa, o salário do comprador e em quantos anos
ele vai pagar. Calcule o valor da prestação mensal,
sabendo que ela não pode exceder 30% do salário ou então
o empréstimo será negado.'''
print('=' * 50)
print((' ' * 10), 'Programa \033[1;4mDESAFIO36\033[m iniciado.')
print('=' * 50)

print('Olá! Para conseguir um empréstimo para comprar uma casa, primeiro responda a algumas perguntas.')
valor_casa = float(input('Digite o valor da casa: '))
sal_comprador = float(input('Informe o seu salário: '))
anos = int(input('Diga em quantos anos você quer pagar a casa: '))
print('_' * 50)

parcelas = valor_casa / (anos * 12)
if parcelas > (sal_comprador * 0.3):
    print('As parcelas do pagamento mensal são de \033[31mR$ {:.2f}\033[m \033[4mpor mês\033[m, excedendo \033[31m30%\033[m '
          'do seu salário (\033[31mR$ {:.2f}\033[m). Empréstimo \033[1mnegado\033[m.'
          .format(parcelas, (sal_comprador * 0.3)))
else:
    print('As parcelas do pagamento mensal são de \033[32mR$ {:.2f}\033[m \033[4mpor mês\033[m e não excedem \033[32m30%\033[m '
          'do seu salário (\033[32mR$ {:.2f}\033[m). Empréstimo \033[1maprovado\033[m.'
          .format(parcelas, (sal_comprador * 0.3)))

print('=' * 50)
print('Fim do programa.')
