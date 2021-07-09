'''Desenvolva um programa que leia o primeiro termo e a
razão de uma PA. No final, mostre os 10 primeiros
termos dessa progressão.'''
print('=' * 50)
print((' ' * 10), 'Programa \033[1;4mDESAFIO51\033[m iniciado.')
print('=' * 50)

primeiro_termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
print('_' * 50)

soma = primeiro_termo
print('Os 10 primeiros termos dessa PA são:')
for cont in range(1, 11):
    if cont == 10:
        print(soma)
        break
    print(soma, ',', end='')
    soma += razao
print()

print('=' * 50)
print('Fim do programa.')