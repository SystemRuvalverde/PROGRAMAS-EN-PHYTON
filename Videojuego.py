import pygame
import sys
import random

# Inicializar Pygame
pygame.init()

# Configuración de la pantalla
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Esquiva al Enemigo")

# Colores
white = (255, 255, 255)
blue = (255, 0, 0)

# Jugador
player_size = 50
player_x = width // 2 - player_size // 2
player_y = height - 2 * player_size
player_speed = 5

# Enemigo
enemy_size = 50
enemy_x = random.randint(0, width - enemy_size)
enemy_y = 0
enemy_speed = 5

# Reloj
clock = pygame.time.Clock()

# Puntuación
score = 0
font = pygame.font.Font(None, 36)

# Función principal del juego
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    player_x += (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * player_speed

    # Mover al enemigo
    enemy_y += enemy_speed
    if enemy_y > height:
        enemy_y = 0
        enemy_x = random.randint(0, width - enemy_size)
        score += 1

    # Verificar colisión
    if (
        player_x < enemy_x + enemy_size
        and player_x + player_size > enemy_x
        and player_y < enemy_y + enemy_size
        and player_y + player_size > enemy_y
    ):
        print("¡Has perdido!")
        pygame.quit()
        sys.exit()

    # Limpiar la pantalla
    screen.fill(white)

    # Dibujar jugador
    pygame.draw.rect(screen, blue, (player_x, player_y, player_size, player_size))

    # Dibujar enemigo
    pygame.draw.rect(screen, blue, (enemy_x, enemy_y, enemy_size, enemy_size))

    # Mostrar puntuación
    score_text = font.render(f"Puntuación: {score}", True, blue)
    screen.blit(score_text, (10, 10))

    # Actualizar la pantalla
    pygame.display.flip()
    # Controlar la velocidad del bucle
    clock.tick(30)