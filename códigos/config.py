import pygame

# Tela
LARGURA = 1280
ALTURA = 720
FPS = 60

# Cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
VERMELHO = (255,44,44)
FUNDO_HISTORIA = (30, 30, 30)

# Fonte
pygame.font.init()
FONTE = pygame.font.Font("mago3.ttf", 40)

# Paletas de sentimentos
PALETAS = {
    "instavel": {"overlay": (120, 0, 0), "alpha": 80},
    "calmo": {"overlay": (40, 90, 160), "alpha": 60},
    "apagado": {"overlay": (0, 0, 0), "alpha": 120},
    "neutro": {"overlay": None, "alpha": 0},
}

# Botões
BOTAO_NORMAL = (180, 180, 180)
BOTAO_HOVER = (230, 230, 230)
BOTAO_SELECIONADO = (120, 160, 220) 
BORDA = 2

