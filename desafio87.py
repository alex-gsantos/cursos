'''
Aprimore o desafio anterior, mostrando no final:
A) a soma de todos os valores pares digitados
B) a soma dos valores da terceira coluna
C) o maior valor da segunda linha
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

print('_' * 50)
par = 0
linha = 0
while linha < 3:
    coluna = 0
    while coluna < 3:
        if lista[linha][coluna] % 2 == 0:
            par += lista[linha][coluna]
        coluna += 1
    linha += 1
print(f'Soma dos números pares: {par}')

print('_' * 50)
coluna = 2
linha = 0
soma = 0
while linha < 3:
    soma += lista[linha][coluna]
    linha += 1
print(f'A soma dos itens na terceira coluna: {soma}')

print('_' * 50)
linha = 2
coluna = 0
maior = 0
while coluna < 3:
    if lista[linha][coluna] > maior:
        maior = lista[linha][coluna]
    coluna += 1
print(maior)

print('=' * 50)
print('Fim do programa.')
