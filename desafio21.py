'''Faça um programa em Python que abra e reproduza o áudio
de um arquivo mp3.'''
print('=' * 50)
print((' ' * 10), 'Programa \033[1;4mDESAFIO21\033[m iniciado.')
print('=' * 50)

print('\033[1mO DESAFIO21 pede para reproduzir um áudio utilizando linguagem Python.\n'
      'A música escolhida foi a música de abertura do desenho Bucky.\033[m')

import pygame
pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('desafio21.mp3')
pygame.mixer.music.play()
pygame.event.wait()

print('=' * 50)
print('Fim do programa.')