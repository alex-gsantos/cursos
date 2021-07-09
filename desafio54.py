'''Crie um programa que leia o ano de nascimento de sete
pessoas. No final, mostre quantas pessoas ainda não
atingiram a maioridade e quantas já são maiores.
Considere 21 anos a maioridade.'''
print('=' * 50)
print((' ' * 10), 'Programa \033[1;4mDESAFIO54\033[m iniciado.')
print('=' * 50)

de_maior = 0
de_menor = 0
for cont in range(1, 8):
    aux = int(input('Digite a idade da pessoa {}: '.format(cont)))
    if aux >= 21:
        de_maior += 1
    else:
        de_menor += 1
print('_' * 50)

print('Existem \033[1m{}\033[m que \033[1;4mjá\033[m atingiram a maioridade.'.format(de_maior))
print('Existem \033[1m{}\033[m que ainda \033[1;4mnão\033[m chegaram à maioridade.'.format(de_menor))

print('=' * 50)
print('Fim do programa.')
