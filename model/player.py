# Importa o módulo pygame para desenvolvimento de jogos
import pygame

# Importa RLEACCEL para otimização de transparência nas imagens
from pygame.locals import RLEACCEL

# Importa as constantes de largura e altura da tela do arquivo de configurações
from settings import SCREEN_WIDTH, SCREEN_HEIGHT

# Define a classe Player estendendo pygame.sprite.Sprite
# Essa classe representa o jogador no jogo
class Player(pygame.sprite.Sprite):
    def __init__(self):
        # Inicializa a superclasse Sprite
        super(Player, self).__init__()
        
        # Carrega a imagem do jogador a partir da pasta de assets
        self.surf = pygame.image.load("assets/jet.png").convert_alpha()
        
        # Redimensiona a imagem para o tamanho desejado
        self.surf = pygame.transform.scale(self.surf, (60, 30))
        
        # Define a cor branca como transparente (filtro de cor)
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        
        # Cria o retângulo da imagem, que será usado para posicionamento e colisão
        self.rect = self.surf.get_rect()

    # Atualiza a posição do jogador com base nas teclas pressionadas
    def update(self, pressed_keys):
        # Move para cima
        if pressed_keys[pygame.K_UP]:
            self.rect.move_ip(0, -5)
        # Move para baixo
        if pressed_keys[pygame.K_DOWN]:
            self.rect.move_ip(0, 5)
        # Move para a esquerda
        if pressed_keys[pygame.K_LEFT]:
            self.rect.move_ip(-5, 0)
        # Move para a direita
        if pressed_keys[pygame.K_RIGHT]:
            self.rect.move_ip(5, 0)

        # Garante que o jogador não ultrapasse os limites da tela
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
