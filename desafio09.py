'''Faça um programa que leia um número Inteiro qualquer e mostre
a sua tabuada.'''
print('=' * 50)
print((' ' * 10), 'Programa \033[1;4mDESAFIO09\033[m iniciado.')
print('=' * 50)

num = int(input('Digite um número: '))
#posso usar variáveis para guardar códigos de cores e formatos
f = '\033[m'
l = {'vt':'\033[32m'}
print('_' * 50)
print(f'Tabuada do número \033[4m{num}\033[m:')
print('{}{}{} x 1 = {}{}'.format(l['vt'], num, f, l['vt'], num*1))
print('{}{}{} x 2 = {}{}'.format(l['vt'], num, f, l['vt'], num*2))
print('{}{}{} x 3 = {}{}'.format(l['vt'], num, f, l['vt'], num*3))
print('{}{}{} x 4 = {}{}'.format(l['vt'], num, f, l['vt'], num*4))
print('{}{}{} x 5 = {}{}'.format(l['vt'], num, f, l['vt'], num*5))
print('{}{}{} x 6 = {}{}'.format(l['vt'], num, f, l['vt'], num*6))
print('{}{}{} x 7 = {}{}'.format(l['vt'], num, f, l['vt'], num*7))
print('{}{}{} x 8 = {}{}'.format(l['vt'], num, f, l['vt'], num*8))
print('{}{}{} x 9 = {}{}'.format(l['vt'], num, f, l['vt'], num*9))
print('{}{}{} x 10 = {}{}'.format(l['vt'], num, f, l['vt'], num*10), f)

print('=' * 50)
print('Fim do programa.')
