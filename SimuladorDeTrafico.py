import pygame
import sys
import random

# Configuración del simulador
FPS = 60
ANCHO_PANTALLA = 1366
ALTO_PANTALLA = 768
VELOCIDAD_COCHE = 5
VELOCIDAD_MOTO = 4
VELOCIDAD_CAMION = 4
COLOR_FONDO = (128, 128, 128)

pygame.init()

# Carga de imágenes
coche_imagen = pygame.image.load("coche.png")
moto_imagen = pygame.image.load("moto.png")
camion_imagen = pygame.image.load("camion.png")

class Coche:
    def __init__(self, x, y):
        self.imagen = coche_imagen
        self.rectangulo = self.imagen.get_rect(topleft=(x, y))

    def mover(self):
        self.rectangulo.y += VELOCIDAD_COCHE
        if self.rectangulo.y > ALTO_PANTALLA:
            self.rectangulo.y = 0

class Moto:
    def __init__(self, x, y):
        self.imagen = moto_imagen
        self.rectangulo = self.imagen.get_rect(topleft=(x, y))

    def mover(self):
        self.rectangulo.y += VELOCIDAD_MOTO
        if self.rectangulo.y > ALTO_PANTALLA:
            self.rectangulo.y = 0

class Camion:
    def __init__(self, x, y):
        self.imagen = camion_imagen
        self.rectangulo = self.imagen.get_rect(topleft=(x, y))

    def mover(self):
        self.rectangulo.y += VELOCIDAD_CAMION
        if self.rectangulo.y > ALTO_PANTALLA:
            self.rectangulo.y = 0

def main():
    reloj = pygame.time.Clock()

    pantalla = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA))
    pygame.display.set_caption("Simulador de Tráfico")

    coches = [Coche(random.randint(0, ANCHO_PANTALLA - coche_imagen.get_width()),
                   random.randint(0, ALTO_PANTALLA - coche_imagen.get_height())) for _ in range(5)]

    motos = [Moto(random.randint(0, ANCHO_PANTALLA - moto_imagen.get_width()),
                  random.randint(0, ALTO_PANTALLA - moto_imagen.get_height())) for _ in range(5)]

    camiones = [Camion(random.randint(0, ANCHO_PANTALLA - camion_imagen.get_width()),
                      random.randint(0, ALTO_PANTALLA - camion_imagen.get_height())) for _ in range(5)]

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        for coche in coches:
            coche.mover()

        for moto in motos:
            moto.mover()

        for camion in camiones:
            camion.mover()

        pantalla.fill(COLOR_FONDO)

        for coche in coches:
            pantalla.blit(coche.imagen, coche.rectangulo)

        for moto in motos:
            pantalla.blit(moto.imagen, moto.rectangulo)

        for camion in camiones:
            pantalla.blit(camion.imagen, camion.rectangulo)

        pygame.display.flip()
        reloj.tick(FPS)

if __name__ == "__main__":
    main()
