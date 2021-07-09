'''
Faça um programa que ajude um jogador da mega sena a criar
palpites. O programa vai perguntar quantos jogos serão
gerados e vai sortear 6 números entre 1 e 60 para cada
jogo, cadastrando tudo em uma lista composta.
Não pode haver números repetidos na mesma lista.
'''

import random
from time import sleep
'''
lista = list()
num = int(input('Digite quantos jogos serão gerados: '))
cont1 = 1
aux = 0
while cont1 <= num:
    cont2 = 1
    while cont2 <= 6:
        aux = random.randint(1, 60)
        lista.append(aux)
        cont2 += 1
    cont1 += 1
    sleep(1)
    print(lista)
    lista.clear()
    #conferir lista2[0] com todos os itens da lista[0:5]
    #conferir lista2[1] com todos os itens da lista[0:5]
'''
print('=' * 50)
print((' ' * 10), 'Programa \033[1;4mDESAFIO88z\033[m iniciado.')
print('=' * 50)

import random
from time import sleep

lista = list()
num = int(input('Digite quantos jogos serão gerados: '))
cont1 = 1
aux = 0
while cont1 <= num:
    cont2 = 1
    while cont2 <= 6:
        aux = random.randint(1, 60)
        lista.append(aux)
        cont2 += 1

    lista2 = lista[:]
    cont3 = len(lista)#TOMAR CUIDADO COM O LEN!!
    n1 = 0
    while n1 < cont3:
        n2 = 0
        while n2 < cont3:
            aux1 = lista[n1]
            aux2 = lista2[n2]
            if aux1 == aux2:
                while aux1 == aux2:
                    aux1 = random.randint(1, 60)
                lista[n1] = aux1
                n2 = 0
            else:
                n2 += 1
        n1 += 1

    cont1 += 1
    sleep(0.5)
    print(lista)
    lista.clear()

print('=' * 50)
print('Fim do programa.')