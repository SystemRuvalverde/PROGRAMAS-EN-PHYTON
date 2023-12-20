import pygame
from pygame.locals import *

# Inicializar pygame
pygame.init()

# Configurar pantalla
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Juego del Gato')
pygame.cursors.diamond
# Inicializar el tablero
board = [[None, None, None], [None, None, None], [None, None, None]]

# Variables para almacenar las posiciones de las fichas
x_turn = True
o_positions = []
x_positions = []

# Función para dibujar las fichas en la pantalla
def draw_pieces():
    global x_positions, o_positions
    for pos in x_positions:
        pygame.draw.line(screen, (255, 0, 0), (pos[0] + 25, pos[1] + 25), (pos[0] + 175, pos[1] + 175), 4)
        pygame.draw.line(screen, (255, 0, 0), (pos[0] + 175, pos[1] + 25), (pos[0] + 25, pos[1] + 175), 4)
    for pos in o_positions:
        pygame.draw.circle(screen, (0, 0, 255), (pos[0] + 100, pos[1] + 100), 50, 4)

# Función para verificar si hay un ganador
def check_winner():
    for row in board:
        if all(cell == 'X' for cell in row):
            draw_winning_line((0, row.index('X') * 200), (600, row.index('X') * 200))
            return 'X'
        elif all(cell == 'O' for cell in row):
            draw_winning_line((0, row.index('O') * 200), (600, row.index('O') * 200))
            return 'O'

    for col in range(3):
        if all(row[col] == 'X' for row in board):
            draw_winning_line((col * 200, 0), (col * 200, 600))
            return 'X'
        elif all(row[col] == 'O' for row in board):
            draw_winning_line((col * 200, 0), (col * 200, 600))
            return 'O'

    if all(board[i][i] == 'X' for i in range(3)):
        draw_winning_line((0, 0), (600, 600))
        return 'X'
    elif all(board[i][i] == 'O' for i in range(3)):
        draw_winning_line((0, 0), (600, 600))
        return 'O'

    if all(board[i][2 - i] == 'X' for i in range(3)):
        draw_winning_line((600, 0), (0, 600))
        return 'X'
    elif all(board[i][2 - i] == 'O' for i in range(3)):
        draw_winning_line((600, 0), (0, 600))
        return 'O'

    return None

# Función para dibujar la línea de victoria
def draw_winning_line(start, end):
    pygame.draw.line(screen, (0, 255, 0), start, end, 8)

# Bucle principal del juego
running = True
while running:
    # Limpiar la pantalla
    screen.fill((255, 255, 255))

    # Dibujar líneas de la estructura del gato
    pygame.draw.line(screen, (0, 0, 0), (200, 0), (200, 600), 4)
    pygame.draw.line(screen, (0, 0, 0), (400, 0), (400, 600), 4)
    pygame.draw.line(screen, (0, 0, 0), (0, 200), (600, 200), 4)
    pygame.draw.line(screen, (0, 0, 0), (0, 400), (600, 400), 4)

    # Dibujar cuadrícula
    for x in range(0, 600, 200):
        for y in range(0, 600, 200):
            pygame.draw.line(screen, (0, 0, 0), (x, 0), (x, 600), 1)
            pygame.draw.line(screen, (0, 0, 0), (0, y), (600, y), 1)

    # Dibujar las fichas en la pantalla
    draw_pieces()

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

        if event.type == MOUSEBUTTONDOWN:
            # Obtener la posición del ratón
            x, y = pygame.mouse.get_pos()
            # Convertir la posición a la cuadrícula
            square_x, square_y = x // 200, y // 200
            # Verificar si la casilla está vacía
            if board[square_y][square_x] is None:
                # Actualizar la posición de la ficha y el estado del tablero
                if x_turn:
                    x_positions.append((square_x * 200, square_y * 200))
                    board[square_y][square_x] = 'X'
                    x_turn = False
                else:
                    o_positions.append((square_x * 200, square_y * 200))
                    board[square_y][square_x] = 'O'
                    x_turn = True

    # Verificar si hay un ganador o empate
    winner = check_winner()
    if winner:
        print(f'¡El jugador {winner} ha ganado!')
        running = False
    elif all(cell is not None for row in board for cell in row):
        print('¡Empate!')
        running = False

    # Actualizar la pantalla
    pygame.display.flip()

# Cerrar Pygame
pygame.quit()
