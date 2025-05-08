import pygame
import random
from pygame.locals import K_ESCAPE, K_RETURN, KEYDOWN, QUIT
from model.player import Player
from model.enemy import Enemy
from model.cloud import Cloud
from settings import SCREEN_WIDTH, SCREEN_HEIGHT
from game_states import MENU, JOGANDO, GAME_OVER

# Inicializa o Pygame e a fonte
pygame.init()
pygame.font.init()

# Configura a janela principal
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Swift Escape")

# Fonte usada nos menus
font = pygame.font.SysFont("Arial", 36)

# Criação de eventos personalizados
ADDENEMY = pygame.USEREVENT + 1     # Evento para adicionar inimigos
pygame.time.set_timer(ADDENEMY, 250)

ADDCLOUD = pygame.USEREVENT + 2     # Evento para adicionar nuvens
pygame.time.set_timer(ADDCLOUD, 1000)

# Função utilitária para desenhar texto centralizado na tela
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect(center=(x, y))
    surface.blit(textobj, textrect)

# Tela de menu principal
def menu_principal():
    while True:
        # Fundo preto e instruções
        screen.fill((0, 0, 0))
        draw_text("Swift Escape", font, (255, 255, 255), screen, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 3)
        draw_text("Pressione ENTER para começar", font, (255, 255, 255), screen, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

        # Atualiza a tela
        pygame.display.flip()

        # Trata eventos do menu
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_RETURN:
                    return JOGANDO      # Começar o jogo
                elif event.key == K_ESCAPE:
                    pygame.quit()
                    exit()
            elif event.type == QUIT:
                pygame.quit()
                exit()

# Tela de game over
def game_over(score_time):
    while True:
        # Fundo preto e mensagem de fim de jogo
        screen.fill((0, 0, 0))
        draw_text(f"Game Over", font, (255, 0, 0), screen, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 3)
        draw_text(f"Pontos por tempo: {score_time}", font, (255, 255, 255), screen, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        draw_text("Pressione ENTER para jogar novamente", font, (255, 255, 255), screen, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50)

        # Atualiza a tela
        pygame.display.flip()

        # Trata eventos da tela de game over
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_RETURN:
                    return JOGANDO      # Reiniciar o jogo
                elif event.key == K_ESCAPE:
                    pygame.quit()
                    exit()
            elif event.type == QUIT:
                pygame.quit()
                exit()

# Loop principal do jogo (durante a partida)
def loop_jogo():
    # Cria o jogador e os grupos de sprites
    player = Player()
    enemies = pygame.sprite.Group()
    clouds = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()
    all_sprites.add(player)

    clock = pygame.time.Clock()
    running = True

    # Inicializa a variável de pontuação de tempo
    score_time = 0
    start_ticks = pygame.time.get_ticks()  # Captura o tempo de início para o cálculo de tempo

    while running:
        # Verifica os eventos
        for event in pygame.event.get():
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                return MENU             # Volta ao menu
            elif event.type == QUIT:
                pygame.quit()
                exit()
            elif event.type == ADDENEMY:
                new_enemy = Enemy()
                enemies.add(new_enemy)
                all_sprites.add(new_enemy)
            elif event.type == ADDCLOUD:
                new_cloud = Cloud()
                clouds.add(new_cloud)
                all_sprites.add(new_cloud)

        # Captura teclas pressionadas
        pressed_keys = pygame.key.get_pressed()

        # Atualiza jogador, inimigos e nuvens
        player.update(pressed_keys)
        enemies.update()
        clouds.update()

        # Preenche fundo com azul (céu)
        screen.fill((135, 206, 250))

        # Desenha todos os elementos na tela
        for entity in all_sprites:
            screen.blit(entity.surf, entity.rect)

        # Verifica colisão entre jogador e inimigos
        if pygame.sprite.spritecollideany(player, enemies):
            player.kill()
            return game_over(score_time)           # Vai para a tela de fim de jogo

        # Atualiza o tempo de sobrevivência (pontuação)
        score_time = (pygame.time.get_ticks() - start_ticks) // 1000  # Tempo em segundos

        # Exibe a pontuação de tempo na tela
        draw_text(f"Tempo: {score_time}", font, (255, 255, 255), screen, SCREEN_WIDTH - 150, 30)

        # Atualiza a tela
        pygame.display.flip()

        # Controla a taxa de frames
        clock.tick(30)

# Controlador de estado do jogo
estado = MENU
while True:
    if estado == MENU:
        estado = menu_principal()
    elif estado == JOGANDO:
        estado = loop_jogo()
    elif estado == GAME_OVER:
        estado = game_over(score_time)
