'''Desenvolva um programa que leia as duas notas de um aluno
e mostre a media.'''
print('=' * 50)
print((' ' * 10), 'Programa \033[1;4mDESAFIO07\033[m iniciado.')
print('=' * 50)

nota1 = float(input('Digite a nota do primeiro bimestre: '))
nota2 = float(input('Digite a nota do segundo bimestre: '))
media = (nota1 + nota2) / 2
print('_' * 50)
print('A média de suas notas é: \033[46m{}\033[m!'.format(media))

print('=' * 50)
print('Fim do programa.')
