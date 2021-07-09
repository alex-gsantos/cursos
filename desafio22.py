'''Crie um programa que leia o nome completo de uma pessoa e
mostre:
- o nome com todas as letras maiusculas
- o nome com todas minusculas
- quantas letras ao todo (sem considerar espaços)
- quantas letras tem o primeiro nome'''
print('=' * 50)
print((' ' * 10), 'Programa \033[1;4mDESAFIO22\033[m iniciado.')
print('=' * 50)

nome = str(input('Digite o seu nome completo: '))
print('_' * 50)

print('Usando a função \033[33m"nome.upper()"\033[m: \033[1;35m', nome.upper(), '\033[m')
print('Usando a função \033[33m"nome.lower()"\033[m: \033[1;35m', nome.lower(), '\033[m')
print('_' * 50)

nome2 = nome.split()
print('Utilizando a função \033[33m"split"\033[m: ', nome2)
nome3 = str(''.join(nome2))
print('Utilizando a função \033[33m"join"\033[m:', nome3)
print('_' * 50)

print('Contagem do total de caracteres: \033[35m', nome3.count('') - 1, '\033[m')
#CONTA QUANTOS CARACTERES TEM (total + 1)
#print(nome3)
print('Contagem de caracteres na posição 0(zero): \033[35m', nome2[0].count('') - 1, '\033[m')

print('=' * 50)
print('Fim do programa.')
