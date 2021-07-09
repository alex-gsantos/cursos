'''Desenvolva uma lógica que leia o peso e a altura de uma
pessoa, calcule seu IMC e mostre seu status, de acordo
com a tabela abaixo:
- Abaixo de 18.5: abaixo do peso
- Entre 18.5 e 25: peso ideal
- 25 até 30: sobrepeso
- 30 até 40: obesidade
- Acima de 40: obesidade mórbida
IMC =  peso / altura ao quadrado'''
print('=' * 50)
print((' ' * 10), 'Programa \033[1;4mDESAFIFO43\033[m iniciado.')
print('=' * 50)

print('Olá. Vamos calcular o seu IMC, mas para isso precisamos de alguns dados.')
peso = float(input('Digite quanto você pesa (em Kg): '))
altura = float(input('Digite qual é a sua altura (em metros): '))
print('=' * 50)

imc = peso / (altura ** 2)
if imc < 18.5:
    print('Seu IMC é de \033[33m{:.2f}\033[m. Você está \033[33mabaixo\033[m do peso ideal.'.format(imc))
elif imc >= 18.5 and imc <= 25:
    print('Seu IMC é de \033[32m{:.2f}\033[m. Você está no peso ideal.'.format(imc))
elif imc > 25 and imc <= 30:
    print('Seu IMC é de \033[32m{:.2f}\033[m. Você está com \033[32msobrepeso\033[m. Vá queimar umas calorias.'.format(imc))
elif imc > 30 and imc <= 40:
    print('Seu IMC é de \033[31m{:.2f}\033[m. Você está com \033[31mobesidade\033[m. Melhor iniciar uma dieta rígida.'.format(imc))
else:
    print('Seu IMC é de \033[1;4;31m{:.2f}\033[m. \033[31mVocê está com\033[m \033[1;4;31mobesidade mórbida\033[m. Melhor morar no mar.'.format(imc))

print('=' * 50)
print('Fim do programa.')
