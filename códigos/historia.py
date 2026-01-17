import pygame
from texto import TextoDigitado
from config import LARGURA, ALTURA, PALETAS, BOTAO_HOVER, BORDA, BOTAO_NORMAL, BOTAO_SELECIONADO, FONTE

class Historia:
    def __init__(self):
        self.escolhas = []
        self.mostrar_escolhas = False
        self.selecao = 0
        self.tempo_fim_texto = None
        self.tempo_espera = 5000  

    @property
    def mostrar_escolhas(self):
        return self.__mostrar_escolhas
    
    @mostrar_escolhas.setter
    def mostrar_escolhas(self, novo_mostrar_escolhas):
        self.__mostrar_escolhas = novo_mostrar_escolhas

    @property
    def selecao(self):
        return self.__selecao
    
    @selecao.setter
    def selecao(self, nova_selecao):
        self.__selecao = nova_selecao

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

        self.falas = [
            {
                "texto": "A cidade parece grande demais.",
                "imagem": "",
                "estado": "instavel",
            },
            {
                "texto": "Um gato parado na calcada.",
                "imagem": "",
                "estado": "instavel",
                "escolhas": [
                    {
                        "texto": "Adotar o gato",
                        "proxima": 2,
                        "estado": "calmo"
                    },
                    {
                        "texto": "Seguir em frente",
                        "proxima": 3,
                        "estado": "apagado"
                    }
                ]
            },
            {
                "texto": "O silencio em casa e diferente agora.",
                "imagem": "",
                "estado": "calmo",
            },
            {
                "texto": "A cidade continua a mesma.",
                "imagem": "",
                "estado": "apagado",
            }
        ]


        self.indice_fala = 0
        self.finalizada = False

        self.texto = TextoDigitado(velocidade=40)

        # --- CONTROLE DE TRANSIÇÃO ---
        self.estado_atual = "instavel"
        self.estado_alvo = "instavel"

        self.alpha_atual = PALETAS[self.estado_atual]["alpha"]
        self.alpha_alvo = self.alpha_atual

        self.velocidade_transicao = 0.5 

        self._carregar_fala_atual()

    @property
    def falas(self):
        return self.__falas
    
    @falas.setter
    def falas(self, novas_falas):
        self.__falas = novas_falas

    @property
    def indice_fala(self):
        return self.__indice_fala
    
    @indice_fala.setter
    def indice_fala(self, nova_indice_fala):
        self.__indice_fala = nova_indice_fala

    @property
    def finalizada(self):
        return self.__finalizada
    
    @finalizada.setter
    def finalizada(self, nova_finalizada):
        self.__finalizada = nova_finalizada

    @property
    def texto(self):
        return self.__texto
    
    @texto.setter
    def texto(self, novo_texto):
        self.__texto = novo_texto

    @property
    def estado_atual(self):
        return self.__estado_atual
    
    @estado_atual.setter
    def estado_atual(self, novo_estado_atual):
        self.__estado_atual = novo_estado_atual

    @property
    def estado_alvo(self):
        return self.__estado_alvo
    
    @estado_alvo.setter
    def estado_alvo(self, novo_estado_alvo):
        self.__estado_alvo = novo_estado_alvo

    @property
    def alpha_atual(self):
        return self.__alpha_atual
    
    @alpha_atual.setter
    def alpha_atual(self, novo_alpha_atual):
        self.__alpha_atual = novo_alpha_atual

    @property
    def alpha_alvo(self):
        return self.__alpha_alvo
    
    @alpha_alvo.setter
    def alpha_alvo(self, novo_alpha_alvo):
        self.__alpha_alvo = novo_alpha_alvo

    @property
    def velocidade_transicao(self):
        return self.__velocidade_transicao
    
    @velocidade_transicao.setter
    def velocidade_transicao(self, nova_velocidade_transicao):
        self.__velocidade_transicao = nova_velocidade_transicao

    def _carregar_fala_atual(self):
        fala = self.falas[self.indice_fala]

        self.tempo_fim_texto = None

        self.texto.iniciar(fala["texto"])

        self.imagem = pygame.image.load(fala["imagem"]).convert()
        self.imagem = pygame.transform.scale(self.imagem, (LARGURA, ALTURA))

        self.estado_alvo = fala.get("estado", "neutro")
        self.alpha_alvo = PALETAS[self.estado_alvo]["alpha"]

        self.escolhas = fala.get("escolhas", [])
        self.mostrar_escolhas = False

    def atualizar(self):
        self.texto.atualizar()

        if self.texto.terminou() and self.escolhas:
            self.mostrar_escolhas = True

        if self.alpha_atual < self.alpha_alvo:
            self.alpha_atual += self.velocidade_transicao
        elif self.alpha_atual > self.alpha_alvo:
            self.alpha_atual -= self.velocidade_transicao

        self.alpha_atual = max(0, min(self.alpha_atual, 255))

        if self.texto.terminou() and not self.escolhas:
            if self.tempo_fim_texto is None:
                self.tempo_fim_texto = pygame.time.get_ticks()
            else:
                agora = pygame.time.get_ticks()
                if agora - self.tempo_fim_texto >= self.tempo_espera:
                    self.indice_fala += 1

                    if self.indice_fala < len(self.falas):
                        self._carregar_fala_atual()
                    else:
                        self.finalizada = True

    def evento(self, evento):
        if self.mostrar_escolhas:
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_UP:
                    self.selecao = max(0, self.selecao - 1)

                if evento.key == pygame.K_DOWN:
                    self.selecao = min(len(self.escolhas) - 1, self.selecao + 1)

                if evento.key in (pygame.K_RETURN, pygame.K_SPACE):
                    self._escolher(self.selecao)

            if evento.type == pygame.MOUSEBUTTONDOWN:
                if evento.button == 1:
                    for i, botao in enumerate(self.botoes):
                        if botao.collidepoint(evento.pos):
                            self._escolher(i)
            return

        if evento.type == pygame.KEYDOWN:
            if evento.key in (pygame.K_SPACE, pygame.K_RETURN):
                if self.texto.terminou():
                    self.indice_fala += 1
                    if self.indice_fala < len(self.falas):
                        self._carregar_fala_atual()
                        self.tempo_fim_texto = None
                    else:
                        self.finalizada = True

    def _escolher(self, indice):
        escolha = self.escolhas[indice]
        self.indice_fala = escolha["proxima"]

        # mudança de estado emocional
        self.estado_alvo = escolha["estado"]
        self.alpha_alvo = PALETAS[self.estado_alvo]["alpha"]

        self.mostrar_escolhas = False
        self._carregar_fala_atual()


    def _aplicar_filtro(self, tela):
        dados = PALETAS.get(self.estado_alvo)
        if not dados or not dados["overlay"]:
            return

        camada = pygame.Surface(tela.get_size())
        camada.fill(dados["overlay"])
        camada.set_alpha(int(self.alpha_atual))
        tela.blit(camada, (0, 0))

    def desenhar(self, tela):
        tela.blit(self.imagem, (0, 0))
        self._aplicar_filtro(tela)
        self.texto.desenhar(tela)

        if self.mostrar_escolhas:
            self.botoes = []
            mouse_pos = pygame.mouse.get_pos()
            y = ALTURA - 260

            pulso = (pygame.time.get_ticks() // 500) % 2

            for i, escolha in enumerate(self.escolhas):
                rect = pygame.Rect(100, y, LARGURA - 200, 50)

                hover = rect.collidepoint(mouse_pos)
                selecionado = (i == self.selecao)

            if selecionado:
                cor = BOTAO_SELECIONADO
            elif hover:
                cor = BOTAO_HOVER
            else:
                cor = BOTAO_NORMAL

                borda = 3 if selecionado and pulso else 2
                pygame.draw.rect(tela, cor, rect, borda)

                texto = f"{i+1}. {escolha['texto']}"
                render = self.texto.FONTE.render(texto, True, cor)
                tela.blit(render, (rect.x + 20, rect.y + 12))

                self.botoes.append(rect)
                y += 70

