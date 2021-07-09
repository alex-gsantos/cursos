'''Crie um programa que leia duas notas de um aluno e calcule
sua média, mostrando uma mensagem no final, de acordo
com a média atingida:
- Média abaixo de 5.0: REPROVADO
- Média entre 5.0 e 6.9: RECUPERAÇÃO
- Média de 7.0 ou superior: APROVADO'''
print('=' * 50)
print((' ' * 10), 'Programa \033[1;4mDESAFIO40\033[m iniciado.')
print('=' * 50)

print('Vamos realizar sua avaliação anual.')
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2

if media < 5:
    print('Sua média é de \033[31m{:.2f}\033[m, abaixo de 5.0 pontos. Está \033[1mreprovado\033[m. \033[1m:(\033[m'
          .format(media))
elif 5 <= media <7:
    print('Sua média é de \033[33m{:.2f}\033[m. Está de recuperação, estude mais. \033[1m:)\033[m'
          .format(media))
else:
    print('Parabéns! Sua média é \033[32m{:.2f}\033[m, está \033[1maprovado!\033[m \033[1m*_*\033[m'
          .format(media))

print('=' * 50)
print('Fim do programa.')
