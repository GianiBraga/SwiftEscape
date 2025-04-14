# Importa o módulo pygame
import pygame

# Importa constantes úteis para eventos e teclas
from pygame.locals import K_ESCAPE, KEYDOWN, QUIT

# Importa as classes do jogo organizadas em módulos
from model.player import Player
from model.enemy import Enemy
from model.cloud import Cloud

# Importa as constantes de configuração da tela
from settings import SCREEN_WIDTH, SCREEN_HEIGHT

# Inicializar o pygame (obrigatório antes de usar qualquer função do pygame)
pygame.init()

# Criar o objeto da tela com dimensões especificadas
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Criar evento personalizado para adicionar inimigos a cada 250ms
ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 250)

# Criar evento personalizado para adicionar nuvens a cada 1000ms (1 segundo)
ADDCLOUD = pygame.USEREVENT + 2
pygame.time.set_timer(ADDCLOUD, 1000)

# Instanciar o jogador
player = Player()

# Criar grupos para sprites:
# - enemies: apenas os inimigos, para detectar colisões
# - clouds: apenas as nuvens, que são decorativas
# - all_sprites: todos os elementos desenhados na tela
enemies = pygame.sprite.Group()
clouds = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

# Variável para manter o loop principal rodando
running = True

# Criar um relógio para controlar a taxa de atualização (frames por segundo)
clock = pygame.time.Clock()

# Início do loop principal do jogo
while running:
    # Verifica todos os eventos que ocorreram (teclas, fechamento da janela, etc.)
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            # Se a tecla ESC for pressionada, o jogo é encerrado
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            # Se a janela for fechada, o jogo também é encerrado
            running = False
        elif event.type == ADDENEMY:
            # Adiciona um novo inimigo aos grupos de sprites
            new_enemy = Enemy()
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)
        elif event.type == ADDCLOUD:
            # Adiciona uma nova nuvem aos grupos de sprites
            new_cloud = Cloud()
            clouds.add(new_cloud)
            all_sprites.add(new_cloud)
    
    # Obtém as teclas que estão sendo pressionadas no momento
    pressed_keys = pygame.key.get_pressed()

    # Atualiza a posição do jogador com base nas teclas pressionadas
    player.update(pressed_keys)

    # Atualiza as posições dos inimigos e nuvens
    enemies.update()
    clouds.update()

    # Preenche o fundo da tela com um azul claro (céu)
    screen.fill((135, 206, 250))

    # Desenha todos os sprites na tela
    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)

    # Verifica colisão entre o jogador e qualquer inimigo
    if pygame.sprite.spritecollideany(player, enemies):
        # Se houver colisão, remove o jogador e encerra o jogo
        player.kill()
        running = False

    # Atualiza a tela com tudo que foi desenhado
    pygame.display.flip()

    # Controla a taxa de frames (30 FPS)
    clock.tick(30)
