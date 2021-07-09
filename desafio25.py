'''Crie um programa que leia o nome de uma pessoa e diga se
ela tem "Silva" no nome'''
print('=' * 50)
print((' ' * 10), 'Programa \033[DESAFIO25 iniciado.')
print('=' * 50)

nome = str(input('Digite um nome: '))
print('Existe "Silva" no nome?\033[33m', 'Silva' in nome, '\033[m')

print('=' * 50)
print('Fim do programa.')
