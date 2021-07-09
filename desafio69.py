'''Crie um programa que leia a idade e o sexo de várias
pesoas. A cada pessoa cadastrada, o programa deverá
perguntar se o usuário quer ou não continuar. No final,
mostre:
A) quantas pessoas tem mais de 18 anos
B) quantos homens foram cadastrados
C) quantas mulheres tem menos de 20 anos'''
print('=' * 50)
print((' ' * 10), 'Programa \033[1;4mDESAFIO69\033[m iniciado.')
print('=' * 50)

resposta = 'S'
cont_maioridade = 0
cont_homens = 0
cont_mulheres = 0
while resposta == 'S':
    print('_' * 50)
    idade = int(input('Digite a idade da pessoa: '))
    sexo = str(input('Digite o sexo da pessoa [M/F]: ')).upper()
    if idade >= 18:
        cont_maioridade += 1
    if sexo == 'M':
        cont_homens += 1
    if sexo == 'F':
        if idade < 20:
            cont_mulheres += 1
    resposta = str(input('Deseja continuar o programa?[S/N]\n')).upper()

print('_' * 50)
print(f'A) Existem \033[1;32m{cont_maioridade}\033[m pessoa(s) com mais de 18 anos.\n'
      f'B) Foram cadastrado(s) \033[1;32m{cont_homens}\033[m homem(ns).\n'
      f'C) Foram cadastrada(s) \033[1;32m{cont_mulheres}\033[m mulher(es) com menos de 20 anos.')

print('=' * 50)
print('Fim do programa.')