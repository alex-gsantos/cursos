'''Faça um programa que leia o sexo de uma pessoa, mas só
aceite 'M' ou 'F'. Caso esteja errado, peça a digitação
novamente até ter um valor correto.'''
print('=' * 50)
print((' ' * 10), 'Programa \033[1;4mDESAFIO57\033[m iniciado.')
print('=' * 50)

resposta = str(input('Digite qual é o seu sexo [M/F]: ')).upper()
while resposta != 'M' and resposta != 'F':
    resposta = str(input('Você só pode escolher \033[33mM\033[m ou \033[33mF\033[m. Digite novamente: ')).upper()

print('=' * 50)
print('Fim do programa.')
