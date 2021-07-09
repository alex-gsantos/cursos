'''Escreva um programa que leia um número n inteiro
qualquer e mostre na tela os n primeiros elementos de
uma Sequência de Fibonacci.'''
num = int(input('Quantos elementos da Sequência de Fibonacci você quer ver?\n'))
ant = 1
atual = 1
cont = 1
if num == 1:
    print('\033[34m', 0)
else:
    print('\033[34m', atual, ',', end='')
    cont += 1
    while cont <= num:
        if cont == num:
            print(atual)
        else:
            print(atual, ',', end='')
            aux = ant
            ant = atual
            atual = atual + aux
        cont += 1

