import pygame
from texto import TextoDigitado
from config import *



# roteiro
historia = [
    {
        "texto": "Incrível como a cidade continua sendo a mesma.\nMesmo com tantas coisas terríveis pairando sobre si,\nela continua com essa máscara esbanjando beleza para os idiotas.",
        "imagem": "cidade.png",
        "cor": VERMELHO,
        "proximo": 1
    },
    {
        "texto": "Por que estou pensando nisso?\nAté parece que me importo com alguma coisa que acontece por aqui.",
        "imagem": "olhar_lado.png",
        "cor": VERMELHO,
        "proximo": 2
    },
    {
        "texto": "Às vezes eu até queria me importar.\nÉ uma pena existir alguém como eu.\nSem amigos.\nSem importância.",
        "imagem": "olhar_frente.png",
        "cor": VERMELHO,
        "proximo": 3
    },
    {
        "texto": "Estou cansada...\nEu só queria ser alguém melhor.\nMas talvez algum dia tudo isso pare.",
        "imagem": "olhos_lagrimas.png",
        "cor": VERMELHO,
        "proximo": 4
    },
    {
        "texto": "Mas o que é aquilo?\nUm gato?",
        "imagem": "gato_distante.png",
        "cor": VERMELHO,
        "proximo": 5
    },
    {
        "texto": "Um gato de rua.",
        "imagem": "gato_olhando.png",
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
        "texto": "Você está sozinho?\nQue idiota...\nAté parece que um gato falaria comigo.",
        "imagem": "gato_close.png",
        "cor": VERMELHO,
        "proximo": 1
    },
    {
        "texto": "Bem...\nAcho que você vem comigo.\nTalvez formemos uma boa dupla.",
        "imagem": "gato_no_colo.png",
        "cor": VERMELHO,
        "proximo": 2
    },
    {
        "texto": "",
        "imagem": "apartamento_gato.png",
        "cor": AZUL,
        "proximo": 3
    },
    {
        "texto": "Talvez adotar você não tenha sido uma má ideia.\nPelo menos agora o silêncio é diferente.\nTalvez eu também mereça cuidado.\nTalvez agora eu tenha coragem de pedir ajuda.",
        "imagem": None,
        "cor": AZUL
    }
]



final_ruim = [
    {
        "texto": "Você não é o único que está sozinho.\nMas eu não sou boa o suficiente para cuidar de você.",
        "imagem": "gato_olhando.png",
        "cor": VERMELHO,
        "proximo": 1
    },
    {
        "texto": "Adeus, gato.\nTenho coisas mais importantes para lidar.",
        "imagem": "afastando.png",
        "cor": VERMELHO_ESCURO,
        "proximo": 2
    },
    {
        "texto": "Adeus...",
        "imagem": "olhar_camera.png",
        "cor": VERMELHO_ESCURO,
        "proximo": 3
    },
    {
        "texto": "Tudo continua do mesmo jeito.\nA cada dia, o medo desaparece.\nE essa ideia estranha não assusta mais como antes.",
        "imagem": None,
        "cor": VERMELHO_ESCURO
    }
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
        self.em_escolha = True
        self.opcoes = [
            ("Levar o gato para casa", "final_bom"),
            ("Seguir reto", "final_ruim")
        ]




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



    def _carregar_imagem(self, nome):
        if nome is None:
            return None
        imagem = pygame.image.load(nome).convert()
        return pygame.transform.scale(imagem, (LARGURA, ALTURA))

    def atualizar(self):
        self.texto.atualizar()

        if self.texto.terminou() and not self.em_escolha:
            if self.tempo_fim_texto is None:
                self.tempo_fim_texto = pygame.time.get_ticks()
            else:
                agora = pygame.time.get_ticks()
                if agora - self.tempo_fim_texto >= self.tempo_espera:
                    self.avancar()


    def avancar(self):
        self.tempo_fim_texto = None

        if "escolha" in self.cena_atual:
            self.em_escolha = True
            self.opcoes = list(self.cena_atual["escolha"]["opcoes"].items())
            return

        proximo = self.cena_atual.get("proximo")
        if proximo is None:
            return

        self.indice = proximo
        self._trocar_cena()


    def _trocar_cena(self):
        self.cena_atual = self.cenas[self.indice]
        self.texto = TextoDigitado(self.cena_atual["texto"])
        self.imagem = self._carregar_imagem(self.cena_atual["imagem"])
        self.cor_atual = self.cena_atual["cor"]

    def evento(self, evento):
        if self.em_escolha and evento.type == pygame.MOUSEBUTTONDOWN:
            if evento.button == 1:
                for i, rect in enumerate(self.botoes):
                    if rect.collidepoint(evento.pos):
                        _, destino = self.opcoes[i]
                        self._ir_para_final(destino)

    def _ir_para_final(self, nome_final):
        if nome_final == "final_bom":
            self.cenas = final_bom
        else:
            self.cenas = final_ruim

        self.indice = 0
        self.em_escolha = False
        self._trocar_cena()

    def desenhar_caixa_texto(self, tela, texto_surface, estado):
        dados = ESTADOS.get(estado, ESTADOS["neutro"])
        cor = dados["cor"]
        alpha = dados["alpha"]

        largura = LARGURA - 80
        linhas = texto_surface.get_height() // 20
        altura = 150 + (linhas * 5)
        x = 40
        y = ALTURA - altura - 30

        # fundo transparente
        caixa = pygame.Surface((largura, altura), pygame.SRCALPHA)
        caixa.fill((0, 0, 0, alpha))
        tela.blit(caixa, (x, y))

        # borda fina
        espessura = 2 if cor == VERMELHO else 1
        pygame.draw.rect(
            tela,
            cor,
            (x, y, largura, altura),
            espessura
        )

        # texto
        tela.blit(texto_surface, (x + 20, y + 20))

        pulso = (pygame.time.get_ticks() // 500) % 2
        if pulso:
            largura += 1
            altura += 1


    def desenhar(self, tela):
        if self.imagem:
            tela.blit(self.imagem, (0, 0))

        # --- caixa de texto ---
        dados = ESTADOS.get(self.estado, ESTADOS["neutro"])
        cor = dados["cor"]

        texto_surface = self.texto.renderizar(cor)
        self.desenhar_caixa_texto(tela, texto_surface, self.estado)

        # --- Botões de escolha ---
        if self.em_escolha:
            self._desenhar_escolhas(tela, cor)

    def _desenhar_escolhas(self, tela, cor):
        fonte = pygame.font.Font("mago1.ttf", 20)
        mouse = pygame.mouse.get_pos()

        y_inicial = ALTURA - 90
        self.botoes = []

        for i, (texto, _) in enumerate(self.opcoes):
            render = fonte.render(texto, True, cor)
            rect = render.get_rect(center=(LARGURA // 2, y_inicial))

            hover = rect.collidepoint(mouse)
            cor_texto = cor if hover else (120, 120, 120)

            render = fonte.render(texto, True, cor_texto)
            tela.blit(render, rect)

            self.botoes.append(rect)
            y_inicial += 30

