'''#Desenvolva um programa que leia o nome, idade e sexo
de 4 pessoas. No final do programa, mostre:
- A média de idade do grupo
- Qual é o nome do homem mais velho
- Quantas mulheres têm menos de 21 anos'''
print('=' * 50)
print((' ' * 10), 'Programa \033[1;4mDESAFIO56\033[m iniciado.')
print('=' * 50)

soma = 0
mais_velho = 0
novas = 0
nome2 = 'vazio'

print('\033[1;4mDados das pessoas\033[m')
for cont in range(1,5):
    nome = str(input('Digite o nome da pessoa {}: '.format(cont)))
    idade = int(input('Digite a idade da pessoa {}: '.format(cont)))
    sexo = str(input('Digite o sexo da pesoa (M ou F) {}: '.format(cont)))
    print('-' * 37)
    soma += idade
    if cont == 1:
        if sexo == 'M':
            mais_velho = idade
            nome2 = nome
    else:
        if sexo == 'M':
            if idade > mais_velho:
                mais_velho = idade
                nome2 = nome
        else:
            if idade < 21:
                novas += 1
print('_' * 50)

print('A média das idades é \033[33m{}\033[m.\n'
      'O nome do homem mais velho é: \033[33m{}\033[m.\n'
      'A quantidade de mulheres abaixo de 21 é \033[33m{}\033[m.'
      .format((soma / 4), nome2, novas))

print('=' * 50)
print('Fim do programa.')
