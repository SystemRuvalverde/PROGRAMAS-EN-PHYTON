import pygame
import sys
from pygame.locals import *
from math import radians, sin, cos

# Inicializar Pygame
pygame.init()

# Configuración de la ventana
width, height = 800, 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Sistema Solar Simulator")

# Colores
white = (255, 255, 255)
yellow = (255, 255, 0)
blue = (0, 0, 255)

# Clase para representar un planeta
class Planet:
    def __init__(self, distance, radius, color, speed):
        self.distance = distance  # Distancia desde el sol
        self.radius = radius  # Radio del planeta
        self.color = color  # Color del planeta
        self.angle = 0  # Ángulo inicial
        self.speed = speed  # Velocidad de rotación

    def update(self):
        self.angle += self.speed

    def draw(self):
        x = int(width / 2 + self.distance * cos(radians(self.angle)))
        y = int(height / 2 + self.distance * sin(radians(self.angle)))
        pygame.draw.circle(window, self.color, (x, y), self.radius)

# Crear planetas
sun = Planet(0, 50, yellow, 0)
earth = Planet(150, 20, blue, 1)

planets = [earth]

# Ciclo principal del juego
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    window.fill(white)

    # Dibujar el sol
    pygame.draw.circle(window, sun.color, (int(width / 2), int(height / 2)), sun.radius)

    # Actualizar y dibujar planetas
    for planet in planets:
        planet.update()
        planet.draw()

    pygame.display.flip()
    pygame.time.Clock().tick(60)