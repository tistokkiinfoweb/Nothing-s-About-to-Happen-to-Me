import pygame
from config import *

import pygame

class TextoDigitado:
    def __init__(self, texto):
        self.texto_completo = texto
        self.texto_atual = ""
        self.indice = 0
        self.velocidade = 30
        self.ultimo_tempo = pygame.time.get_ticks()
        self.fonte = pygame.font.Font("adicionais/fonte/mago1.ttf", 35)

    def atualizar(self):
        agora = pygame.time.get_ticks()
        if self.indice < len(self.texto_completo):
            if agora - self.ultimo_tempo >= self.velocidade:
                self.texto_atual += self.texto_completo[self.indice]
                self.indice += 1
                self.ultimo_tempo = agora

    def terminou(self):
        return self.indice >= len(self.texto_completo)

    def renderizar(self, cor):
        if self.texto_atual == "":
            return pygame.Surface((1, 1), pygame.SRCALPHA)

        linhas = self.texto_atual.split("\n")
        superficies = [self.fonte.render(l, True, cor) for l in linhas]

        largura = max(s.get_width() for s in superficies)
        altura = sum(s.get_height() for s in superficies)

        surface = pygame.Surface((largura, altura), pygame.SRCALPHA)

        y = 0
        for s in superficies:
            surface.blit(s, (0, y))
            y += s.get_height()

        return surface

    @property
    def fonte(self):
        return self.__fonte
    
    @fonte.setter
    def fonte(self, nova_fonte):
        self.__fonte = nova_fonte

    @property
    def velocidade(self):
        return self.__velocidade
    
    @velocidade.setter
    def velocidade(self, nova_velocidade):
        self.__velocidade = nova_velocidade

    @property
    def texto_completo(self):
        return self.__texto_completo
    
    @texto_completo.setter
    def texto_completo(self, novo_texto_completo):
        self.__texto_completo = novo_texto_completo

    @property
    def indice(self):
        return self.__indice
    
    @indice.setter
    def indice(self, novo_indice):
        self.__indice = novo_indice
    
    @property
    def ultimo_tempo(self):
        return self.__ultimo_tempo
    
    @ultimo_tempo.setter
    def ultimo_tempo(self, novo_ultimo_tempo):
        self.__ultimo_tempo = novo_ultimo_tempo


    def iniciar(self, texto):
        self.texto_completo = texto
        self.indice = 0
        self.ultimo_tempo = pygame.time.get_ticks()

    def terminou(self):
        return self.indice >= len(self.texto_completo)
