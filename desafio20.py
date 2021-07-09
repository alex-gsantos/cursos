'''O mesmo professor do desafio anterior quer sortear a ordem
de apresentação de trabalhos. Faça um programa que leia o
nome dos quatro alunos e mostre a ordem sorteada.'''
print('=' * 50)
print((' ' * 10), 'Programa \033[1;4mDESAFIO20\033[m iniciado.')
print('=' * 50)

import random
aluno1 = str(input('Aluno \033[4m1\033[m: '))
aluno2 = str(input('Aluno \033[4m2\033[m: '))
aluno3 = str(input('Aluno \033[4m3\033[m: '))
aluno4 = str(input('Aluno \033[4m4\033[m: '))
#posso fazer uma lista
lista = [aluno1, aluno2, aluno3, aluno4]
#posso usar o método RANDOM para embaralhar uma lista
random.shuffle(lista)
print('_' * 50)

print('A ordem de apresentação será:')
#agora a lista está embaralhada, então posso colocá-la no print
print('\033[34m', lista, '\033[m')

print('=' * 50)
print('Fim do programa.')
