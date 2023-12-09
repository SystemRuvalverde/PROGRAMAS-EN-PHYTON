import pygame
import sys
import math

# Inicializar Pygame
pygame.init()

# Configuración de la pantalla
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Simulador del Sistema Solar")

# Definir colores
white = (255, 255, 255)
yellow = (255, 255, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
green = (0, 255, 0)

# Definir parámetros del sistema solar
sun_radius = 50
planet_radius = [10, 15, 20, 25, 30]  # Radio de los planetas
planet_distance = [100, 150, 200, 250, 300]  # Distancia de los planetas al sol
planet_speed = [0.02, 0.015, 0.01, 0.008, 0.005]  # Velocidad de rotación de los planetas

# Función para calcular la posición de un planeta en un momento dado
def calculate_position(angle, distance):
    x = width // 2 + distance * math.cos(angle)
    y = height // 2 + distance * math.sin(angle)
    return int(x), int(y)

# Bucle principal
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(white)  # Fondo blanco

    # Dibujar el sol
    pygame.draw.circle(screen, yellow, (width // 2, height // 2), sun_radius)

    # Dibujar planetas y calcular nueva posición
    for i in range(len(planet_radius)):
        angle = pygame.time.get_ticks() * planet_speed[i]
        x, y = calculate_position(angle, planet_distance[i])
        pygame.draw.circle(screen, blue, (x, y), planet_radius[i])

    pygame.display.flip()
    clock.tick(60)  # 60 fotogramas por segundo