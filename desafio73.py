'''Crie uma tupla preenchida com os 20 primeiros
colocados da tabela do Campeonato brasileiro de
futebol, na ordem de colocação. Depois mostre:
A) apenas os 5 primeiros colocados
B) os últimos 4 colocados da tabela
C) uma lista com os times em ordem alfabética
D) em que posição na tabela está o time da Chapecoense'''
print('=' * 50)
print((' ' * 10), 'Programa \033[1;4mDESAFIO72\033[m iniciado.')
print('=' * 50)

colocacao = ('Flamengo', 'Santos', 'Palmeiras', 'Gremio', 'AtleticoPR', 'Sao Paulo', 'Internacional', 'Corinthians', 'Fortaleza'
             , 'Goias', 'Bahia', 'Vasco', 'AtleticoMG', 'Fluminense', 'Botafogo', 'Ceara', 'Cruzeiro', 'CSA', 'Chapecoense', 'Avai')
print('\033[33mOs cinco primeiros times na tabela do Campeonato Brasileiro de Futebol:\033[m')
for cont in range(1, 6):
    if cont == 5:
        print(colocacao[cont])
        break
    print(colocacao[cont], ', ', end='')
print('_' * 50)
print('\033[32mOs quatro últimos da colocação são:\033[m')
print(colocacao[-4:])
print('_' * 50)

print('\033[36mOs times em ordem alfabética:\033[m')
b = sorted(colocacao)
print(b)


print('_' * 50)
cont = 0
for cont in range(1, 20):
    if colocacao[cont] == 'Chapecoense':
        print(f'\033[34mChapecoense está na posição {cont + 1}.\033[m')

print('=' * 50)
print('Fim do programa.')
