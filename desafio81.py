'''
Crie um programa que vai ler vários números e colocar em
uma lista. Depois disso, mostre:
A) quantos números foram digitados
B) a lista de valores ordenada de forma decrescente
C) se o valor 5 foi digitado e está ou não na lista
'''
print('=' * 50)
print((' ' * 10), 'Programa \033[1;4mDESAFIO81\033[m iniciado.')
print('=' * 50)

reposta = 'S'
lista = []
cont = 0
while reposta == 'S':
    num = int(input('Digite um número: '))
    lista.append(num)
    cont += 1
    reposta = str(input('Deseja continuar? [S/N]\n')).upper()
lista.sort(reverse=True)

print('_' * 50)
print(f'Foram digitados \033[32m{cont}\033[m números.')
print(f'Esta é a lista que foi criada: \033[32m{lista}\033[m')
if 5 in lista:
    print('O valor \033[32m"5"\033[m está na lista.')
else:
    print('O valor \033[32m"5"\033[m não está na lista.')

print('=' * 50)
print('Fim do programa.')
