# estados/menu.py
import pygame
from config import LARGURA, ALTURA, BRANCO, PRETO, VERMELHO, FONTE

class Menu:
    def __init__(self):
        self.botao = pygame.Rect(
            LARGURA // 2 - 100,
            ALTURA // 2 - 30,
            200,
            60
        )
        self.ativo = False   # foco (teclado)
        self.iniciar = False

    def evento(self, evento):
        # Mouse
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if evento.button == 1 and self.botao.collidepoint(evento.pos):
                self.iniciar = True

        # Teclado
        if evento.type == pygame.KEYDOWN:
            if evento.key in (pygame.K_RETURN, pygame.K_SPACE):
                self.iniciar = True

    def desenhar(self, tela):
        tela.fill(PRETO)

        mouse_pos = pygame.mouse.get_pos()
        hover_mouse = self.botao.collidepoint(mouse_pos)

        # Ativo se mouse em cima OU foco por teclado
        ativo = hover_mouse or self.ativo

        cor = VERMELHO if ativo else BRANCO

        pygame.draw.rect(tela, cor, self.botao, 2)

        texto = FONTE.render("INICIAR", True, cor)
        texto_rect = texto.get_rect(center=self.botao.center)
        tela.blit(texto, texto_rect)
