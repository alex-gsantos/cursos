'''
Crie um programa onde o usuário digite uma expressão
qualquer que use parenteses. Seu aplicativo deverá
analisar se a expressão passada está com os parenteses
abertos e fechados na ordem correta.
'''
print('=' * 50)
print((' ' * 10), 'Programa \033[1;4mDESAFIO83\033[m iniciado.')
print('=' * 50)

expressao = str(input('Digite uma expressão: '))
aux1 = expressao.count('(')
aux2 = expressao.count(')')

if ((aux1 + aux2) % 2) != 0:
    if aux1 > aux2:
        print(f'Faltam \033[31m{aux1 - aux2}\033[m parenteses do lado direito \033[31m")"\033[m.')
    else:
        print(f'Faltam \033[31m{aux2 - aux1}\033[m parenteses do lado esquerdo \033[31m"("\033[m.')
else:
    print('A expressão está correta.')

print('=' * 50)
print('Fim do programa.')
