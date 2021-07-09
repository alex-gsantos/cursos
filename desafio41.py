'''A Confederação Nacional de Natação precisa de um programa
que leia o ano de nascimento de um atleta e mostre sua
categoria, de acordo com a idade:
- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JUNIOR
- Até 20 anos: SÊNIOR
- Acima: MASTER'''
print('=' * 50)
print((' ' * 10), 'Programa \033[1;4mDESAFIO41\033[m iniciado.')
print('=' * 50)

print('Olá. Precisamos saber em qual categoria iremos colocá-lo. Por favor, informe sua idade: ')
idade = int(input())
if idade <= 9:
    print('Você foi inscrito na categoria \033[1;35mMIRIM\033[m.')
elif (idade > 9) and (idade <= 14):
    print('Você foi inscrito na categoria \033[1;35mINFANTIL\033[m.')
elif (idade > 14) and (idade <= 19):
    print('Você foi inscrito na categoria \033[1;35mJUNIOR\033[m.')
elif idade == 20:
    print('Você foi inscrito na categoria \033[1;35mSÊNIOR\033[m.')
else:
    print('Você foi inscrito na categoria \033[1;35mMASTER\033[m.')

print('=' * 50)
print('Fim do programa.')