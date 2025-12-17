# estados/historia.py
import pygame
from texto import TextoDigitado

class Historia:
    def __init__(self):
        self.falas = [
            ("Hoje o dia parece estranho.", "download (81).jpg"),
            ("O céu está pesado.", "download (82).jpg"),
            ("Eu só queria sair de casa.", "Elis Regina.jpg"),
        ]


        self.indice_fala = 0
        self.texto = TextoDigitado(velocidade=40)
        self.texto.iniciar(self.falas[self.indice_fala])
        self.finalizada = False

        self.falas, caminho = self.falas[self.indice_fala]
        self.imagem = pygame.image.load(caminho).convert()

    def atualizar(self):
        self.texto.atualizar()

    def evento(self, evento):
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE:
                if self.texto.terminou():
                    self.indice_fala += 1
                    if self.indice_fala < len(self.falas):
                        self.texto.iniciar(self.falas[self.indice_fala])
                    else:
                        self.finalizada = True

    def desenhar(self, tela):
        imagem_atual = self.imagem[self.indice_fala]

        # Centraliza a imagem
        rect = imagem_atual.get_rect(center=(400, 200))
        tela.blit(imagem_atual, rect)

        self.texto.desenhar(tela)
