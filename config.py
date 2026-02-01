import pygame

# Tela
LARGURA = 1280
ALTURA = 720
FPS = 60

# Cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
VERMELHO = (120, 0, 0)
VERMELHO_ESCURO = (60, 0, 0)
AZUL = (80, 120, 200)


# Fonte
pygame.font.init()
FONTE = pygame.font.Font("mago1.ttf", 60)

# Estados de sentimentos
ESTADOS = {
    "instavel": {
        "cor": (200, 40, 40), 
        "alpha": 150
    },
    "calmo": {
        "cor": (80, 140, 255),  
        "alpha": 190
    },
    "neutro": {
        "cor": (220, 220, 220),  
        "alpha": 170
    }
}


# Botões
BOTAO_NORMAL = (180, 180, 180)
BOTAO_HOVER = (230, 230, 230)
BOTAO_SELECIONADO = (120, 160, 220)  # azul suave
BORDA = 2
