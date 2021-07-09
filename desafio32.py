'''Faça um programa que leia um ano qualquer e mostre se
ele é bissexto.'''
print('=' * 50)
print((' ' * 10), 'Programa \033[1;4mDESAFIO32\033[m iniciado.')
print('=' * 50)

ano = int(input('Digite o ano: '))
if ano % 100 == 0:
    if ano % 400 != 0:
        print(f'{ano} \033[11;4mnão\033[m é ano bissexto.')
if ano % 4 == 0:
    print(f'{ano} \033[1;4mé\033[m ano bissexto.')
else:
    print(f'{ano} \033[1;4mnão\033[m é ano bissexto.')

print('=' * 50)
print('Fim do programa.')
