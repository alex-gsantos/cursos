'''Escreva um programa que leia um número inteiro qualquer e
peça para o usuário escolher qual será a base de
conversão:
1) para binário
2) para octal
3) para hexadecimal'''
print('=' * 50)
print((' ' * 10), 'Programa \033[1;4mDESAFIO37\033[m iniciado.')
print('=' * 50)

num = int(input('Digite um número inteiro: '))
a = int(input('Digite a opção que você quer:\n'
        '\033[31m1\033[m - Converter para binário\n'
        '\033[31m2\033[m - Converter para octal\n'
        '\033[31m3\033[m - Converter para hexadecimal\n'))
print('_' * 50)

if a == 1:
    print('O número \033[32m{}\033[m convertido para binário fica \033[32m{}\033[m.'
          .format(num, bin(num)))
elif a == 2:
    print('O número \033[32m{}\033[m convertido para octal fica \033[32m{}\033[m.'
          .format(num, oct(num)))
elif a == 3:
    print('O número \033[32m{}\033[m convertido para hexadecimal fica \033[32m{}\033[m.'
          .format(num, hex(num)))
else:
    print('Opção inválida. Programa terminado.')

print('=' * 50)
print('Fim do programa.')
