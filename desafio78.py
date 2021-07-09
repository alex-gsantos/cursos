'''
Faça um programa que leia 5 valores numéricos e guarde-os
em uma lista. No final, mostre qual foi o maior e o menor
valor digitado e as suas respectivas posições na lista.
'''
print('=' * 50)
print((' ' * 10), 'Programa \033[1;4mDESAFIO78\033[m iniciado.')
print('=' * 50)

lista = []
for i in range(0, 5):
    aux = int(input('Digite um número: '))
    lista.append(aux)

maior = lista[0]
menor = lista[0]
for i in range(1, 5):
    if lista[i] > maior:
        maior = lista[i]
    if lista[i] < menor:
        menor = lista[i]
print('_' * 50)

print(f'O \033[4mmaior\033[m número é \033[35m{maior}\033[m, e está lozalizado na posição \033[35m{lista.index(maior)}\033[m.')
print(f'O \033[4mmenor\033[m número é \033[36m{menor}\033[m, e está lozalizado na posição \033[36m{lista.index(menor)}\033[m.')

print('=' * 50)
print('Fim do programa.')
