'''
Aprimore o DESAFIO93 para que ele funcione com v?rios
jogadores, incluindo um sistema de visualiza??o de
detalhes do aproveitamento de cada jogador.
'''

nome = 0
nomes = {}
num_partidas = 0
gols = []
catalogo = []
resumo = {}
resposta = 'S'

while resposta == 'S':
    n1 = 1
    gols_total = 0
    nome = str(input('Digite o nome do jogador: '))
    num_partidas = int(input('Digite o n?mero de partidas: '))
    while n1 <= num_partidas:
        aux = int(input(f'Gols da partida {n1}: '))
        gols_total += aux
        gols.append(f'Gols da partida {n1}: {aux}')
        n1 += 1

    resumo = {'partidas': num_partidas, 'gols_partida': gols, 'total_gols': gols_total}
    lista_nomes = {'nome': nome, 'aproveitamento': resumo}
    catalogo.append(lista_nomes)
    resposta = str(input('Deseja cadastrar mais um jogador? [S/N] ')).upper()

print('Nome: ', catalogo[0]["nome"])
print('N?mero de partidas: ', catalogo[0]["aproveitamento"]["partidas"])
print('Total de gols', catalogo[0]["aproveitamento"]["gols_partida"])

print('Nome: ', catalogo[1]["nome"])
print('N?mero de partidas: ', catalogo[1]["aproveitamento"]["partidas"])
print('Total de gols ', catalogo[1]["aproveitamento"]["gols_partida"])