'''Crie um programa que tenha uma tupla totalmente
preenchida com uma contagem por extenso, de zero até 20.
Seu programa deverá ler um número pelo teclado
(entre 0 e 20) e mostrá-lo por extenso.'''
print('=' * 50)
print((' ' * 10), 'Programa \033[1;4mDESAFIO72\033[m iniciado.')
print('=' * 50)

lista_num = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
             'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
num = int(input('Digite um número entre \033[33m0\033[m e \033[33m20\033[m: '))
while (num > 20) or (num < 0):
    print('O número deve estar no intervalo de \033[33m0\033[m a \033[33m20\033[m.')
    num = int(input('Digite um número: '))
print(f'O número \033[34m{num}\033[m por extenso fica \033[34m{lista_num[(num)]}\033[m.')

print('=' * 50)
print('Fim do programa.')
