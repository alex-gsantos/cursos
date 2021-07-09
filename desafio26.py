'''Faça um programa que leia uma frase pelo teclado e mostre:
- Quantas vezes aparece a letra "A"
- Em que posição ela aparece a primeira vez
- Em que posição ela aparece a última vez'''
print('=' * 50)
print((' ' * 10), 'Programa \033[1;4mDESAFIO26\033[m iniciado.')
print('=' * 50)

frase = str(input('Digite uma frase: ')).upper()
#utilizei a função upper() para considerar todas as letras como A maiúsculo
cont = frase.count('A')
print('A letra \033[35m"A"\033[m aparece \033[35m',
      (frase.count('A')), '\033[mvez(es).' )
print('A primeira letra \033[35m"A"\033[m aparece na '
      'posição \033[35m', frase.find('A'), '\033[m')
print('A última letra \033[35m"A"\033[m aparece na '
      'posição \033[35m', frase.rfind('A'), '\033[m')

print('=' * 50)
print('Fim do programa.')
