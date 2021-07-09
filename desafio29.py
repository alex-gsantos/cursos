'''Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que
ele foi multado.
A multa vai custar R$ 7,00 por cada Km acima do limite.'''
print('=' * 50)
print((' ' * 10), 'Programa \033[1;4mDESAFIO29\033[m iniciado.')
print('=' * 50)

velocidade = int(input('Digite a velocidade que o carro passou: '))
if velocidade <= 80:
    print('\033[34mFique tranquilo, você não infringiu a lei.\033[m')
else:
    vel = velocidade - 80
    multa = vel * 7
    print('Você estava \033[4m{}Km/h\033[m \033[1;31mACIMA\033[m do '
          'limite de velocidade. Pagará uma \033[31mmulta\033[m '
          'de \033[31mR$ {:.2f}\033[m.'.format(vel, multa))

print('=' * 50)
print('Fim do programa.')
