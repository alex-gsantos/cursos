'''Crie um algooritmo que leia um número e mostre o seu dobro,
triplo e raiz quadrada.'''
print('=' * 50)
print((' ' * 10), 'Programa \033[1;4mDESAFIO06\033[m iniciado.')
print('=' * 50)

num = int(input('Digite um número: '))
dobro = num * 2
triplo = num * 3
raiz = num ** (1/2)
print('_' * 50)

print('O dobro de \033[7m{}\033[m é \033[4m{}\033[m,\n'
      'O triplo de \033[7m{}\033[m é \033[4m{}\033[m,\n'
      'A raiz quadrada de \033[7m{}\033[m é \033[4m{:.2f}\033[m.'
      .format(num, dobro, num, triplo, num, raiz))

print('=' * 50)
print('Fim do programa.')
