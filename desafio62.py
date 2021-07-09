'''Melhore o DESAFIO61, perguntando para o usuário se ele
quer mostrar mais alguns termos. O programa encerra
quando ele disse que quer mostrar 0 termos.'''
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
        print('{', aux, '}')
    else:
        while resposta2 != 0:
            while cont <= termos:
                if cont == 1:
                    print('{', aux, ',', end='')
                else:
                    aux += razao
                    if cont == termos:
                        print(aux, '}')
                    else:
                        print(aux, ',', end='')
                cont += 1
            resposta2 = int(input('Quantos termos mais você quer ver? (digite 0 para encerrar)\n'))
            if resposta2 != 0:
                termos += resposta2
                print('{', end='')
    resposta1 = str(input('Você deseja continuar?[S/N]\n')).upper()
