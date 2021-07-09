'''
Crie um programa que leia nome e duas notas de vários
alunos e guarde tudo em uma lista composta. No final,
mostre um boletim contendo a média de cada um e permita
que o usuário possa mostrar as notas de cada aluno
individualmente.
'''
print('=' * 50)
print((' ' * 10), 'Programa \033[1;4mDESAFIO89\033[m iniciado.')
print('=' * 50)

lista_notas = list()
lista_tudo = list()
lista_tudo2 = list()
resposta = 'S'
cont = 0
while resposta == 'S':
    nome = str(input('Digite o nome do aluno: '))
    nota1 = float(input('Digite a nota 1: '))
    nota2 = float(input('Digite a nota 2: '))

    cont += 1
    lista_notas.append(nota1)
    lista_notas.append(nota2)
    lista_tudo.append(nome)
    lista_tudo.append(lista_notas[:])
    lista_tudo2.append(lista_tudo[:])
    lista_notas.clear()
    lista_tudo.clear()

    resposta = str(input('Deseja continuar? [S/N]\n')).upper()

n1 = 0
n2 = 1

print('NOME', (' ' * 36), 'N1    N2  | MEDIA')
while n1 < cont:
    aux1 = lista_tudo2[n1][0]
    aux2 = len(aux1)
    aux3 = lista_tudo2[n1][1][0]
    aux4 = lista_tudo2[n1][1][1]
    media = (aux3 + aux4) / 2
    print(f'{lista_tudo2[n1][0]}', ('_' * (40 - aux2)), lista_tudo2[n1][1][0], '+', lista_tudo2[n1][1][1], '=', media)
    n1 += 1

print('=' * 50)
print('Fim do programa.')