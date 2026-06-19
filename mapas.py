import pygame
import constantes

mapa_actual = 1

#PARADERO
mapa1_img = pygame.image.load(
    "assets/images/Map/Paradero.png"
)

#DONDE ESTAN LAS LETRAS ULAGOS
mapa2_img = pygame.image.load(
    "assets/images/Map/Entrada_universidad.png"
)

#SI
mapa3_img = pygame.image.load(
    "assets/images/Map/Entrada_u2.png"
)

#este es el mapa4 ENTRADA EDIFICIO IZQUIERDO
mapa_edificio = pygame.image.load(
    "assets/images/Map/Edificio1_1.png"
)

#ESTE ES EL PASILLO DEL EDIFICIO IZQUIERDO
mapa5_img = pygame.image.load(
    "assets/images/Map/Pasillo.png"
)

#LA OFICINA DE PROFESORES
mapa6_img = pygame.image.load(
    "assets/images/Map/Oficina_profesores.png"
)

#ENTRADA EDIFICIO DERECHA
mapa7_img = pygame.image.load(
    "assets/images/Map/Edificio2.png"
)

#AQUI IRA LA BIBLIOTECA pero aun no se termina
#mapa8_img = pygame.image.load(
#    "assets/images/Map/.png"
#)

#LAS ESCALERAS
mapa9_img = pygame.image.load(
    "assets/images/Map/Escaleras.png"
)

#Segundo piso
mapa10_img = pygame.image.load(
    "assets/images/Map/Segundo_piso.png"
)

#Mapa del patio central
paredes_mapa1 = [
    pygame.Rect(0, 0, constantes.ANCHO_VENTANA, 40),
    pygame.Rect(0, 0, 40, constantes.ALTO_VENTANA),
    pygame.Rect(constantes.ANCHO_VENTANA - 40, 0, 40, constantes.ALTO_VENTANA),
    pygame.Rect(0, constantes.ALTO_VENTANA - 40, 700, 40),
    pygame.Rect(1200, constantes.ALTO_VENTANA - 40, 720, 40),

    # arboleda de flores amarillas (zona oscura izquierda) - límite total
    pygame.Rect(0, 0, 1040, 1080),

    # paradero (caseta azul)
    pygame.Rect(1165, 40, 290, 330),

    # carretera (franja gris diagonal) - bloqueada por tramos
    pygame.Rect(1430, 0, 490, 200),
    pygame.Rect(1550, 200, 370, 250),
    pygame.Rect(1650, 450, 270, 300),
    pygame.Rect(1750, 750, 170, 330),
]

# salida del mapa 1 hacia el patio central
salida_mapa1 = pygame.Rect(700, constantes.ALTO_VENTANA - 40, 500, 40)

# mapa 2: primera zona verde
paredes_mapa2 = [
    pygame.Rect(0, 0, 700, 40),
    pygame.Rect(1200, 0, constantes.ANCHO_VENTANA - 1200, 40),
    pygame.Rect(0, 0, 40, constantes.ALTO_VENTANA),
    pygame.Rect(constantes.ANCHO_VENTANA - 40, 0, 40, constantes.ALTO_VENTANA),
    pygame.Rect(800, 600, 300, 200), #logo ulagos
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
    # pared diagonal
    pygame.Rect(3180, 1500, 40, 40),
    pygame.Rect(3220, 1430, 40, 40),
    pygame.Rect(3270, 1360, 40, 40),
    pygame.Rect(3310, 1290, 40, 40),
    pygame.Rect(3360, 1220, 40, 40),
    pygame.Rect(3390, 1150, 40, 40),
    pygame.Rect(3430, 1080, 40, 40),
    pygame.Rect(3470, 1010, 40, 40),
    pygame.Rect(3510, 940, 40, 40),

    pygame.Rect(200, 940, 1455, 1000), #pared aula magna
    pygame.Rect(200, 750, 240, 240), #entrada izquuierda aula magna
    pygame.Rect(1341, 750, 314, 300), #entrada derecha aula magna

     pygame.Rect(1790, 960, 120, 220), #escritorio

    pygame.Rect(100, -20, 74, 360),    # pared izquierda superior
    pygame.Rect(100, 650, 74, 876),    # pared izquierda inferior
    pygame.Rect(3478, -120, 180, 480),  # pared derecha superior
    pygame.Rect(3478, 650, 180, 860),  # pared derecha inferior
    pygame.Rect(100, 122, 1855, 40),   # pared superior (izquierda de la puerta)
    pygame.Rect(2280, 122, 2655, 40),  # pared superior (derecha de la puerta)

    
    pygame.Rect(100, 1540, 3702, 120)  # pared inferior
    
]

# salida izquierda de mapa 4 hacia nuevo mapa 5
salida_mapa4_izquierda = pygame.Rect(100, 340, 40, 440)

# salida derecha de retorno a mapa 3
salida_mapa4_derecha = pygame.Rect(3528, 440, 40, 260)

# salida superior de mapa 4 hacia la oficina de profesores (mapa 6)
salida_mapa4_arriba = pygame.Rect(1955, 80, 324, 80)

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


# mapa 6: oficina de profesores (mapa con cámara libre, tamaño 3840x2160)
MAPA6_ANCHO = 3840
MAPA6_ALTO = 2160

paredes_oficina_profesores = [
    # bordes externos
    pygame.Rect(0, 0, MAPA6_ANCHO, 30),                      # pared superior
    pygame.Rect(0, 0, 30, MAPA6_ALTO),                       # pared izquierda
    pygame.Rect(MAPA6_ANCHO - 30, 0, 30, MAPA6_ALTO),        # pared derecha
    pygame.Rect(0, MAPA6_ALTO - 30, 1700, 30),                    # pared inferior izquierda
    pygame.Rect(2140, MAPA6_ALTO - 30, MAPA6_ANCHO - 2140, 30),   # pared inferior derecha

    # columna central en T que separa los dos cubículos
    pygame.Rect(1794, 824, 249, 1270),

    # borde inferior del pasillo (deja hueco donde está la columna central)
    pygame.Rect(0, 824, 1794, 26),
    pygame.Rect(2043, 824, 1797, 26),

    # muebles del pasillo superior
    pygame.Rect(986, 420, 129, 226),    # extintor rojo
    pygame.Rect(2230, 679, 420, 162),   # mesa con impresora
    pygame.Rect(2780, 420, 113, 291),   # dispensador de agua
    pygame.Rect(2958, 420, 162, 291),   # archivero negro

    # muebles cubículo izquierdo
    pygame.Rect(1164, 937, 226, 162),   # cajonera/mueble arriba
    pygame.Rect(1455, 1600, 323, 291),  # escritorio con silla

    # muebles cubículo derecho
    pygame.Rect(2036, 1600, 323, 291),  # escritorio con silla
]

# puerta de entrada a oficina de profesores (parte superior del mapa 4)
salida_mapa4_oficina = pygame.Rect(
    2450,  # X
    0,     # Y
    180,   # ancho
    40     # alto
)

# salida inferior de oficina de profesores (entre los dos cubículos)
salida_oficina_profesores = pygame.Rect(1700, MAPA6_ALTO - 60, 440, 60)


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
