'''Refaça o DESAFIO51, lendo o primeiro termo e a razão
de uma PA, mostrando os 10 primeiros termos da progressão
usando a estrutura WHILE.'''
print('Iniciando programa.')
resposta1 = 'S'
while resposta1 == 'S':
    primeiro_termo = int(input('Informe o primeiro termo: '))
    razao = int(input('Informe a razao: '))
    termos = int(input('Quantos termos você quer ver?\n'))
    aux = primeiro_termo
    cont = 1
    resposta2 = 1
    if termos == 1:
        print('\033[33m{', aux, '}')
    else:
        while resposta2 != 0:
            while cont <= termos:
                if cont == 1:
                    print('\033[34m{', aux, ',', end='')
                else:
                    aux += razao
                    if cont == termos:
                        print(aux, '}\033[m')
                    else:
                        print(aux, '\033[34m,', end='')
                cont += 1
            resposta2 = int(input('Quantos termos mais você quer ver? (digite 0 para encerrar)\n'))
            if resposta2 != 0:
                termos += resposta2
                print('\033[34m{', end='')
    resposta1 = str(input('Você deseja continuar?[S/N]\n')).upper()
