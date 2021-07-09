'''
Crie um programa onde o usuário possa digitar sete
valores numéricos e cadastre-os em uma lista única que
mantenha separados os valores pares e ímpares. no final,
mostre os valores pares e impares em ordem crescente.
'''
print('=' * 50)
print((' ' * 10), 'Programa \033[1;4mDESAFIO85\033[m iniciado.')
print('=' * 50)

lista = list()
lista_par = list()
lista_impar = list()

for i in range(0, 8):
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        lista_par.append(num)
    else:
        lista_impar.append(num)

lista_par.sort()
lista_impar.sort()
lista.append(lista_par[0:])
lista.append(lista_impar[0:])
print(f'Lista completa: \033[33m{lista}\033[m')
print(f'Lista dos números pares: \033[36m{lista[0]}\033[m')
print(f'Lista dos números impares: \033[34m{lista[1]}\033[m')

print('=' * 50)
print('Fim do programa.')
