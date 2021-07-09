'''Um professor quer sortear um dos seus quatro alunos para
apagar o quadro. Faça um programa que ajude ele, lendo
os nomes deles e escrevendo o nome do escolhido.'''
print('=' * 50)
print((' ' * 10), 'Programa \033[1;4mDESAFIO19\033[m iniciado.')
print('=' * 50)

import random
aluno1 = input('Digite o nome do \033[4maluno 1\033[m: ')
aluno2 = input('Digite o nome do \033[4maluno 2\033[m: ')
aluno3 = input('Digite o nome do \033[4maluno 3\033[m: ')
aluno4 = input('Digite o nome do \033[4maluno 4\033[m: ')
print('_' * 50)
#O método random sorteia entre 0 a 1. Para que ele funcione,
#é preciso invocar o método e o tipo de dado do random
#inteiro, float, boolean, etc
#aleatorio = random.randint(1, 4)

#Uma outra maneira de se fazer é:
lista = [aluno1, aluno2, aluno3, aluno4]#tipo um array
#e randomizar uma escolha dentro dessa lista
aleatorio = random.choice(lista)
print('O aluno sorteado para apagar o quadro foi o(a) \033[1;4;7;37m{}\033[m.'.format(aleatorio))

print('=' * 50)
print('Fim do programa.')
