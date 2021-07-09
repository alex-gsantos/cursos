'''Crie um programa que leia dois valores e mostre um
menu na tela:
[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa
Seu programa deverá realizar a operação solicitada em
cada caso.'''
print('=' * 50)
print((' ' * 10), 'Programa \033[1;4mDESAFIO59\033[m iniciado.')
print('=' * 50)

v1 = int(input('Digite um número: '))
v2 = int(input('Digite outro número: '))
a = 0
while a != 5:
    a = int(input('Digite o número da operação que você quer:\n'
                  '\033[33m[1]\033[m \033[31msomar\033[m\n'
                  '\033[33m[2]\033[m \033[32mmultiplicar\033[m\n'
                  '\033[33m[3]\033[m \033[34mmaior\033[m\n'
                  '\033[33m[4]\033[m \033[35mnovos números\033[m\n'
                  '\033[33m[5]\033[m sair\n'))
    if a == 1:
        print('A soma de \033[31m{}\033[m e \033[31m{}\033[m dá \033[31m{}\033[m.'
              .format(v1, v2, (v1 + v2)))
        print('_' * 50)
    elif a == 2:
        print('A multiplicação entre \033[32m{}\033[m e \033[32m{}\033[m dá \033[32m{}\033[m.'
              .format(v1, v2, (v1 * v2)))
        print('_' * 50)
    elif a == 3:
        if v1 > v2:
            print('\033[34m{}\033[m é o maior valor.'
                  .format(v1))
            print('_' * 50)
        else:
            print('\033[34m{}\033[m é o maior valor.'
                  .format(v2))
            print('_' * 50)
    elif a == 4:
        print('_' * 50)
        v1 = int(input('\033[35mNovos números.\033[m\nDigite um número: '))
        v2 = int(input('Digite outro número: '))
    elif a == 5:
        print('Fim das operações.')
    else:
        print('Essa opção não existe.')

print('=' * 50)
print('Fim do programa.')
