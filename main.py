import pygame
from pygame.locals import *
from sys import exit

pygame.init()


tela = pygame.display.set_mode([920,720])
pygame.display.set_caption('Adventure Cat')

fundo = pygame.image.load('')
tela.blit(fundo, (0,0))

fonte = pygame.font.SysFont('mago3', 100, False)
rodando = True

while rodando == True:
    mensagem = f'Adventure Cat'
    texto = fonte.render(mensagem, True, (255,255,255))
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            loop = False
            exit()
    
    tela.blit(texto, (180,160))
    pygame.display.flip()
