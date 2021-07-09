'''
Crie um programa que leia nome, sexo e idade de várias
pessoas, guardando os dados de cada pessoa em um dicionário
 e todos os dicionarios em uma lista. No final, mostre:
A) quantas pessoas foram cadastradas
B) a media de idade do grupo
C) uma lista com todas as mulheres
D) uma lista com todas as pessoas com idade acima da média
'''
qntde = 0
idade_total = 0
dicionario = {}
lista_nomes = {}
lista_mulheres = []
idade_acima = []
resposta = 'S'
resumo = []
idade_acima = []

while resposta == 'S':
    nome = str(input('Digite o nome: '))
    sexo = str(input('Digite o sexo: [M/F]')).upper()
    if sexo == 'F':
        lista_mulheres.append(nome)
    idade = int(input('Digite a idade: '))
    idade_total += idade
    qntde += 1
    lista_nomes = {'nome': nome, 'sexo': sexo, 'idade': idade}
    resumo.append(lista_nomes)
    resposta = str(input('Deseja continuar? [S/N]')).upper()

idade_total = idade_total // qntde
aux1 = 0
aux2 = 0
while aux1 < qntde:
    aux2 = resumo[aux1]["idade"]
    if aux2 > idade_total:
        idade_acima.append(resumo[aux1]["nome"])
    aux1 += 1

dicionario = {'todos': resumo, 'lista_mulheres': lista_mulheres, 'idade_acima': idade_acima}

print('_' * 50)
print(f'Foram cadastradas {qntde} pessoas.')
print('A média das idades é {:.2f}'.format(idade_total))
print('Lista das mulheres: ', dicionario["lista_mulheres"])
print('Pessoas acima da media de idade: ', dicionario["idade_acima"])
