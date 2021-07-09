'''Crie um programa que mostre na tela todos os números
pares que estão no intervalo entre 1 e 50.'''
print('=' * 50)
print((' ' * 10), 'Programa \033[1;4mDESAFIO47\033[m iniciado.')
print('=' * 50)

print('Mostrar todos os pares no intervalo 1 a 50.')
for i in range(1, 51):
    if (i % 2 == 0):
        print(i)

print('=' * 50)
print('Fim do programa.')
