# main.py
import pygame
import sys

from config import *
from menu import Menu
from historia import Historia

pygame.init()
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Nothing's About to Happen to Me")
clock = pygame.time.Clock()

estado_atual = "menu"

menu = Menu()
historia = Historia()

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if estado_atual == "menu":
        menu.evento(evento)

    if menu.iniciar:
        estado_atual = "historia"

    elif estado_atual == "historia":
        historia.evento(evento)
    if historia.finalizada:
        estado_atual = "menu"

    if estado_atual == "historia":
        historia.atualizar()
        if historia.finalizada:
            estado_atual = "menu"

    # desenhos base
    if estado_atual == "menu":
        menu.desenhar(tela)

    elif estado_atual == "historia":
        tela.fill(FUNDO_HISTORIA)
        historia.desenhar(tela)

    pygame.display.flip()
    clock.tick(FPS)
