# utils/texto.py
import pygame
from config import PRETO, BRANCO, FONTE

class TextoDigitado:
    def __init__(self, velocidade=15):
        self.velocidade = velocidade
        self.texto_completo = ""
        self.texto_visivel = ""
        self.indice = 0
        self.ultimo_tempo = pygame.time.get_ticks()

    def iniciar(self, texto):
        self.texto_completo = texto
        self.texto_visivel = ""
        self.indice = 0
        self.ultimo_tempo = pygame.time.get_ticks()

    def atualizar(self):
        agora = pygame.time.get_ticks()
        if self.indice < len(self.texto_completo):
            if agora - self.ultimo_tempo > 1000 // self.velocidade:
                self.texto_visivel += self.texto_completo[self.indice]
                self.indice += 1
                self.ultimo_tempo = agora

    def terminou(self):
        return self.indice >= len(self.texto_completo)

    def desenhar(self, tela):
        caixa = pygame.Rect(50, 400, 700, 150)
        pygame.draw.rect(tela, PRETO, caixa)
        pygame.draw.rect(tela, BRANCO, caixa, 2)

        render = FONTE.render(self.texto_visivel, True, BRANCO)
        tela.blit(render, (70, 430))
