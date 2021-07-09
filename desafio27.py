'''Faça um programa que leia o nome completo de uma pessoa
mostrando em seguida o primeiro e o último nome separadamente
Ex.: Ana Maria de Souza
primeiro = Ana
ultimo = Souza'''
print('=' * 50)
print((' ' * 10), 'Programa \033[1;4mDESAFIO27\033[m iniciado.')
print('=' * 50)

nome = str(input('Digite seu nome completo: '))
separar = nome.split()
#Para saber quantas posições(elementos) existem numa lista depois
# de usar o comando "split", usa-se o comando "len(nome)", onde
#'nome' é o nome da variável que contém a lista dos elementos
#separados.
print('Seu \033[4mprimeiro\033[m nome é: \033[36m{}\033[m.'
      .format(separar[0]))
print('O seu \033[4múltimo\033[m nome é: \033[36m{}\033[m.'
      .format(separar[len(separar) - 1]))

print('=' * 50)
print('Fim do programa.')
