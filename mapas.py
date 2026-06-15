import pygame
import constantes

mapa_actual = 1

mapa_edificio = pygame.image.load(
    "assets/images/Map/Edificio1_1.png"
)

# mapa 1: INICIO
paredes_mapa1 = [
    pygame.Rect(0, 0, constantes.ANCHO_VENTANA, 40),
    pygame.Rect(0, 0, 40, constantes.ALTO_VENTANA),
    pygame.Rect(constantes.ANCHO_VENTANA - 40, 0, 40, constantes.ALTO_VENTANA),
    pygame.Rect(0, constantes.ALTO_VENTANA - 40, 700, 40),
    pygame.Rect(1200, constantes.ALTO_VENTANA - 40, 720, 40)
]

# salida del mapa 1 hacia el patio central
salida_mapa1 = pygame.Rect(700, constantes.ALTO_VENTANA - 40, 500, 40)

# mapa 2: primera zona verde
paredes_mapa2 = [
    pygame.Rect(0, 0, 700, 40),
    pygame.Rect(1200, 0, constantes.ANCHO_VENTANA - 1200, 40),
    pygame.Rect(0, 0, 40, constantes.ALTO_VENTANA),
    pygame.Rect(constantes.ANCHO_VENTANA - 40, 0, 40, constantes.ALTO_VENTANA)
]

# puerta superior a INICIO
salida_mapa2 = pygame.Rect(700, 0, 500, 40)

# salida inferior a segunda zona verde: toda la anchura libre en el borde inferior
salida_mapa2_abajo = pygame.Rect(0, constantes.ALTO_VENTANA - 40, constantes.ANCHO_VENTANA, 40)

# segunda zona verde
paredes_mapa3 = [
    pygame.Rect(0, 0, 40, 420),
    pygame.Rect(0, 680, 40, constantes.ALTO_VENTANA - 680),
    pygame.Rect(constantes.ANCHO_VENTANA - 40, 0, 40, 420),
    pygame.Rect(constantes.ANCHO_VENTANA - 40, 680, 40, constantes.ALTO_VENTANA - 680),
    pygame.Rect(0, constantes.ALTO_VENTANA - 40, constantes.ANCHO_VENTANA, 40)
]

# salida superior a mapa 2
salida_mapa3 = pygame.Rect(0, 0, constantes.ANCHO_VENTANA, 40)

# salida izquierda a nuevo mapa 4
salida_mapa3_izquierda = pygame.Rect(0, 320, 40, 440)

# salida derecha a nuevo mapa 7
salida_mapa3_derecha = pygame.Rect(constantes.ANCHO_VENTANA - 40, 420, 40, 260)

# salida inferior a nuevo mapa 8
salida_mapa3_abajo = pygame.Rect(0, constantes.ALTO_VENTANA - 40, constantes.ANCHO_VENTANA, 40)

# mapa 4: nuevo mapa a la izquierda de mapa 3
# pared izquierda dividida para dejar abierta la puerta izquierda
# pared derecha dividida para dejar abierta la puerta derecha
paredes_mapa4 = [
    pygame.Rect(100, -40, 90, 360),    # pared izquierda superior
    pygame.Rect(100, 780, 90, 876),    # pared izquierda inferior
    pygame.Rect(3528, -40, 180, 480),  # pared derecha superior
    pygame.Rect(3528, 700, 180, 860),  # pared derecha inferior
    pygame.Rect(100, -40, 3702, 162),  # pared superior
    pygame.Rect(100, 1676, 3702, 120)  # pared inferior
]

# salida izquierda de mapa 4 hacia nuevo mapa 5
salida_mapa4_izquierda = pygame.Rect(100, 340, 40, 440)

# salida derecha de retorno a mapa 3
salida_mapa4_derecha = pygame.Rect(3528, 440, 40, 260)

# mapa 5: nueva zona a la izquierda de mapa 4
paredes_mapa5 = [
    pygame.Rect(0, 0, 40, 320),
    pygame.Rect(0, 320, 40, 440),
    pygame.Rect(0, 760, 40, constantes.ALTO_VENTANA - 760),
    pygame.Rect(constantes.ANCHO_VENTANA - 40, 0, 40, 320),
    pygame.Rect(constantes.ANCHO_VENTANA - 40, 760, 40, constantes.ALTO_VENTANA - 760),
    pygame.Rect(0, 0, constantes.ANCHO_VENTANA, 40),
    pygame.Rect(0, constantes.ALTO_VENTANA - 40, constantes.ANCHO_VENTANA, 40)
]


# salida derecha de retorno a mapa 4
salida_mapa5 = pygame.Rect(constantes.ANCHO_VENTANA - 40, 420, 40, 260)



# mapa 7: nueva zona a la derecha de mapa 3
zona_colision_mapa7_superior = pygame.Rect(40, 40, constantes.ANCHO_VENTANA - 80, 240)
zona_colision_mapa7 = pygame.Rect(40, 680, 1360, 360)
paredes_mapa7 = [
    pygame.Rect(0, 0, 40, 420),
    pygame.Rect(0, 680, 40, constantes.ALTO_VENTANA - 680),
    pygame.Rect(constantes.ANCHO_VENTANA - 40, 0, 40, constantes.ALTO_VENTANA - 40),
    pygame.Rect(0, 0, constantes.ANCHO_VENTANA, 40),
    pygame.Rect(40, constantes.ALTO_VENTANA - 40, 2610, 40),
    zona_colision_mapa7,
    zona_colision_mapa7_superior
]

# salida izquierda de retorno a mapa 3
salida_mapa7 = pygame.Rect(0, 420, 40, 260)

# salida inferior hacia el nuevo mapa
salida_mapa7_abajo = pygame.Rect(1440, constantes.ALTO_VENTANA - 40, 480, 40)

# nuevo mapa 9: zona debajo de mapa 7
paredes_mapa9 = [
    pygame.Rect(0, 0, 40, constantes.ALTO_VENTANA),
    pygame.Rect(constantes.ANCHO_VENTANA - 40, 0, 40, constantes.ALTO_VENTANA),
    pygame.Rect(40, 0, 1440, 40),
    pygame.Rect(0, constantes.ALTO_VENTANA - 40, constantes.ANCHO_VENTANA, 40),
    pygame.Rect(1600, 700, 320, 380)
]

# entrada superior de retorno a mapa 7
salida_mapa9 = pygame.Rect(1440, 0, 480, 40)

# mapa 8: nueva zona abajo de mapa 3
paredes_mapa8 = [
    pygame.Rect(0, 0, 40, constantes.ALTO_VENTANA),
    pygame.Rect(constantes.ANCHO_VENTANA - 40, 0, 40, constantes.ALTO_VENTANA),
    pygame.Rect(0, 0, 1120, 40),
    pygame.Rect(1380, 0, constantes.ANCHO_VENTANA - 1380, 40),
    pygame.Rect(0, constantes.ALTO_VENTANA - 40, constantes.ANCHO_VENTANA, 40)
]

# salida superior de retorno a mapa 3
salida_mapa8 = pygame.Rect(1120, 0, 260, 40)

paredes_edificio = [

    pygame.Rect(0, 0, 600, 20),      # arriba
    pygame.Rect(0, 0, 20, 216),      # izquierda
    pygame.Rect(580, 0, 20, 216),    # derecha
    pygame.Rect(0, 196, 600, 20)     # abajo

]

puerta_izquierda = pygame.Rect(
    0,
    80,
    20,
    60
)

puerta_derecha = pygame.Rect(
    580,
    80,
    20,
    60
)

puerta_arriba = pygame.Rect(
    260,
    0,
    80,
    20
)
