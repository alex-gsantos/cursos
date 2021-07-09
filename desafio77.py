'''Crie um programa que tenha uma tupla com várias
palavras(não usar acentos). Depois disso, você deve
mostrar, para cada palavra,  quais são suas vogais.'''
print('=' * 50)
print(' ' * 10, 'Programa \033[1;4mDESAFIO76\033[m iniciado.')
print('=' * 50)

palavras = ('bombeiros', 'livro', 'gato', 'caderno', 'estudar', 'ratazana')

a = 'a'
e = 'e'
i = 'i'
o = 'o'
u = 'u'

for cont in palavras:
    aux1 = cont.count('a')
    aux2 = cont.count('e')
    aux3 = cont.count('i')
    aux4 = cont.count('o')
    aux5 = cont.count('u')
    #não existe comando para mostrar as vogais, então é preciso criar variáveis e fazer
    # comparações booleanas com o que eu quero que apareça na tela
    print(f'As vogais de "\033[35m{cont}\033[m" são:', end='')
    if aux1 > 0:
        print((f' \033[36m{a}\033[m') * aux1, end='')
    if aux2 > 0:
        print((f' \033[36m{e}\033[m') * aux2, end='')
    if aux3 > 0:
        print((f' \033[36m{i}\033[m') * aux3, end='')
    if aux4 > 0:
        print((f' \033[36m{o}\033[m') * aux4, end='')
    if aux5 > 0:
        print((f' \033[36m{u}\033[m') * aux5, end='')
    print()

print('=' * 50)
print('Fim do programa.')
