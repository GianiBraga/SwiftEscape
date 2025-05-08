# Importa o módulo principal do pygame
import pygame

# Importa o módulo random para geração de números aleatórios
import random

# Importa RLEACCEL para otimização de transparência nas imagens
from pygame.locals import RLEACCEL

# Importa as constantes de largura e altura da tela do arquivo de configurações
from settings import SCREEN_WIDTH, SCREEN_HEIGHT

# Define a classe Enemy estendendo pygame.sprite.Sprite
# Essa classe representa os inimigos (mísseis) que se movem da direita para a esquerda
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        # Inicializa a superclasse Sprite
        super(Enemy, self).__init__()

        # Carrega a imagem do míssil a partir da pasta de assets
        self.surf = pygame.image.load("assets/missel.png").convert()
        
        # Redimensiona a imagem do míssil
        self.surf = pygame.transform.scale(self.surf, (50, 20))
        
        # Define a cor branca como transparente
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        
        # Define a posição inicial do míssil fora da tela, à direita
        # A posição vertical é aleatória dentro da altura da tela
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT),
            )
        )
        
        # Define uma velocidade aleatória para o míssil
        self.speed = random.randint(5, 20)

    # Atualiza a posição do míssil
    def update(self):
        # Move o míssil para a esquerda com base na sua velocidade
        self.rect.move_ip(-self.speed, 0)
        
        # Remove o míssil se ele sair completamente da tela (pela esquerda)
        if self.rect.right < 0:
            self.kill()
