'''Faça um programa que leia o nome de uma pessoa e mostre
uma mensagem de boas-vindas.'''
print('=' * 50)
print((' ' * 10), 'Programa \033[1;4mDESAFIO02\033[m iniciado.')
print('=' * 50)

#a função INPUT() serve para ler um valor do teclado(do usuário)
nome = input('Digite seu nome: ')
print('_' * 50)
#dentro do PRINT eu posso misturar variáveis e frases, que nem no java
print('Seja bem vindo,', '\033[32m', nome, '\033[m', '!')

print('=' * 50)
print('Fim do programa.')
