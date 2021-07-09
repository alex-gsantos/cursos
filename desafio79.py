'''
Crie um programa onde o usuário possa digitar vários
valores numéricos e cadastre-os em uma lista. Caso o
número já exista lá dentro, ele não será adicionado.
No final, serão exibidos todos os valores únicos digitados,
em ordem crescente.
'''
print('=' * 50)
print((' ' * 10), 'Programa \033[1;4mDESAFIO79\033[m iniciado.')
print('=' * 50)

lista = []
cont = 0
resposta = 'S'
while resposta == 'S':
    aux = int(input('Digite um número: '))
    if aux in lista:
        print('Já existe esse número na lista.')
    else:
        lista.append(aux)
    resposta = str(input('Deseja continuar? [S/N]\n')).upper()

print('_' * 50)
lista.sort()
print(f'Os números existentes na lista, em ordem crescente: \033[33m{lista}\033[m')

print('=' * 50)
print('Fim do programa.')
