'''Crie um programa que leia vários números inteiros
pelo teclado. No final da execução, mostre a média
entre todos os valores e qual foi o maior e o menor
valores lidos. O programa deve perguntar ao usuário
se ele quer ou não continuar a digitar valores.'''
print('=' * 50)
print((' ' * 10), 'Programa DESAFIO65 iniciado.')
print('=' * 50)

resposta = 'S'
cont = 0
soma = 0
while resposta == 'S':
    n1 = int(input('Digite um número inteiro: '))
    if cont == 0:
        maior = n1
        menor = n1
    else:
        if n1 > maior:
            maior = n1
        if n1 < menor:
            menor = n1
    soma += n1
    cont += 1
    resposta = str(input('Deseja continuar?[S/N]\n')).upper()
print('_' * 50)
print('A média entre os valores é \033[33m{:.2f}\033[m.\n'
      'O maior valor lido foi o \033[33m{}\033[m, e o menor \033[33m{}\033[m.'
      .format((soma / cont), maior, menor))

print('=' * 50)
print('Fim do programa.')
