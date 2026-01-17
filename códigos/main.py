import pygame
import sys

from config import *
from menu import Menu
from historia import Historia

pygame.init()
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Nothing's About to Happen to Me")
clock = pygame.time.Clock()

fonte_titulo = pygame.font.Font("mago3.ttf", 60)
fonte_botao = pygame.font.Font("mago3.ttf", 32)

menu = Menu(fonte_titulo, fonte_botao)
historia = Historia()

estado = "menu"

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if estado == "menu":
        menu.evento(evento)
    elif estado == "jogo":
            historia.evento(evento)

    if estado == "menu":
        if menu.acao == "iniciar":
            estado = "jogo"
        if menu.acao == "sair":
            pygame.quit()
            sys.exit()

        menu.desenhar(tela)

    elif estado == "jogo":
        historia.atualizar()
        historia.desenhar(tela)

        pygame.display.flip()
        clock.tick(60)
            
    elif estado == "jogo":
        historia.evento(evento)

    if estado == "menu":
        if menu.acao == "iniciar":
            estado = "jogo"

        elif menu.acao == "sair":
            pygame.quit()
            sys.exit()

    elif estado == "historia":
        historia.evento(evento)
    if historia.finalizada:
        estado = "menu"

    if estado == "historia":
        historia.atualizar()
        if historia.finalizada:
            estado6 = "menu"

    # DESENHO
    if estado == "menu":
        menu.desenhar(tela)

    elif estado == "jogo":
        historia.atualizar()
        historia.desenhar(tela)

    pygame.display.flip()
    clock.tick(FPS)

