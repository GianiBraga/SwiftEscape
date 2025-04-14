# Importa o módulo principal do pygame
import pygame

# Importa o módulo random para gerar posições aleatórias
import random

# Importa RLEACCEL para melhorar o desempenho ao usar cores transparentes
from pygame.locals import RLEACCEL

# Importa as dimensões da tela definidas no arquivo de configurações
from settings import SCREEN_WIDTH, SCREEN_HEIGHT

# Define a classe Cloud que representa as nuvens no fundo do jogo
# A classe herda de pygame.sprite.Sprite
class Cloud(pygame.sprite.Sprite):
    def __init__(self):
        # Inicializa a superclasse Sprite
        super(Cloud, self).__init__()

        # Carrega a imagem da nuvem com suporte a transparência (alpha)
        self.surf = pygame.image.load("assets/cloud.png").convert_alpha()
        
        # Redimensiona a imagem da nuvem
        self.surf = pygame.transform.scale(self.surf, (70, 50))
        
        # Define a cor preta como transparente
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        
        # Define a posição inicial da nuvem fora da tela, à direita
        # A posição vertical é aleatória dentro da altura da tela
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT),
            )
        )

    # Atualiza a posição da nuvem
    def update(self):
        # Move a nuvem lentamente para a esquerda
        self.rect.move_ip(-5, 0)
        
        # Remove a nuvem se ela sair completamente da tela
        if self.rect.right < 0:
            self.kill()
