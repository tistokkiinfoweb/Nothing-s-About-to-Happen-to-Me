import pygame
from config import PRETO, BRANCO, FONTE

class TextoDigitado:
    def __init__(self, velocidade=15):
        self.fonte = FONTE
        self.velocidade = velocidade
        self.texto_completo = ""
        self.texto_visivel = ""
        self.indice = 0
        self.ultimo_tempo = pygame.time.get_ticks()

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
    def texto_visivel(self):
        return self.__texto_visivel
    
    @texto_visivel.setter
    def texto_visivel(self, novo_texto_visivel):
        self.__texto_visivel = novo_texto_visivel

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


    
    def renderizar(self, cor):
        linhas = self.texto_visivel.split("\n")
        surfaces = []

        for linha in linhas:
            render = self.fonte.render(linha, True, cor)
            surfaces.append(render)

        largura = max(s.get_width() for s in surfaces)
        altura = sum(s.get_height() for s in surfaces)

        surface = pygame.Surface((largura, altura), pygame.SRCALPHA)

        y = 0
        for s in surfaces:
            surface.blit(s, (0, y))
            y += s.get_height()

        return surface


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
