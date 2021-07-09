'''Faça um programa que leia o ano de um jovem e informe,
de acordo com sua idade:
- Se ele ainda vai se alistar ao serviço militar
- Se é hora de se alistar
- Se já passou do tempo do alistamento
Seu programa também deverá mostrar o tempo que falta ou
que passou do prazo.'''
print('=' * 50)
print((' ' * 10), 'Programa \033[1;4mDESAFIO39\033[m iniciado.')
print('=' * 50)

idade = int(input('Bem vindo ao 42º Regimento, soldado. Qual é a sua idade?\n'))
if idade < 18:
    print('Você ainda é jovem, recruta! Volte daqui a \033[36m{}\033[m anos.'
          .format(18 - idade))
elif idade == 18:
    print('Hora de se alistar, cadete! Vá buscar seu fuzil e entre logo na fila!!!')
else:
    print('Seu tempo de alistamento já passou em \033[36m{}\033[m ano(s), meu caro veterano. Volte para casa.'
          .format(idade - 18))

print('=' * 50)
print('Fim do programa.')
