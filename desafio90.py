'''
Faça um programa que leia o nome e média de um aluno,
guardando também a situação em um dicionario. No
final, mostre o conteúdo da estrutura na tela.
'''
lista = list()
l_nome = dict()
l_media = list()
l_situacao = list()
resposta = 'S'
cont = 0

while resposta == 'S':
    nome = input('Digite o nome: ')
    num = float(input('Digite a media: '))
    if num >=7:
        aux = ('Aprovado.')
    elif num < 7 and num >= 4:
         aux = ('Recuperação.')
    else:
        aux = ('Reprovado.')
    l_media.append(num)
    l_situacao.append(aux)
    l_nome = {'Aluno': nome[:], 'Media': l_media[:], 'Situacao': l_situacao[:]}
    #quando eu for criar um dicionario, preciso me referir ao "LABEL",
    #isto é, me referir ás chaves(Aluno, Media, etc). As chaves são os
    # nomes dos campos.
    lista.append(l_nome.copy())
    l_media.clear()
    l_situacao.clear()
    cont += 1
    resposta = str(input('Deseja continuar? [S/N] ')).upper()

print('_' * 50)
n1 = 0
#a primeira chave se refere a um elemento da "lista", que é uma list().
# A segunda chave se refere ao "l_nomes", que se refere a um dicionario.
while n1 < cont:
    print(f'\033[33mNome:\033[m {lista[n1]["Aluno"]}')
    print(f'\033[33mMédia\033[m: {lista[n1]["Media"][0]}')
    print(f'\033[33mSituação\033[m: {lista[n1]["Situacao"][0]}')
    n1 += 1
    print('_' * 50)

print('=' * 50)
print('Fim do programa.')