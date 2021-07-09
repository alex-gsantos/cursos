'''
Faça um programa que leia o nome e peso de várias pessoas,
guardando tudo em uma lista. No final, mostre:
A) quantas pessoas foram cadastradas
B) uma listagem com as pessoas mais pesadas
C) uma listagem com as pessoas mais leves
'''
print('=' * 50)
print((' ' * 10), 'Programa \033[1;4mDESAFIO84\033[m iniciado.')
print('=' * 50)

lista_tudo = list()
lista_pesadas = list()
lista_leves = list()
cont = 0
resposta = 'S'
while resposta == 'S':
    lista_tudo.append(str(input('Nome: ')))
    lista_tudo.append(float(input('Peso: ')))
    if cont == 0:
        lista_pesadas.append(lista_tudo[0])
        lista_pesadas.append(lista_tudo[1])
        lista_leves.append(lista_tudo[0])
        lista_leves.append(lista_tudo[1])
        lista_tudo.clear()
    else:
        if lista_tudo[1] == lista_pesadas[1]:
            lista_pesadas.append(lista_tudo[0])
            lista_pesadas.append(lista_tudo[1])
            lista_tudo.clear()
        elif lista_tudo[1] > lista_pesadas[1]:
            lista_pesadas.clear()
            lista_pesadas.append(lista_tudo[0])
            lista_pesadas.append(lista_tudo[1])
            lista_tudo.clear()
        elif lista_tudo[1] == lista_leves[1]:
            lista_leves.append(lista_tudo[0])
            lista_leves.append(lista_tudo[1])
            lista_tudo.clear()
        elif lista_tudo[1] < lista_leves[1]:
            lista_leves.clear()
            lista_leves.append(lista_tudo[0])
            lista_leves.append(lista_tudo[1])
            lista_tudo.clear()
    cont += 1
    resposta = str(input('Deseja continuar [S/N]:\n')).upper()

print('_' * 50)
print(f'Quantidade de pessoas cadastradas: \033[33m{cont}\033[m')
print(f'Lista das pessoas mais pesadas: \033[31m{lista_pesadas}\033[m')
print(f'Lista das pessoas mais leves: \033[32m{lista_leves}\033[m')

print('=' * 50)
print('Fim do programa.')