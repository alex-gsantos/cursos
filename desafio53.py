'''Crie um programa que leia uma frase qualquer e diga se
ela é um palíndromo, desconsiderando os espaços.
split
join
comparar strings'''
print('=' * 50)
print((' ' * 10), 'Programa \033[1;4mDESAFIO53\033[m iniciado.')
print('=' * 50)

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''

for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
    #a variável "inverso" vai receber letra por letra a frase
    #que está tudo junto(variável "junto")
print(junto, inverso)

print('=' * 50)
print('Fim do programa.')
