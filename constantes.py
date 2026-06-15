import pygame
pygame.init()

# Resolución de DISEÑO - todo el juego (mapas, bus, colisiones) usa esto
ANCHO_VENTANA = 1920
ALTO_VENTANA = 1080

# Resolución REAL de la pantalla del usuario (detectada automáticamente)
info = pygame.display.Info()
ANCHO_PANTALLA = info.current_w
ALTO_PANTALLA = info.current_h


COLOR_JUGADOR = (0, 0, 255)
COLOR_BG = (0, 0, 20)
BLANCO = (255, 255, 255)
NEGRO = (20, 20, 20)
GRIS = (70, 70, 70)
AZUL = (50, 120, 255)

FPS = 60

ANCHO_MAPA = 3000
ALTO_MAPA = 2000
VELOCIDAD = 20

ESCALA_PERSONAJE = 4

ANCHO_PERSONAJE = 32 * ESCALA_PERSONAJE
ALTO_PERSONAJE = 53 * ESCALA_PERSONAJE