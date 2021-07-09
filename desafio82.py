'''
Crie um programa que vai ler vários números e colocar em
uma lista. Depois disso, crie duas listas extras que vão
conter apenas os valores pares e os valores ímpares
digitados, respectivamete. Ao final, mostre o conteúdo
das três listas geradas.
'''
print('=' * 50)
print((' ' * 10), 'Programa \033[1;4mDESAFIO82\033[m iniciado.')
print('=' * 50)

lista = []
lista_par = []
lista_impar = []
resposta = 'S'
aux = 1
while aux != 0:
    aux = int(input('Digite \033[31m0(zero)\033[m para sair. Insira um número: '))
    if aux == 0:
        break
    else:
        lista.append(aux)

for num in lista:
    if (num % 2 == 0):
        lista_par.append(num)
    else:
        lista_impar.append(num)

print('_' * 50)
print(f'Lista original: \033[36m{lista}\033[m')
print(f'Lista só com números pares: \033[36m{lista_par}\033[m')
print(f'Lista só com números ímpares: \033[36m{lista_impar}\033[m')

print('=' * 50)
print('Fim do programa.')
