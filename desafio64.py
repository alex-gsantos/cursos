''''Crie um programa que leia vários números inteiros
pelo teclado. o programa só vai parar quando o usuário
digitar o valor 999, que é a condição de parada. No
final, mostre quantos números foram digitados e qual foi
a soma entre eles (desconsiderando o flag).'''
soma = 0
cont = 0
n1 = int(input('Digite um número (ou \033[31m999\033[m para sair): '))
if n1 == 999:
    print('Tchau.')
else:
    while n1 != 999:
        soma += n1
        cont += 1
        n1 = int(input('Digite um número (ou \033[31m999\033[m para sair): '))
    print('Foram digitados um total de \033[33m{}\033[m números. A soma deles dá \033[33m{}\033[m.'
          .format(cont, soma))
