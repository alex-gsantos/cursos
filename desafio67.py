'''Faça um programa que mostre a tabuada de vários
números, um de cada vez, para cada valor digitado pelo
usuário. O programa será interrompido quando o número
solicitado for negativo.'''
print('=' * 50)
print('Programa \033[4mDESAFIO67\033[m iniciado. Digite um \033[31mnúmero negativo\033[m para \033[31msair\033[m.')
print('=' * 50)


resposta = str(input('Você quer ver a tabuada de algum número? \033[31m[S/N]\033[m\n')).upper()
while resposta == 'S':
    num = 1
    while num > 0:
        print('_' * 50)
        print('\033[4;31mDigite um número negativo para sair.\033[m')
        num = int(input('Digite um número: '))
        if num < 0:
            break
        else:
            print(f'Tabuada do \033[36m{num}\033[m.')
            for cont in range(1,11):
                print(f'\033[36m{cont} x {num}\033[m = \033[33m{cont * num}\033[m')
            print('_' * 50)
    resposta = str(input('Você deseja continuar?\033[31m[S/N]\033[m\n')).upper()

print('=' * 50)
print('Programa encerrado.')
