# estados/exploracao.py
import pygame
from config import FUNDO_EXPLORACAO, LARGURA, ALTURA

class Exploracao:
    def __init__(self):
        self.x = 400
        self.y = 400
        self.vel = 4

    def atualizar(self):
        teclas = pygame.key.get_pressed()

        if teclas[pygame.K_a]:
            self.x -= self.vel
        if teclas[pygame.K_d]:
            self.x += self.vel

        self.x = max(0, min(self.x, LARGURA - 40))


    def desenhar(self, tela):
        pygame.draw.rect(tela, (200, 200, 200), (self.x, self.y, 40, 40))
