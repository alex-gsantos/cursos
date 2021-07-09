'''
Crie um programa que leia nome, ano de nascimento e
carteira de trabalho e cadastre-os(com idade) em um
dicionario se por acaso a CTPS for diferente de zero, o
dicionario receberá também o ano de contratação e o
salário. Calcule e acrescente, além da idade, com
quantos anos a pessoa vai se aposentar.
'''
catalogo = []
lista = {}
l_trabalho = {}
resposta = 'S'
cont = 0
ano_contrato = 0
sal = 0
aposentadoria = 0
while resposta == 'S':
    cont += 1
    nome = str(input('Digite o nome: '))
    nascimento = int(input('Digite o ano de nascimento: '))
    nascimento = 2020 - nascimento
    ctps = int(input('Digite o numero da CTPS (ou 0 se não tiver): '))
    if ctps == 0:
        aposentadoria = 0
        lista = {'nome': nome, 'nasceu': nascimento, 'carteira': aposentadoria}
    else:
        ano_contrato = int(input('Digite o ano de contratação: '))
        sal = float(input('Digite seu salário: R$ '))
        aposentadoria = 35 - (2020 - ano_contrato)
        if aposentadoria < 0:
            aposentadoria = 0
        l_trabalho = {'num_ctps': ctps, 'salario': sal, 'contrato': ano_contrato, 'aposenta': aposentadoria}
        lista = {'nome': nome, 'nasceu': nascimento, 'carteira': l_trabalho}

    catalogo.append(lista)
    resposta = str(input('Deseja continuar? [S/N] ')).upper()

print('_' * 50)
aux = 0
while aux < cont:
    print('Nome: ', catalogo[aux]['nome'])
    print('Idade: ', catalogo[aux]['nasceu'])
    if catalogo[aux]['carteira'] != 0:
        print('Ano de contrato: ', catalogo[aux]['carteira']['contrato'])
        print('Salario: ', catalogo[aux]['carteira']['salario'])
        print('Aposentadoria: ', catalogo[aux]['carteira']['aposenta'])
    else:
        print('Aposentadoria: ', catalogo[aux]['carteira'])
    print('-' * 30)
    aux += 1