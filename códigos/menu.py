import pygame
from config import LARGURA, ALTURA, PRETO, BRANCO

BOTAO_NORMAL = (180, 180, 180)
BOTAO_HOVER = (230, 230, 230)

class Menu:
    def __init__(self, fonte_titulo, fonte_botao):
        self.fonte_titulo = fonte_titulo
        self.fonte_botao = fonte_botao

        self.botoes = {
            "iniciar": pygame.Rect(LARGURA//2 - 150, ALTURA//2, 300, 50),
            "sair": pygame.Rect(LARGURA//2 - 150, ALTURA//2 + 80, 300, 50),
        }

        self.acao = None

    @property
    def fonte_titulo(self):
        return self.__fonte_titulo
    
    @fonte_titulo.setter
    def fonte_titulo(self, nova_fonte_titulo):
        self.__fonte_titulo = nova_fonte_titulo

    @property
    def fonte_botao(self):
        return self.__fonte_botao
    
    @fonte_botao.setter
    def fonte_botao(self, nova_fonte_botao):
        self.__fonte_botao = nova_fonte_botao
    
    @property
    def botoes(self):
        return self.__botoes
    
    @botoes.setter
    def botoes(self, novos_botoes):
        self.__botoes = novos_botoes

    @property
    def acao(self):
        return self.__acao
    
    @acao.setter
    def acao(self, nova_acao):
        self.__acao = nova_acao

    def evento(self, evento):
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if evento.button == 1:
                for nome, rect in self.botoes.items():
                    if rect.collidepoint(evento.pos):
                        self.acao = nome

        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_RETURN:
                self.acao = "iniciar"
            if evento.key == pygame.K_ESCAPE:
                self.acao = "sair"

    def desenhar(self, tela):
        tela.fill(0,0,0)
        mouse_pos = pygame.mouse.get_pos()

        # Título
        titulo = self.fonte_titulo.render(
            "Nothing's About to Happen to Me", True, BRANCO
        )
        tela.blit(
            titulo,
            titulo.get_rect(center=(LARGURA//2, ALTURA//2 - 120))
        )

        # Botões
        for nome, rect in self.botoes.items():
            hover = rect.collidepoint(mouse_pos)
            cor = BOTAO_HOVER if hover else BOTAO_NORMAL

            pygame.draw.rect(tela, cor, rect, 2)

            texto = nome.upper()
            render = self.fonte_botao.render(texto, True, cor)
            tela.blit(render, render.get_rect(center=rect.center))
