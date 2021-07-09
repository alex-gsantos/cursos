'''
Crie um programa onde 4 jogadores joguem um dado e
tenham resultados aleatórios. Guarde esses
resultados em um dicionario. No final, coloque esse
dicionario em ordem, sabendo que o vencedor tirou o
maior numero no dado.
'''
import random
lista = {}
l_nome = list()
l_num = list()
n1 = 0
while n1 < 4:
    aux = random.randint(1, 6)
    l_nome.append(f'Jogador {n1}')
    l_num.append(aux)
    n1 += 1



lista = {'Nome:': l_nome, 'Dado:': l_num}
print(lista)








'''
n1 = 0
while n1 < 3:
    n2 = 0
    aux1 = l_num[n2]
    nom1 = l_nome[n2]
    aux2 = l_num[n2 + 1]
    nom2 = l_nome[n2 + 1]
    if aux1 > aux2:
        while aux1 > aux2:
            l_num.append(aux1)
            l_num.remove(aux1)
            l_nome.append(nom1)
            l_nome.remove(nom1)
        n2 += 1
    n1 += 1

lista = {'Nome:': l_nome, 'Dado:': l_num}
print(lista)


n1 = 0
n2 = 0
while n1 < 4:
    print(f'Nome: {lista["Nome:"][n1]}')
    print(f'Dado: {lista["Dado:"][n1]}')
    n1 += 1

#l_nome.clear()
#l_num.clear()
l_num_aux = l_num[:]
l_nome_aux = list()
n1 = 0
while n1 < 4:
    n2 = 0
    aux1 = l_num[n1]
    aux2 = l_num_aux[n2]
    while n2 < 4:
        if aux1 > aux2:
            aux3 = aux2
            l_num_aux[n2] = aux1
            l_num_aux[n1] = aux3
        n2 += 1
        
    n1 += 1
print(l_num)
#fazer uma lista ao contrário, onde os números tem um conteúdo, que é os Jogadores.
#sortear de modo reverso os números

print(l_nome)
print(l_num)
print(lista)
lista = {'Jogador': l_nomes, 'Numero': }
'''