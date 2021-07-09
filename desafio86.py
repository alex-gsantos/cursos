'''
Crie um programa que crie uma matriz de dimensão 3x3 e
preencha com valores lidos pelo teclado. No final, mostre
a matriz na tela, com a formatação correta.
'''
print('=' * 50)
print((' ' * 10), 'Programa \033[1;4mDESAFIO86\033[m iniciado.')
print('=' * 50)

lista = list()
num = list()
linha = 0
while linha < 3:
    coluna = 0
    while coluna < 3:
        aux = int(input('Digite um número: '))
        num.append(aux)
        coluna += 1
    lista.append(num[0:])
    num.clear()
    linha += 1
print('_' * 50)

linha = 0
while linha < 3:
    coluna = 0
    while coluna < 3:
        print(f'[ {lista[linha][coluna]} ] ', end='')
        coluna += 1
    linha += 1
    print()

print('=' * 50)
print('Fim do programa.')
