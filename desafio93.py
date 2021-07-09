'''
Crie um programa que gerencie o aproveitamento de um
jogador de futebol. O programa vai ler o nome do jogador
e quantas partidas ele jogou. Depois vai ler a quantidade
de gols feitos em cada partida. No final, tudo isso será
guardado em um dicionario, incluindo o total de gols
feitos durante o campeonato.
'''
nome = 0
nomes = {}
num_partidas = 0
gols = []
catalogo = []
resumo = {}

n1 = 1
gols_total = 0
nome = str(input('Digite o nome do jogador: '))
num_partidas = int(input('Digite o número de partidas: '))
while n1 <= num_partidas:
    aux = int(input(f'Gols da partida {n1}: '))
    gols_total += aux
    gols.append(f'Gols da partida {n1}: {aux}')
    n1 += 1

resumo = {'partidas': num_partidas, 'gols_partida': gols, 'total_gols': gols_total}
lista_nomes = {'nome': nome, 'aproveitamento': resumo}

catalogo.append(lista_nomes)
print(catalogo)
print(catalogo[0]['aproveitamento'])