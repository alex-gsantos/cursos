'''
Crie um programa onde o usuário possa digitar cinco
valores numéricos e cadastre-os em uma lista, já na
posição correta de inserção(sem usar o sort()). No final,
mostre a lista ordenada na tela.
SUGESTÃO DO PROFESSOR: Crie a lista inteira primeiro, depois
arrume elas.
'''
print('=' * 50)
print((' ' * 10), 'Programa \033[1;4mDESAFIO80\033[m iniciado.')
print('=' * 50)

lista1 = []
for cont in range(0, 5):
    aux = int(input('Digite um número: '))
    lista1.append(aux)
print('_' * 50)

lista2 = lista1[:]
lista3 = []
maior = [0]
operador = 0
aux = len(lista1)
while operador <= aux:
    for cont in range(0, (len(lista1))):
        if lista1[cont] <= lista2[0]:
            maior.insert(0, lista1[cont])

    lista3.append(maior[0])
    lista1.remove(maior[0])
    lista2.remove(maior[0])

    if len(lista1) == 0:
        operador = 10

print(lista3)

print('=' * 50)
print('Fim do programa.')

''' 17 LINHAS! AY, CARAMBA!
cont = 0
cont3 = 0
aux1 = 1
aux2 = 1
while aux1 == 1 and cont3 <= len(lista1):
    cont2 = 0
    while aux2 == 1 and cont2 <= len(lista1):
        if lista1[cont] >= lista1[cont2]:
            aux2 = 1
            cont2 += 1
        else:
            lista1.insert(cont2, lista1[cont])
            lista1.remove(lista1[cont])
            aux2 = 0
    aux2 == 1
    cont3 += 1

print(lista1)
'''
