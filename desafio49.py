'''Refaça o DESAFIO09, mostrando a tabuada de um número
que o usuário escolher, só que agora utilizando um
laço for.'''
print('=' * 50)
print((' ' * 10), 'Programa \033[1;4mDESAFIO49\033[m iniciado.')
print('=' * 50)

num = int(input('Digite um número: '))
print('_' * 50)

print(f'\033[1mTabuada do {num}\033[m')
for i in range(1, 11):
    print('\033[36m{}\033[m x {} = \033[36m{}\033[m'.format(i, num, (i * num)))

print('=' * 50)
print('Fim do programa.')
