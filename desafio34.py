'''Escreva um programa que pergunte o salário de um funcionário
e calcule o valor do seu aumento.
Para salários superiores a R$ 1.250,00, calcule um aumento
de 10%.
Para os inferiores ou iguais, o aumento é de 15%.'''
print('=' * 50)
print((' ' * 10), 'Programa \033[1;4mDESAFIO34\033[m iniciado.')
print('=' * 50)

salario = float(input('Digite o salário: '))
if salario > 1250:
    salario = salario + (salario * 0.10)
    print('Você recebeu um \033[1;32maumento de 10%!\033[m '
          'Seu novo salário é: \033[4;33mR$ {:.2f}.\033[m'
          .format(salario))
else:
    salario = salario + (salario * 0.15)
    print('Você recebeu um \033[1;32maumento de 15%!\033[m '
          'Seu novo salário é: \033[4;33mR$ {:.2f}\033[m.'
          .format(salario))

print('=' * 50)
print('Fim do programa.')
