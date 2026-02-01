import pygame
import sys

from config import *
from menu import Menu
from historia import Historia

pygame.init()
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Nothing's About to Happen to Me")
clock = pygame.time.Clock()

fonte_titulo = pygame.font.Font("mago1.ttf", 60)
fonte_botao = pygame.font.Font("mago1.ttf", 32)

menu = Menu(fonte_titulo, fonte_botao)
historia = Historia()

estado = "menu"
fade_alpha = 0
fade_velocidade = 2

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if estado == "menu":
            menu.evento(evento)

        elif estado == "jogo":
            historia.evento(evento)

    #ATUALIZAÇÃO
    if estado == "menu":
        if menu.acao == "iniciar":
            historia = Historia()
            fade_alpha = 0
            estado = "jogo"

        elif menu.acao == "sair":
            pygame.quit()
            sys.exit()

    elif estado == "jogo":
        historia.atualizar()

        if historia.finalizada:
            fade_alpha = 0
            estado = "fade"

    elif estado == "fade":
        fade_alpha += fade_velocidade
        if fade_alpha >= 255:
            fade_alpha = 255
            menu.acao = None
            estado = "menu"

    #DESENHO 
    tela.fill(PRETO)

    if estado == "menu":
        menu.desenhar(tela)

    elif estado == "jogo":
        historia.desenhar(tela)

    elif estado == "fade":
        historia.desenhar(tela)

        fade = pygame.Surface((LARGURA, ALTURA))
        fade.fill((0, 0, 0))
        fade.set_alpha(fade_alpha)
        tela.blit(fade, (0, 0))

    pygame.display.flip()
    clock.tick(FPS)
