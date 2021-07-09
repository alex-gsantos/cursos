'''Crie um programa que vai gerar cinco números aleatórios
e colocar em uma tupla. Depois disso, mostre a listagem
de números gerados e também indique o menor e o maior
valor que estão na tupla.'''
import random
print('=' * 50)
print((' ' * 10), 'Programa \033[1;4mDESAFIO74\033[m iniciado.')
print('=' * 50)

import random

n1 = random.randint(1, 100)
maior = n1
menor = n1
n2 = random.randint(1, 100)
if n2 > maior:
    maior = n2
if n2 < menor:
    menor = n2
n3 = random.randint(1, 100)
if n3 > maior:
    maior = n3
if n3 < menor:
    menor = n3
n4 = random.randint(1, 100)
if n4 > maior:
    maior = n4
if n4 < menor:
    menor = n4
n5 = random.randint(1, 100)
if n5 > maior:
    maior = n5
if n5 < menor:
    menor = n5
aux = (n1, n2, n3, n4, n5)

print(f'Lista dos números gerados: \033[33m{aux}\033[m')
print(f'Maior número da lista: \033[33m{maior}\033[m')
print(f'Menor número da lista: \033[33m{menor}\033[m')

print('=' * 50)
print('Fim do programa.')

'''
aux = ('', '', '', '', '')

for cont in range(0, 5):
    aux[cont] = random.randint(1, 100)
#como criar uma string que receba valor INT a cada rodada do loop?
#essa string deve colocar cada random numa posição crescente dentro de si(começa no 0)
    #criar várias variáveis, fazer uma lista
#para criar a tupla eu preciso que uma variável receba todos os valores de uma vez só
    if cont == 0:
        maior = aux
        menor = aux
    else:
        if aux > maior:
            maior = aux
        if aux < menor:
            menor = aux
    print('Random = ', aux)

#posso referenciar numeros inteiros a cada conteúdo em determinado índice na variável 'aux'
'''