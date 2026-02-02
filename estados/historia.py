import pygame
from utils.texto import TextoDigitado
from config import *



# roteiro
historia = [
    {
        "texto": "Incrivel como a cidade continua sendo a mesma.\nMesmo com tantas coisas terriveis pairando sobre si,\nela continua com essa mascara esbanjando beleza para os idiotas.",
        "imagem": "adicionais/imagens/cidade,png",
        "cor": VERMELHO,
        "proximo": 1
    },
    {
        "texto": "Por que estou pensando nisso?\nAte parece que me importo com alguma coisa que acontece por aqui.",
        "imagem": "adicionais/imagens/olhar_frente.png",
        "cor": VERMELHO,
        "proximo": 2
    },
    {
        "texto": "As vezes eu ate queria me importar.\nE uma pena existir alguem como eu.\nSem amigos.\nSem importancia.",
        "imagem":"adicionais/imagens/olhar_lateral.png",
        "cor": VERMELHO,
        "proximo": 3
    },
    {
        "texto": "Estou cansada...\nEu so queria ser alguem melhor.\nMas talvez algum dia tudo isso pare.",
        "imagem": "adicionais/imagens/choro.png",
        "cor": VERMELHO,
        "proximo": 4
    },
    {
        "texto": "Mas o que e aquilo?\nUm gato?",
        "imagem":"adicionais/imagens/gato_longe.png",
        "cor": VERMELHO,
        "proximo": 5
    },
    {
        "texto": "Um gato de rua.",
        "imagem": "adicionais/imagens/gato_perto.png",
        "cor": VERMELHO,
        "escolha": {
            "texto": "O que fazer?",
            "opcoes": {
                "Levar o gato para casa": "final_bom",
                "Seguir reto": "final_ruim"
            }
        }
    }
]



final_bom = [
    {
        "texto": "Voce esta sozinho?\nQue idiota...\nAte parece que um gato falaria comigo.\nIsso e tao surreal quanto eu ser uma personagem de um jogo com a historia triste kakakakakaka",
        "imagem":"adicionais/imagens/gato_perto.png",
        "cor": VERMELHO,
        "proximo": 1
    },
    {
        "texto": "Bem...Acho que voce vem comigo.\nTalvez formemos uma boa dupla.",
        "imagem": "adicionais/imagens/teto.jpg",
        "cor": VERMELHO,
        "proximo": 2
    },
    {
        "texto": "",
        "imagem":None,
        "cor": AZUL,
        "proximo": 3
    },
    {
        "texto": "",
        "imagem":"adicionais/imagens/yuri.jpg",
        "cor": AZUL,
        "proximo": 4
    },
    {
        "texto": "Talvez adotar voce nao tenha sido uma ma ideia.\nPelo menos eu nao me sinto tao so... \nObrigada por me ajudar meu bichano. \nTalvez agora eu tenha coragem de pedir ajuda.",
        "imagem": None,
        "cor": AZUL
    },
    {
        "texto": "",
        "imagem": None,
        "cor": AZUL
    },
    {
        "texto": "Nothings about to happen to me e uma homenagem a todos os meus queridos companheiros",
        "imagem": "adicionais\Imagens\gatos.png",
        "cor": AZUL
    },
    {
        "texto": "Especialmente a nossa dev que partiu durante as producoes \nDescanse em paz Adelaide, te amo...",
        "imagem": "adicionais\Imagens\dede.png",
        "cor": AZUL
    },
    {
        "texto": "Obrigada por jogar",
        "imagem": None,
        "cor": AZUL
    }
]



final_ruim = [
    {
        "texto": "Voce nao e o unico que esta sozinho.\nAlgum dia voce entendera que eu nao seria boa o suficiente para cuidar de voce.",
        "imagem":"adicionais/imagens/gato_perto.png",
        "cor": VERMELHO,
        "proximo": 1
    },
    {
        "texto": "Adeus, gato.\nTenho problemas mais importantes para lidar.",
        "imagem": "adicionais/imagens/gato_longe.png",
        "cor": VERMELHO_ESCURO,
        "proximo": 2
    },
    {
        "texto": "Adeus...",
        "imagem": "adicionais/imagens/gato_longe.png",
        "cor": VERMELHO_ESCURO,
        "proximo": 3
    },
    {
        "texto": "E tudo continua do mesmo jeito. \nA cada dia que passa, o medo vai embora. \nE a cada dia que passa, essa ideia nao assusta mais como antes.",
        "imagem": None,
        "cor": VERMELHO_ESCURO
    },
]



class Historia:
    def __init__(self):
        # --- ROTEIRO ---
        self.cenas = historia
        self.indice = 0
        self.cena_atual = self.cenas[self.indice]

        # --- TEXTO ---
        self.texto = TextoDigitado(self.cena_atual["texto"])

        # --- IMAGEM ---
        self.imagem = self._carregar_imagem(self.cena_atual["imagem"])

        # --- COR / FILTRO ---
        self.cor_atual = self.cena_atual["cor"]

        # --- TEMPO ---
        self.tempo_fim_texto = None
        self.tempo_espera = 5000

        # --- ESCOLHAS ---
        self.em_escolha = False
        self.opcoes = [
            ("Levar o gato para casa", "final_bom"),
            ("Seguir reto", "final_ruim")
        ]

        self.botoes = []
        self.finalizada = False


    @property
    def cenas(self):
        return self.__cenas
    
    @cenas.setter
    def cenas(self, novas_cenas):
        self.__cenas = novas_cenas

    @property
    def indice(self):
        return self.__indice
    
    @indice.setter
    def indice(self, nova_indice):
        self.__indice = nova_indice

    @property
    def cena_atual(self):
        return self.__cena_atual
    
    @cena_atual.setter
    def cena_atual(self, novo_cena_atual):
        self.__cena_atual = novo_cena_atual
    
    @property
    def texto(self):
        return self.__texto
    
    @texto.setter
    def texto(self, novo_texto):
        self.__texto = novo_texto   

    @property
    def imagem(self):
        return self.__imagem
    
    @imagem.setter
    def imagem(self, nova_imagem):
        self.__imagem = nova_imagem
    
    @property
    def cor_atual(self):
        return self.__cor_atual
    
    @cor_atual.setter
    def cor_atual(self, nova_cor_atual):
        self.__cor_atual = nova_cor_atual
    @property
    def tempo_fim_texto(self):
        return self.__tempo_fim_texto
    
    @tempo_fim_texto.setter
    def tempo_fim_texto(self, novo_tempo_fim_texto):
        self.__tempo_fim_texto = novo_tempo_fim_texto

    @property
    def tempo_espera(self):
        return self.__tempo_espera
    
    @tempo_espera.setter
    def tempo_espera(self, novo_tempo_espera):
        self.__tempo_espera = novo_tempo_espera

    @property
    def em_escolha(self):
        return self.__em_escolha
    
    @em_escolha.setter
    def em_escolha(self, nova_em_escolha):
        self.__em_escolha = nova_em_escolha

    @property
    def opcoes(self):
        return self.__opcoes
    
    @opcoes.setter
    def opcoes(self, nova_opcoes):
        self.__opcoes = nova_opcoes

    def resetar(self):
        self.cenas = historia        # roteiro inicial
        self.indice = 0
        self.cena_atual = self.cenas[self.indice]

        self.texto = TextoDigitado(self.cena_atual["texto"])
        self.imagem = self._carregar_imagem(self.cena_atual["imagem"])
        self.cor_atual = self.cena_atual["cor"]

        self.em_escolha = False
        self.opcoes = []

        self.tempo_fim_texto = None
        self.finalizada = False

    def _carregar_imagem(self, nome):
        if nome is None:
            return None
        imagem = pygame.image.load(nome).convert()
        return pygame.transform.scale(imagem, (LARGURA, ALTURA))

    def atualizar(self):
        self.texto.atualizar()

        if self.em_escolha:
            return 

        if self.texto.terminou():
            if self.tempo_fim_texto is None:
                self.tempo_fim_texto = pygame.time.get_ticks()
            else:
                agora = pygame.time.get_ticks()
                if agora - self.tempo_fim_texto >= self.tempo_espera:
                    self.avancar()

    def avancar(self):
        self.tempo_fim_texto = None

        # SE TEM ESCOLHA
        if "escolha" in self.cena_atual:
            self.em_escolha = True
            self.opcoes = list(self.cena_atual["escolha"]["opcoes"].items())
            return

        # AVANÇA NORMALMENTE
        self.indice += 1

        # FIM DO ROTEIRO
        if self.indice >= len(self.cenas):
            self.finalizada = True
            return

        self._trocar_cena()


    def _trocar_cena(self):
        self.cena_atual = self.cenas[self.indice]
        self.texto = TextoDigitado(self.cena_atual["texto"])
        self.imagem = self._carregar_imagem(self.cena_atual["imagem"])
        self.cor_atual = self.cena_atual["cor"]

    def evento(self, evento):
        if not self.em_escolha:
            return

        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
            for i, rect in enumerate(self.botoes):
                if rect.collidepoint(evento.pos):
                    _, destino = self.opcoes[i]
                    self._ir_para_final(destino)
                    return


    def _ir_para_final(self, nome_final):
        if nome_final == "final_bom":
            self.cenas = final_bom
        else:
            self.cenas = final_ruim

        self.indice = 0
        self.em_escolha = False
        self.finalizada = False
        self._trocar_cena() 

    def desenhar_caixa_texto(self, tela, texto_surface, estado):
        largura = LARGURA - 80
        altura = 160
        x = 40
        y = ALTURA - altura - 30
        dados = ESTADOS.get("historia", ESTADOS["neutro"])
        cor = self.cor_atual
        alpha = dados["alpha"]


        caixa = pygame.Surface((largura, altura), pygame.SRCALPHA)
        caixa.fill((0, 0, 0, 140))
        tela.blit(caixa, (x, y))

        # borda
        pygame.draw.rect(
            tela,
            self.cor_atual,
            (x, y, largura, altura),
            2
        )

        tela.blit(texto_surface, (x + 20, y + 20))

        pulso = (pygame.time.get_ticks() // 500) % 2
        if pulso:
            largura += 1
            altura += 1


    def desenhar(self, tela):

        tela.fill((0, 0, 0))

        if self.imagem:
            tela.blit(self.imagem, (0, 0))

        cor = self.cor_atual

        texto_surface = self.texto.renderizar(cor)
        self.desenhar_caixa_texto(tela, texto_surface, estado="historia")

        if self.em_escolha:
            self._desenhar_escolhas(tela, cor)


    def _desenhar_escolhas(self, tela, cor):
        fonte = pygame.font.Font("adicionais/fonte/mago1.ttf", 35)

        self.botoes = []

        y = ALTURA - 100

        for texto, _ in self.opcoes:
            render = fonte.render(texto, True, cor)
            rect = render.get_rect(center=(LARGURA // 2, y))

            tela.blit(render, rect)
            self.botoes.append(rect)

            y += 30
