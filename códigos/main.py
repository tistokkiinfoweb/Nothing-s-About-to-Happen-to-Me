# main.py
import pygame
import sys

from config import *
from menu import Menu
from historia import Historia
from movimento import Exploracao

pygame.init()
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("ADVENTURE CAT")
clock = pygame.time.Clock()

estado_atual = "menu"

menu = Menu()
historia = Historia()
exploracao = Exploracao()

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
        estado_atual = "exploracao"

    if estado_atual == "historia":
        historia.atualizar()
        if historia.finalizada:
            estado_atual = "exploracao"

    elif estado_atual == "exploracao":
        exploracao.atualizar()

    # DESENHO
    if estado_atual == "menu":
        menu.desenhar(tela)

    elif estado_atual == "historia":
        tela.fill(FUNDO_HISTORIA)
        historia.desenhar(tela)

    elif estado_atual == "exploracao":
        tela.fill(FUNDO_EXPLORACAO)
        exploracao.desenhar(tela)

    pygame.display.flip()
    clock.tick(FPS)
