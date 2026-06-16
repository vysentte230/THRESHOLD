import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

import pygame
import math
import constantes
from personaje import Personaje
import mapas
from bus import Bus
#hola brayan
pygame.init()
pygame.mixer.init()


#aqui hace spawn
jugador = Personaje(constantes.ANCHO_VENTANA // 2, 200)
bus = Bus(1800, -300)

fondo_menu = pygame.image.load("assets//images/Menu//Menu.png")
pygame.mixer.music.load("assets//music//musica//EmptyTown_DELTARUNE.mp3")
pygame.mixer.music.play(-1) 


fondo_menu = pygame.transform.scale(fondo_menu,( constantes.ANCHO_VENTANA,constantes.ALTO_VENTANA))

ventana = pygame.Surface((constantes.ANCHO_VENTANA, constantes.ALTO_VENTANA))
pantalla = pygame.display.set_mode((constantes.ANCHO_PANTALLA, constantes.ALTO_PANTALLA))

pygame.display.set_caption("Threshold")


# Configuración mapa 1

MAPA1_SCALE_X = 1.0
MAPA1_SCALE_Y = 1.0

MAPA1_OFFSET_X = 0
MAPA1_OFFSET_Y = 0

mapa1_img = pygame.transform.scale(
    mapas.mapa1_img,
    (
        int(constantes.ANCHO_VENTANA * MAPA1_SCALE_X),
        int(constantes.ALTO_VENTANA * MAPA1_SCALE_Y)
    )
)

mapa1_w, mapa1_h = mapa1_img.get_size()


# Configuración del mapa 4
MAPA4_SCALE_X = 2.60
MAPA4_SCALE_Y = 1.9
MAPA4_OFFSET_X = 100
MAPA4_OFFSET_Y = -60
mapa4_img = pygame.transform.scale(
    mapas.mapa_edificio,
    (
        int(constantes.ANCHO_VENTANA * MAPA4_SCALE_X),
        int(constantes.ALTO_VENTANA * MAPA4_SCALE_Y)
    )
)
mapa4_w, mapa4_h = mapa4_img.get_size()

estado_juego = "menu"

# varibles movimiento
mover_arriba = False
mover_abajo = False
mover_izquierda = False
mover_derecha = False

# controlar frame rate
reloj = pygame.time.Clock()

#fuentes para crear letras :p
fuente_titulo = pygame.font.SysFont("assets/fonts/PressStart2p.ttf",120)
fuente_boton = pygame.font.SysFont("assets/fonts/PressStart2p.ttf",50)

def render_pixelado(fuente, texto, color, factor=3):
    superficie = fuente.render(texto, False, color)
    w, h = superficie.get_size()
    pequena = pygame.transform.scale(superficie, (max(1, w // factor), max(1, h // factor)))
    return pygame.transform.scale(pequena, (w, h))

def dibujar_texto_glow(ventana, texto, fuente, color, pos, intensidad=4, alpha_glow=40, factor_pixel=3):
    x, y = pos
    superficie = render_pixelado(fuente, texto, color, factor_pixel)
    superficie_glow = superficie.copy()
    superficie_glow.set_alpha(alpha_glow)

    offsets = [
        (-intensidad, 0), (intensidad, 0), (0, -intensidad), (0, intensidad),
        (-intensidad, -intensidad), (intensidad, intensidad),
        (-intensidad, intensidad), (intensidad, -intensidad)
    ]
    for dx, dy in offsets:
        ventana.blit(superficie_glow, (x + dx, y + dy))

    ventana.blit(superficie, (x, y))


def obtener_variables_mapa(mapa):
    salida_abajo = None
    salida_izquierda = None

    if mapa == 1:
        paredes = mapas.paredes_mapa1
        salida = mapas.salida_mapa1
    elif mapa == 2:
        paredes = mapas.paredes_mapa2
        salida = mapas.salida_mapa2
        salida_abajo = mapas.salida_mapa2_abajo
    elif mapa == 3:
        paredes = mapas.paredes_mapa3
        salida = mapas.salida_mapa3
        salida_izquierda = mapas.salida_mapa3_izquierda
        salida_abajo = mapas.salida_mapa3_abajo
    elif mapa == 4:
        paredes = mapas.paredes_mapa4
        salida = mapas.salida_mapa4_derecha
        salida_izquierda = mapas.salida_mapa4_izquierda
    elif mapa == 5:
        paredes = mapas.paredes_mapa5
        salida = mapas.salida_mapa5
    elif mapa == 6:
        paredes = mapas.paredes_oficina_profesores
        salida = mapas.salida_oficina_profesores
    elif mapa == 7:
        paredes = mapas.paredes_mapa7
        salida = mapas.salida_mapa7
        salida_abajo = mapas.salida_mapa7_abajo
    elif mapa == 8:
        paredes = mapas.paredes_mapa8
        salida = mapas.salida_mapa8
    elif mapa == 9:
        paredes = mapas.paredes_mapa9
        salida = mapas.salida_mapa9
    elif mapa == 10:
        paredes = mapas.paredes_edificio
        salida = mapas.puerta_izquierda
    else:
        paredes = mapas.paredes_mapa1
        salida = mapas.salida_mapa1

    return paredes, salida, salida_izquierda, salida_abajo


def posicionar_jugador_entrada(salida_rect, lado, jugador):
    if lado == "arriba":
        jugador.forma.centerx = salida_rect.centerx
        jugador.forma.centery = salida_rect.bottom + jugador.forma.height // 2 + 30
    elif lado == "abajo":
        jugador.forma.centerx = salida_rect.centerx
        jugador.forma.centery = salida_rect.top - jugador.forma.height // 2 - 30
    elif lado == "izquierda":
        jugador.forma.centerx = salida_rect.right + jugador.forma.width // 2 + 30
        jugador.forma.centery = salida_rect.centery
    elif lado == "derecha":
        jugador.forma.centerx = salida_rect.left - jugador.forma.width // 2 - 30
        jugador.forma.centery = salida_rect.centery

run = True
mostrar_hitbox = False
cooldown_mapa = 0

while run == True:

    # indicar que vaya a 60 fps
    reloj.tick(constantes.FPS)

    if cooldown_mapa > 0:
      cooldown_mapa -= 1

    ventana.fill(constantes.COLOR_BG)

    if estado_juego == "menu":
     ventana.blit(fondo_menu, (0, 0))

     colores_titulo = [
         (170,178,204), (154,160,200), (140,140,192), (144,112,176),
         (160,92,152), (176,76,120), (194,60,88), (210,44,60), (232,32,44)
     ]
     texto = "THRESHOLD"
     x_inicial = constantes.ANCHO_VENTANA // 2 - 320
     tiempo = pygame.time.get_ticks()
     pulso = int(30 + ((math.sin(tiempo / 300) + 1) / 2) * 100)
     for i, letra in enumerate(texto):
         dibujar_texto_glow(ventana, letra, fuente_titulo, colores_titulo[i], (x_inicial + i * 70, 180), alpha_glow=pulso)

     mouse_real = pygame.mouse.get_pos()
     mouse_pos = (
         mouse_real[0] * constantes.ANCHO_VENTANA // constantes.ANCHO_PANTALLA,
         mouse_real[1] * constantes.ALTO_VENTANA // constantes.ALTO_PANTALLA
     )

     boton_jugar = pygame.Rect(constantes.ANCHO_VENTANA//2 - 150, 420, 300, 60)
     color_jugar = (255,255,255) if boton_jugar.collidepoint(mouse_pos) else (184,188,224)
     if boton_jugar.collidepoint(mouse_pos):
         puntos_j = [
             (boton_jugar.x - 30, boton_jugar.y + 10),
             (boton_jugar.x - 30, boton_jugar.y + 30),
             (boton_jugar.x - 10, boton_jugar.y + 20)
         ]
         pygame.draw.polygon(ventana, color_jugar, puntos_j)
     if boton_jugar.collidepoint(mouse_pos):
         dibujar_texto_glow(ventana, "JUGAR", fuente_boton, color_jugar, (boton_jugar.x + 30, boton_jugar.y + 10), intensidad=2)
     else:
         texto_jugar = render_pixelado(fuente_boton, "JUGAR", color_jugar)
         ventana.blit(texto_jugar, (boton_jugar.x + 30, boton_jugar.y + 10))

     boton_salir = pygame.Rect(constantes.ANCHO_VENTANA//2 - 150, 570, 300, 60)
     color_salir = (255,80,80) if boton_salir.collidepoint(mouse_pos) else (144,88,88)
     if boton_salir.collidepoint(mouse_pos):
         puntos_s = [
             (boton_salir.x - 30, boton_salir.y + 10),
             (boton_salir.x - 30, boton_salir.y + 30),
             (boton_salir.x - 10, boton_salir.y + 20)
         ]
         pygame.draw.polygon(ventana, color_salir, puntos_s)
     if boton_salir.collidepoint(mouse_pos):
         dibujar_texto_glow(ventana, "SALIR", fuente_boton, color_salir, (boton_salir.x + 30, boton_salir.y + 10), intensidad=2)
     else:
         texto_salir = render_pixelado(fuente_boton, "SALIR", color_salir)
         ventana.blit(texto_salir, (boton_salir.x + 30, boton_salir.y + 10))
    
    elif estado_juego == "jugando":

        ventana.fill((10, 10, 70))

        velocidad_actual = constantes.VELOCIDAD

        delta_x = 0
        delta_y = 0

        if mover_arriba:
            delta_y = -velocidad_actual

        if mover_abajo:
            delta_y = velocidad_actual

        if mover_izquierda:
            delta_x = -velocidad_actual

        if mover_derecha:
            delta_x = velocidad_actual

        salida_abajo = None
        salida_izquierda = None

        paredes, salida, salida_izquierda, salida_abajo = obtener_variables_mapa(mapas.mapa_actual)

        if mapas.mapa_actual == 1:
            bus.mover()
            bus.animar()
            if jugador.forma.colliderect(bus.rect):
                velocidad_actual = 2

        paredes_con_bus = paredes.copy()
        if mapas.mapa_actual == 1:
            paredes_con_bus.append(bus.rect)

        jugador.movimiento(delta_x, delta_y, paredes_con_bus)

        # cambiar mapa
        cambio_mapa = False
        if cooldown_mapa == 0:
            if mapas.mapa_actual == 1 and jugador.forma.colliderect(salida):
                mapas.mapa_actual = 2
                posicionar_jugador_entrada(mapas.salida_mapa2, "arriba", jugador)
                cooldown_mapa = 30
                cambio_mapa = True
            elif mapas.mapa_actual == 2:
                if jugador.forma.colliderect(salida):
                    mapas.mapa_actual = 1
                    posicionar_jugador_entrada(mapas.salida_mapa1, "abajo", jugador)
                    cooldown_mapa = 30
                    cambio_mapa = True
                elif jugador.forma.colliderect(salida_abajo):
                    mapas.mapa_actual = 3
                    posicionar_jugador_entrada(mapas.salida_mapa3, "arriba", jugador)
                    cooldown_mapa = 30
                    cambio_mapa = True
            elif mapas.mapa_actual == 3:
                if jugador.forma.colliderect(salida):
                    mapas.mapa_actual = 2
                    posicionar_jugador_entrada(mapas.salida_mapa2_abajo, "abajo", jugador)
                    cooldown_mapa = 30
                    cambio_mapa = True
                elif jugador.forma.colliderect(salida_izquierda):
                    mapas.mapa_actual = 4
                    posicionar_jugador_entrada(mapas.salida_mapa4_derecha, "derecha", jugador)
                    cooldown_mapa = 30
                    cambio_mapa = True
                elif jugador.forma.colliderect(mapas.salida_mapa3_derecha):
                    mapas.mapa_actual = 7
                    posicionar_jugador_entrada(mapas.salida_mapa7, "izquierda", jugador)
                    cooldown_mapa = 30
                    cambio_mapa = True
                elif jugador.forma.colliderect(salida_abajo):
                    mapas.mapa_actual = 8
                    posicionar_jugador_entrada(mapas.salida_mapa8, "arriba", jugador)
                    cooldown_mapa = 30
                    cambio_mapa = True
            elif mapas.mapa_actual == 4:
                if jugador.forma.colliderect(salida):
                    mapas.mapa_actual = 3
                    posicionar_jugador_entrada(mapas.salida_mapa3_izquierda, "izquierda", jugador)
                    cooldown_mapa = 30
                    cambio_mapa = True
                elif jugador.forma.colliderect(salida_izquierda):
                    mapas.mapa_actual = 5
                    posicionar_jugador_entrada(mapas.salida_mapa5, "derecha", jugador)
                    cooldown_mapa = 30
                    cambio_mapa = True
                elif jugador.forma.colliderect(mapas.salida_mapa4_oficina):
                    mapas.mapa_actual = 6
                    posicionar_jugador_entrada(mapas.salida_oficina_profesores, "abajo", jugador)
                    cooldown_mapa = 30
                    cambio_mapa = True
            elif mapas.mapa_actual == 5 and jugador.forma.colliderect(salida):
                mapas.mapa_actual = 4
                posicionar_jugador_entrada(mapas.salida_mapa4_izquierda, "izquierda", jugador)
                cooldown_mapa = 30
                cambio_mapa = True
            elif mapas.mapa_actual == 6 and jugador.forma.colliderect(salida):
                mapas.mapa_actual = 4
                posicionar_jugador_entrada(mapas.salida_mapa4_oficina, "arriba", jugador)
                cooldown_mapa = 30
                cambio_mapa = True
            elif mapas.mapa_actual == 7 and jugador.forma.colliderect(salida):
                mapas.mapa_actual = 3
                posicionar_jugador_entrada(mapas.salida_mapa3_derecha, "derecha", jugador)
                cooldown_mapa = 30
                cambio_mapa = True
            elif mapas.mapa_actual == 7 and jugador.forma.colliderect(salida_abajo):
                mapas.mapa_actual = 9
                posicionar_jugador_entrada(mapas.salida_mapa9, "arriba", jugador)
                cooldown_mapa = 30
                cambio_mapa = True
            elif mapas.mapa_actual == 8 and jugador.forma.colliderect(salida):
                mapas.mapa_actual = 3
                posicionar_jugador_entrada(mapas.salida_mapa3_abajo, "abajo", jugador)
                cooldown_mapa = 30
                cambio_mapa = True
            elif mapas.mapa_actual == 9 and jugador.forma.colliderect(salida):
                mapas.mapa_actual = 7
                posicionar_jugador_entrada(mapas.salida_mapa7, "izquierda", jugador)
                cooldown_mapa = 30
                cambio_mapa = True
            elif mapas.mapa_actual == 10 and jugador.forma.colliderect(salida):
                mapas.mapa_actual = 3
                posicionar_jugador_entrada(mapas.salida_mapa3_derecha, "derecha", jugador)
                cooldown_mapa = 30
                cambio_mapa = True

        if cambio_mapa:
            mover_arriba = mover_abajo = mover_izquierda = mover_derecha = False
            paredes, salida, salida_izquierda, salida_abajo = obtener_variables_mapa(mapas.mapa_actual)
            paredes_con_bus = paredes.copy()
            if mapas.mapa_actual == 1:
                paredes_con_bus.append(bus.rect)

        if mapas.mapa_actual == 1:

            # Cámara mapa 1
            camera_x = jugador.forma.centerx - constantes.ANCHO_VENTANA // 2
            camera_y = jugador.forma.centery - constantes.ALTO_VENTANA // 2

            camera_x = max(
                MAPA1_OFFSET_X,
                min(camera_x, MAPA1_OFFSET_X + mapa1_w - constantes.ANCHO_VENTANA)
            )

            camera_y = max(
                MAPA1_OFFSET_Y,
                min(camera_y, MAPA1_OFFSET_Y + mapa1_h - constantes.ALTO_VENTANA)
            )

            ventana.fill((0, 0, 0))
            ventana.blit(
                mapa1_img,
                (MAPA1_OFFSET_X - camera_x, MAPA1_OFFSET_Y - camera_y)
            )

        elif mapas.mapa_actual == 4:

            # Cámara mapa 4
            camera_x = jugador.forma.centerx - constantes.ANCHO_VENTANA // 2
            camera_y = jugador.forma.centery - constantes.ALTO_VENTANA // 2

            camera_x = max(
                MAPA4_OFFSET_X,
                min(camera_x, MAPA4_OFFSET_X + mapa4_w - constantes.ANCHO_VENTANA)
            )

            camera_y = max(
                MAPA4_OFFSET_Y,
                min(camera_y, MAPA4_OFFSET_Y + mapa4_h - constantes.ALTO_VENTANA)
            )

            ventana.fill((0, 0, 0))
            ventana.blit(
                mapa4_img,
                (MAPA4_OFFSET_X - camera_x, MAPA4_OFFSET_Y - camera_y)
            )

        else:
            camera_x = 0
            camera_y = 0

        # dibujar paredes mas colisiones
        for pared in paredes:

            # No dibujar paredes grises en el edificio ni en mapa 4
            if mapas.mapa_actual != 10 and mapas.mapa_actual != 4:
                pygame.draw.rect(
                    ventana,
                    (150, 150, 150),
                    pared
                )

               # mostrar hitbox paredes
            if mostrar_hitbox:
                if mapas.mapa_actual == 1 or mapas.mapa_actual == 4:
                    pygame.draw.rect(
                        ventana,
                        (255, 0, 0),
                        pygame.Rect(pared.x - camera_x, pared.y - camera_y, pared.width, pared.height),
                        3
                    )
                else:
                    pygame.draw.rect(
                        ventana,
                        (255, 0, 0),
                        pared,
                        3
                    )
                   
        if mapas.mapa_actual == 1:

           bus.dibujar(ventana)

           if mostrar_hitbox:

            pygame.draw.rect(
                ventana,
                (255, 255, 0),
                bus.rect,
                4
            )
    
        # dibujar jugador
        if mapas.mapa_actual == 1 or mapas.mapa_actual == 4:
            ventana.blit(
                jugador.image,
                (
                    jugador.forma.x - jugador.sprite_offset.x - camera_x,
                    jugador.forma.y - jugador.sprite_offset.y - camera_y
                )
            )
        else:
            ventana.blit(
                jugador.image,
                (
                    jugador.forma.x - jugador.sprite_offset.x,
                    jugador.forma.y - jugador.sprite_offset.y
                )
            )
        # hitbox jugador
        if mostrar_hitbox:
            if mapas.mapa_actual == 1 or mapas.mapa_actual == 4:
                pygame.draw.rect(
                    ventana,
                    (0, 255, 0),
                    pygame.Rect(
                        jugador.forma.x - camera_x,
                        jugador.forma.y - camera_y,
                        jugador.forma.width,
                        jugador.forma.height
                    ),
                    4
                )
            else:
                pygame.draw.rect(
                    ventana,
                    (0, 255, 0),
                    jugador.forma,
                    4
                )
            
            # Dibujar hitbox de salidas en modo debug
            if mapas.mapa_actual == 4:
                # Dibujar hitbox de salida derecha
                pygame.draw.rect(
                    ventana,
                    (0, 0, 255),
                    pygame.Rect(
                        salida.x - camera_x,
                        salida.y - camera_y,
                        salida.width,
                        salida.height
                    ),
                    3
                )

                # Dibujar hitbox de salida izquierda
                pygame.draw.rect(
                    ventana,
                    (0, 0, 255),
                    pygame.Rect(
                        salida_izquierda.x - camera_x,
                        salida_izquierda.y - camera_y,
                        salida_izquierda.width,
                        salida_izquierda.height
                    ),
                    3
                )

            else:
                # Dibujar hitbox de salida principal para otros mapas
                pygame.draw.rect(
                    ventana,
                    (0, 0, 255),
                    salida,
                    3
                )
                
                # Dibujar salida_abajo si existe
                if salida_abajo is not None:
                    pygame.draw.rect(
                        ventana,
                        (0, 0, 255),
                        salida_abajo,
                        3
                    )
                
                # Dibujar salida_izquierda si existe
                if salida_izquierda is not None:
                    pygame.draw.rect(
                        ventana,
                        (0, 0, 255),
                        salida_izquierda,
                        3
                    )

    
    for event in pygame.event.get():

        # cerrar ventana
        if event.type == pygame.QUIT:
            run = False

        if estado_juego == "menu":
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_real = event.pos
                mouse_pos = (
                    mouse_real[0] * constantes.ANCHO_VENTANA // constantes.ANCHO_PANTALLA,
                    mouse_real[1] * constantes.ALTO_VENTANA // constantes.ALTO_PANTALLA
                )
                if boton_jugar.collidepoint(mouse_pos):
                    pygame.mixer.music.load("assets//music//musica//Awake_Celeste.mp3")
                    pygame.mixer.music.play(-1)
                    estado_juego = "jugando"
                elif boton_salir.collidepoint(mouse_pos):
                    run = False

        if estado_juego == "jugando":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    mostrar_hitbox = not mostrar_hitbox
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    mover_izquierda = True
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    mover_derecha = True
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    mover_arriba = True
                if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    mover_abajo = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    mover_izquierda = False
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    mover_derecha = False
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    mover_arriba = False
                if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    mover_abajo = False

    escalado = pygame.transform.scale(ventana, (constantes.ANCHO_PANTALLA, constantes.ALTO_PANTALLA))
    pantalla.blit(escalado, (0, 0))
    pygame.display.update()
pygame.quit()