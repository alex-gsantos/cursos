'''Crie um programa que leia vários números inteiros pelo
teclado. O programa só vai parar quando o usuário digitar
999, que é a condição de parada. No final, mostre quantos
números foram digitados e qual foi a soma entre eles
(desconsiderando o flag).'''
print('=' * 50)
print((' ' * 10), 'Programa \033[1;4mDESAFIO66\033[m iniciado.')
print('=' * 50)

soma = 0
cont = 0
num = int(input('Digite um número ou 999 para sair: '))
while num != 999:
        cont += 1
        soma += num
        num = int(input('Digite um número: '))
print('_' * 50)

print(f'Foram digitados um total de \033[1;32m{cont}\033[m números, e sua soma dá \033[1;32m{soma}\033[m.')

print('=' * 50)
print('Programa encerrado.')
