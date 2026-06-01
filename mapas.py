import pygame
import constantes

mapa_actual = 1

#mapa n1


paredes_mapa1 = [

    # arriba
    pygame.Rect(0, 0, constantes.ANCHO_VENTANA, 40),

    # izquierda
    pygame.Rect(0, 0, 40, constantes.ALTO_VENTANA),

    # derecha
    pygame.Rect(constantes.ANCHO_VENTANA - 40, 0, 40, constantes.ALTO_VENTANA),

    # abajo izquierda
    pygame.Rect( 0, constantes.ALTO_VENTANA - 40, 700, 40),

    # abajo derecha
    pygame.Rect( 1200, constantes.ALTO_VENTANA - 40, 800, 40)

]

# hueco / salida del mapa 1
salida_mapa1 = pygame.Rect(700, constantes.ALTO_VENTANA - 40, 500, 40)


#mapa n2


paredes_mapa2 = [

    # abajo
    pygame.Rect( 0, constantes.ALTO_VENTANA - 40, constantes.ANCHO_VENTANA, 40 ),

    # izquierda
    pygame.Rect(0, 0, 40, constantes.ALTO_VENTANA),

    # derecha
    pygame.Rect( constantes.ANCHO_VENTANA - 40, 0, 40, constantes.ALTO_VENTANA),

    # arriba izquierda
    pygame.Rect(0, 0, 700, 40),

    # arriba derecha
    pygame.Rect(1200, 0, constantes.ANCHO_VENTANA - 1200, 40),

    ]

#salida mapa2
salida_mapa2 = pygame.Rect( 700, 0, 500, 40)