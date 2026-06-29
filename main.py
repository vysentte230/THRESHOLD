import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
import pygame
import math
import constantes
import random
from personaje import Personaje
import mapas
from bus import Bus
from joel import Joel
from segovia import Segovia


pygame.init()
pygame.mixer.init()

MUSICA_MENU = "assets//music//musica//Titulo_chill.mp3"
MUSICA_JUEGO = "assets//music//musica//Primer_dia.mp3"
MUSICA_MAPA6 = "assets//music//musica//Brilliant Red.mp3"
MUSICA_MAPA7 = "assets//music//musica//biblioteca_ost.mp3"
MUSICA_MINIJUEGO = "assets//music//musica//chill_game.mp3"
musica_actual = MUSICA_MENU
musica_anterior = None

#esto es para el boton de pausa
pausa = False
musica_silenciada = False

boton_reanudar = pygame.Rect(0, 0, 0, 0)
boton_musica = pygame.Rect(0, 0, 0, 0)
boton_menu = pygame.Rect(0, 0, 0, 0)
boton_salir_juego = pygame.Rect(0, 0, 0, 0)

logo_ulagos = pygame.transform.scale(
mapas.ulagos_img,
(300, 200)
)


def reproducir_musica(ruta, loop=-1, inicio=0):
    pygame.mixer.music.load(ruta)
    pygame.mixer.music.play(loop, start=inicio)


#aqui hace spawn
jugador = Personaje(1450, 550)
bus = Bus(1500, -300)
joel = Joel(100, 700)
segovia = Segovia(100, 1050)

fondo_menu = pygame.image.load("assets//images/Menu//Menu.png")
reproducir_musica(MUSICA_MENU)


fondo_menu = pygame.transform.scale(fondo_menu,( constantes.ANCHO_VENTANA,constantes.ALTO_VENTANA))

biblioteca_img = pygame.transform.scale(
    pygame.image.load("assets/images/Map/biblioteca_minijuego.png"),
    (constantes.ANCHO_VENTANA, constantes.ALTO_VENTANA)
)

# Hitboxes de los libros en pantalla (1920x1080)
def generar_libros():
    libros = []
    filas = [
        {"y": 109, "h": 183},
        {"y": 309, "h": 181},
        {"y": 503, "h": 181},
        {"y": 700, "h": 219},
    ]
    secciones = [
        {"x_inicio": 67, "cantidad": 16},
        {"x_inicio": 660, "cantidad": 16},
        {"x_inicio": 1272, "cantidad": 16},
    ]
    for fila in filas:
        for seccion in secciones:
            x = seccion["x_inicio"]
            for _ in range(seccion["cantidad"]):
                libros.append(pygame.Rect(x, fila["y"], 34, fila["h"]))
                x += 36
    return libros

libros_hitboxes = generar_libros()

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

# Configuración mapa 5
MAPA5_SCALE_X = 1.0
MAPA5_SCALE_Y = 1.0

mapa5_img = pygame.transform.scale(
    mapas.mapa5_img,
    (
        int(constantes.ANCHO_VENTANA * MAPA5_SCALE_X),
        int(constantes.ALTO_VENTANA * MAPA5_SCALE_Y)
    )
)
mapa4_w, mapa4_h = mapa4_img.get_size()

# Configuración mapa 6 (doble de pantalla para cámara libre)
MAPA6_SCALE_X = 2.0
MAPA6_SCALE_Y = 2.0
MAPA6_OFFSET_X = 0
MAPA6_OFFSET_Y = 0

# Configuración mapa 5 (pasillo, cámara libre)
MAPA5_SCALE_X = 2.0
MAPA5_SCALE_Y = 2.0
MAPA5_OFFSET_X = 0
MAPA5_OFFSET_Y = 0

mapa5_img = pygame.transform.scale(
    mapas.mapa5_img,
    (
        int(constantes.ANCHO_VENTANA * MAPA5_SCALE_X),
        int(constantes.ALTO_VENTANA * MAPA5_SCALE_Y)
    )
)
mapa5_w, mapa5_h = mapa5_img.get_size()

mapa6_img = pygame.transform.scale(
    mapas.mapa6_img,
    (
        int(constantes.ANCHO_VENTANA * MAPA6_SCALE_X),
        int(constantes.ALTO_VENTANA * MAPA6_SCALE_Y)
    )
)

mapa6_w, mapa6_h = mapa6_img.get_size()

# Configuración mapa 7 (cámara libre)
MAPA7_SCALE_X = 1.7
MAPA7_SCALE_Y = 1.7
MAPA7_OFFSET_X = 0
MAPA7_OFFSET_Y = 0

mapa7_img = pygame.transform.scale(
    mapas.mapa7_img,
    (int(constantes.ANCHO_VENTANA * MAPA7_SCALE_X),
     int(constantes.ALTO_VENTANA * MAPA7_SCALE_Y))
)
mapa7_w, mapa7_h = mapa7_img.get_size()

estado_juego = "menu"

# Intro
intro_textos = [
    "Saludos, veo que eres nuevo por aqui.",
    "Eso es bueno, muy bueno.",
    "Veo que te dirijes a la universidad, se te nota.",
    "pero tranquilo, no pongas esa cara.",
    "Apenas ni pusiste un pie en el lugar.",
    "No pasa nada es normal, nadie es capaz de saber",
    "su propio destino...."
]
intro_linea_actual = 0
intro_char_actual = 0
intro_texto_visible = ""
intro_timer = 0
intro_velocidad = 3
intro_espera = 0
intro_completada = False
intro_fade_alpha = 0
intro_fade_saliendo = False
intro_ultimo_texto = False
sonido_dialogo = pygame.mixer.Sound("assets/music/text sound/dialogo_sound.MP3")
sonido_dialogo.set_volume(0.15)
sonido_boton = pygame.mixer.Sound("assets/music/Effect sound/sound_boton.mp3")
sonido_boton.set_volume(0.5)
MUSICA_INTRO = "assets/music/musica/Begind_Ambient.mp3"

# varibles movimiento
mover_arriba = False
mover_abajo = False
mover_izquierda = False
mover_derecha = False

# controlar frame rate
reloj = pygame.time.Clock()

#fuentes para crear letras :p
fuente_titulo = pygame.font.Font("assets/fonts/PressStart2p.ttf", 120)
fuente_boton = pygame.font.Font("assets/fonts/PressStart2p.ttf", 50)

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

fuente_dialogo = pygame.font.Font("assets/fonts/PressStart2p.ttf", 18)
fuente_nombre = pygame.font.Font("assets/fonts/PressStart2p.ttf", 22)

def dibujar_dialogo_joel(ventana, texto, pagina, total):
    # fondo caja
    caja = pygame.Rect(40, constantes.ALTO_VENTANA - 280, constantes.ANCHO_VENTANA - 80, 240)
    fondo = pygame.Surface((caja.width, caja.height), pygame.SRCALPHA)
    fondo.fill((10, 10, 30, 210))
    ventana.blit(fondo, (caja.x, caja.y))
    pygame.draw.rect(ventana, (100, 140, 255), caja, 3)

    # nombre
    nombre_surf = fuente_nombre.render("Prof. Joel", True, (150, 200, 255))
    ventana.blit(nombre_surf, (caja.x + 20, caja.y - 36))

    # texto (soporta \n)
    lineas = texto.split("\n")
    for i, linea in enumerate(lineas):
        surf = fuente_dialogo.render(linea, True, (255, 255, 255))
        ventana.blit(surf, (caja.x + 20, caja.y + 20 + i * 36))

    # indicador continuar
    if pagina < total - 1:
        ind = fuente_dialogo.render("[ E ] Continuar", True, (180, 180, 255))
    else:
        ind = fuente_dialogo.render("[ E ] Cerrar", True, (180, 180, 255))
    ventana.blit(ind, (caja.right - 320, caja.bottom - 36))    

def dibujar_dialogo_segovia(ventana, texto, pagina, total):
    caja = pygame.Rect(40, constantes.ALTO_VENTANA - 280, constantes.ANCHO_VENTANA - 80, 240)
    fondo = pygame.Surface((caja.width, caja.height), pygame.SRCALPHA)
    fondo.fill((30, 10, 10, 210))
    ventana.blit(fondo, (caja.x, caja.y))
    pygame.draw.rect(ventana, (255, 60, 60), caja, 3)

    nombre_surf = fuente_nombre.render("Prof. Segovia", True, (255, 120, 120))
    ventana.blit(nombre_surf, (caja.x + 20, caja.y - 36))

    lineas = texto.split("\n")
    for i, linea in enumerate(lineas):
        surf = fuente_dialogo.render(linea, True, (255, 255, 255))
        ventana.blit(surf, (caja.x + 20, caja.y + 20 + i * 36))

    if pagina < total - 1:
        ind = fuente_dialogo.render("[ E ] Continuar", True, (255, 150, 150))
    else:
        ind = fuente_dialogo.render("[ E ] Cerrar", True, (255, 150, 150))
    ventana.blit(ind, (caja.right - 320, caja.bottom - 36))

def dibujar_menu_pausa(ventana):

    fondo = pygame.Surface((constantes.ANCHO_VENTANA,
                            constantes.ALTO_VENTANA), pygame.SRCALPHA)
    fondo.fill((0,0,0,120))
    ventana.blit(fondo,(0,0))

    caja = pygame.Rect(
        constantes.ANCHO_VENTANA//2-280,
        constantes.ALTO_VENTANA//2-220,
        560,
        440
    )

    panel = pygame.Surface((caja.width,caja.height),pygame.SRCALPHA)
    panel.fill((10,10,30,220))
    ventana.blit(panel,(caja.x,caja.y))

    pygame.draw.rect(ventana,(100,140,255),caja,4)

    titulo = fuente_nombre.render("PAUSA",True,(180,220,255))
    ventana.blit(titulo,
    (caja.centerx-titulo.get_width()//2,caja.y+20))

    global boton_reanudar
    global boton_musica
    global boton_menu
    global boton_salir_juego

    boton_reanudar = pygame.Rect(caja.x+80,caja.y+90,400,50)
    boton_musica = pygame.Rect(caja.x+80,caja.y+160,400,50)
    boton_menu = pygame.Rect(caja.x+80,caja.y+230,400,50)
    boton_salir_juego = pygame.Rect(caja.x+80,caja.y+300,400,50)

    mouse = pygame.mouse.get_pos()

    mouse = (
        mouse[0]*constantes.ANCHO_VENTANA//constantes.ANCHO_PANTALLA,
        mouse[1]*constantes.ALTO_VENTANA//constantes.ALTO_PANTALLA
    )

    botones = [
        (boton_reanudar,"REANUDAR"),
        (boton_musica,
        "ACTIVAR MUSICA" if musica_silenciada else "SILENCIAR MUSICA"),
        (boton_menu,"VOLVER AL MENU"),
        (boton_salir_juego,"CERRAR JUEGO")
    ]

    for rect,texto in botones:

        color=(50,70,130)

        if rect.collidepoint(mouse):
            color=(90,120,220)

        pygame.draw.rect(ventana,color,rect)
        pygame.draw.rect(ventana,(100,140,255),rect,3)

        txt=fuente_dialogo.render(texto,True,(255,255,255))

        ventana.blit(
            txt,
            (
                rect.centerx-txt.get_width()//2,
                rect.centery-txt.get_height()//2
            )
        )

def dibujar_instructivo_biblioteca(ventana):
    fondo = pygame.Surface((constantes.ANCHO_VENTANA, constantes.ALTO_VENTANA), pygame.SRCALPHA)
    fondo.fill((0, 0, 0, 180))
    ventana.blit(fondo, (0, 0))

    caja = pygame.Rect(400, 200, 1120, 680)
    pygame.draw.rect(ventana, (10, 10, 30), caja)
    pygame.draw.rect(ventana, (100, 140, 255), caja, 3)

    titulo = fuente_nombre.render("MISION: BIBLIOTECA", True, (150, 200, 255))
    ventana.blit(titulo, (caja.centerx - titulo.get_width()//2, caja.y + 30))

    instrucciones = [
        "El Profesor Segovia te encargo buscar un libro.",
        "",
        "- Un libro se iluminara en la estanteria.",
        "- Clickealo antes de que se apague.",
        "- Acertar suma 2 segundos.",
        "- Fallar resta 3 segundos.",
        "- Si el libro se apaga solo resta 3 segundos.",
        "",
        f"Libros a encontrar: 15",
        f"Tiempo inicial: 17 segundos",
        f"Tiempo de reaccion: 3.5 segundos",
    ]
    for i, linea in enumerate(instrucciones):
        color = (255, 255, 255) if linea != "" else (255, 255, 255)
        surf = fuente_dialogo.render(linea, True, color)
        ventana.blit(surf, (caja.x + 40, caja.y + 90 + i * 42))

    boton = pygame.Rect(caja.centerx - 120, caja.bottom - 80, 240, 50)
    mouse_real = pygame.mouse.get_pos()
    mouse_pos = (
        mouse_real[0] * constantes.ANCHO_VENTANA // constantes.ANCHO_PANTALLA,
        mouse_real[1] * constantes.ALTO_VENTANA // constantes.ALTO_PANTALLA
    )
    color_boton = (100, 180, 255) if boton.collidepoint(mouse_pos) else (50, 120, 200)
    pygame.draw.rect(ventana, color_boton, boton)
    pygame.draw.rect(ventana, (150, 200, 255), boton, 2)
    txt = fuente_dialogo.render("INICIAR", True, (255, 255, 255))
    ventana.blit(txt, (boton.centerx - txt.get_width()//2, boton.centery - txt.get_height()//2))

    return boton


def dibujar_teclas_tutorial(ventana, alpha):
    TAM = 60       # tamaño del icono de tecla
    GAP = 12       # separación entre teclas
    RADIO = 8      # radio bordes redondeados
    surf_w = TAM * 3 + GAP * 2
    surf_h = TAM * 2 + GAP
    surf = pygame.Surface((surf_w, surf_h), pygame.SRCALPHA)

    fuente_tecla = pygame.font.Font("assets/fonts/PressStart2p.ttf", 14)

    def key(letra, cx, cy):
        # fondo tecla
        pygame.draw.rect(surf, (30, 30, 40, alpha), (cx, cy, TAM, TAM), border_radius=RADIO)
        # borde exterior luminoso
        pygame.draw.rect(surf, (120, 170, 255, alpha), (cx, cy, TAM, TAM), 3, border_radius=RADIO)
        # borde inferior mas oscuro (efecto 3D)
        pygame.draw.rect(surf, (60, 100, 180, alpha), (cx + 3, cy + TAM - 6, TAM - 6, 6), border_radius=3)
        # letra
        txt = fuente_tecla.render(letra, True, (220, 230, 255))
        txt.set_alpha(alpha)
        surf.blit(txt, (cx + TAM // 2 - txt.get_width() // 2,
                        cy + TAM // 2 - txt.get_height() // 2 - 2))

    # W arriba centrado
    key("W", surf_w // 2 - TAM // 2, 0)
    # A S D abajo
    key("A", 0,               TAM + GAP)
    key("S", TAM + GAP,       TAM + GAP)
    key("D", TAM * 2 + GAP * 2, TAM + GAP)

    # Posición: parte baja de la pantalla, centrado
    pos_x = constantes.ANCHO_VENTANA // 2 - surf_w // 2
    pos_y = constantes.ALTO_VENTANA - surf_h - 80
    ventana.blit(surf, (pos_x, pos_y))


def dibujar_minijuego_biblioteca(ventana, tiempo, libros_correctos, libro_iluminado, libro_timer):
    ventana.blit(biblioteca_img, (0, 0))

    # iluminar libro activo
    if libro_iluminado >= 0 and libro_iluminado < len(libros_hitboxes):
        # Neon orange outer glow
        pygame.draw.rect(ventana, (255, 100, 0), libros_hitboxes[libro_iluminado].inflate(8, 8), 2)
        # Neon yellow inner thick border
        pygame.draw.rect(ventana, (255, 255, 0), libros_hitboxes[libro_iluminado], 6)
        # Translucent bright yellow fill
        s = pygame.Surface((libros_hitboxes[libro_iluminado].width, libros_hitboxes[libro_iluminado].height), pygame.SRCALPHA)
        s.fill((255, 255, 0, 130))
        ventana.blit(s, libros_hitboxes[libro_iluminado].topleft)

    # HUD
    pygame.draw.rect(ventana, (10, 10, 30, 180), pygame.Rect(0, 0, constantes.ANCHO_VENTANA, 60))
    t_surf = fuente_dialogo.render(f"Tiempo: {tiempo:.1f}s", True, (255, 255, 100) if tiempo > 8 else (255, 80, 80))
    ventana.blit(t_surf, (30, 18))
    l_surf = fuente_dialogo.render(f"Libros: {libros_correctos}/15", True, (150, 200, 255))
    ventana.blit(l_surf, (400, 18))

    # barra timer libro
    if libro_iluminado >= 0:
        barra_ancho = int((libro_timer / libro_tiempo_reaccion) * 400)
        pygame.draw.rect(ventana, (60, 60, 60), pygame.Rect(constantes.ANCHO_VENTANA - 430, 18, 400, 24))
        pygame.draw.rect(ventana, (100, 220, 100), pygame.Rect(constantes.ANCHO_VENTANA - 430, 18, barra_ancho, 24))


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
        jugador.forma.centery = salida_rect.bottom + jugador.forma.height // 2 + 120
    elif lado == "abajo":
        jugador.forma.centerx = salida_rect.centerx
        jugador.forma.centery = salida_rect.top - jugador.forma.height // 2 - 120
    elif lado == "izquierda":
        jugador.forma.centerx = salida_rect.right + jugador.forma.width // 2 + 30
        jugador.forma.centery = salida_rect.centery
    elif lado == "derecha":
        jugador.forma.centerx = salida_rect.left - jugador.forma.width // 2 - 30
        jugador.forma.centery = salida_rect.centery
    

run = True
mostrar_hitbox = False
cooldown_mapa = 0
joel_hablado = False
cerca_segovia = False

dialogo_joel_activo = False
dialogo_joel_pagina = 0
dialogo_joel_textos = []
joel_hablado = False

dialogo_segovia_activo = False
dialogo_segovia_pagina = 0
dialogo_segovia_textos = []
segovia_hablado = False

# Minijuego biblioteca
minijuego_activo = False
minijuego_instructivo = False
minijuego_completado = False
mision_biblioteca_activa = False  # Locked until Segovia talks to the player

libro_iluminado = -1
libro_timer = 0
libro_tiempo_reaccion = 3.5
libros_correctos = 0
libros_objetivo = 15
tiempo_minijuego = 17.0
cerca_libreria = False
minijuego_click_procesado = False
boton_iniciar = pygame.Rect(0, 0, 0, 0)

# Tutorial mapa 1
tutorial_timer = 5.0
tutorial_alpha = 255


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
     x_inicial = constantes.ANCHO_VENTANA // 2 - 495
     tiempo = pygame.time.get_ticks()
     pulso = int(30 + ((math.sin(tiempo / 300) + 1) / 2) * 100)
     for i, letra in enumerate(texto):
         dibujar_texto_glow(ventana, letra, fuente_titulo, colores_titulo[i], (x_inicial + i * 120, 180), alpha_glow=pulso)

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

    elif estado_juego == "intro":
        ventana.fill((0, 0, 0))

        if not intro_fade_saliendo:
            if intro_linea_actual < len(intro_textos):
                intro_timer += 1
                if intro_timer >= intro_velocidad:
                    intro_timer = 0
                    if intro_char_actual < len(intro_textos[intro_linea_actual]):
                        intro_texto_visible += intro_textos[intro_linea_actual][intro_char_actual]
                        intro_char_actual += 1
                        sonido_dialogo.play()
                    else:
                        intro_espera += 1
                        if intro_espera >= 40:
                            intro_espera = 0
                            intro_linea_actual += 1
                            intro_char_actual = 0
                            intro_texto_visible = ""
            else:
                intro_fade_saliendo = True
                intro_fade_alpha = 0

            palabras = intro_texto_visible.split(" ")
            lineas_render = []
            linea_temp = ""
            for palabra in palabras:
                test = linea_temp + palabra + " "
                if fuente_boton.size(test)[0] > constantes.ANCHO_VENTANA - 200:
                    lineas_render.append(linea_temp)
                    linea_temp = palabra + " "
                else:
                    linea_temp = test
            lineas_render.append(linea_temp)
            total_h = len(lineas_render) * (fuente_boton.get_height() + 10)
            y_inicio = constantes.ALTO_VENTANA // 2 - total_h // 2
            for i, lr in enumerate(lineas_render):
                s = fuente_boton.render(lr, True, (255, 255, 255))
                ventana.blit(s, (constantes.ANCHO_VENTANA // 2 - s.get_width() // 2,
                                 y_inicio + i * (fuente_boton.get_height() + 10)))

        if intro_fade_saliendo:
            ultimo = fuente_boton.render(intro_textos[-1], True, (255, 255, 255))
            alpha_texto = max(0, 255 - intro_fade_alpha)
            ultimo.set_alpha(alpha_texto)
            ventana.blit(ultimo, (
                constantes.ANCHO_VENTANA // 2 - ultimo.get_width() // 2,
                constantes.ALTO_VENTANA // 2 - ultimo.get_height() // 2
            ))
            intro_fade_alpha += 3
            fade_surf = pygame.Surface((constantes.ANCHO_VENTANA, constantes.ALTO_VENTANA))
            fade_surf.fill((0, 0, 0))
            fade_surf.set_alpha(min(intro_fade_alpha, 255))
            ventana.blit(fade_surf, (0, 0))
            if intro_fade_alpha >= 255:
                estado_juego = "jugando"

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_RETURN, pygame.K_SPACE):
                    intro_fade_saliendo = True

        # dibujar texto actual (siempre visible mientras no fade completo)
        if not intro_fade_saliendo:
            # texto con wrap manual por si es largo
            palabras = intro_texto_visible.split(" ")
            lineas_render = []
            linea_temp = ""
            for palabra in palabras:
                test = linea_temp + palabra + " "
                if fuente_boton.size(test)[0] > constantes.ANCHO_VENTANA - 200:
                    lineas_render.append(linea_temp)
                    linea_temp = palabra + " "
                else:
                    linea_temp = test
            lineas_render.append(linea_temp)

            total_h = len(lineas_render) * (fuente_boton.get_height() + 10)
            y_inicio = constantes.ALTO_VENTANA // 2 - total_h // 2
            for i, lr in enumerate(lineas_render):
                s = fuente_boton.render(lr, True, (255, 255, 255))
                ventana.blit(s, (constantes.ANCHO_VENTANA // 2 - s.get_width() // 2, y_inicio + i * (fuente_boton.get_height() + 10)))

        if intro_fade_saliendo:
            # mostrar ultimo texto desvaneciéndose
            ultimo = fuente_boton.render(intro_textos[-1], True, (255, 255, 255))
            alpha_texto = max(0, 255 - intro_fade_alpha)
            ultimo.set_alpha(alpha_texto)
            ventana.blit(ultimo, (
                constantes.ANCHO_VENTANA // 2 - ultimo.get_width() // 2,
                constantes.ALTO_VENTANA // 2 - ultimo.get_height() // 2
            ))

            intro_fade_alpha += 3
            fade_surf = pygame.Surface((constantes.ANCHO_VENTANA, constantes.ALTO_VENTANA))
            fade_surf.fill((0, 0, 0))
            fade_surf.set_alpha(min(intro_fade_alpha, 255))
            ventana.blit(fade_surf, (0, 0))

            if intro_fade_alpha >= 255:
                estado_juego = "jugando"

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_RETURN, pygame.K_SPACE):
                    intro_fade_saliendo = True
    
    elif estado_juego == "jugando":

        ventana.fill((10, 10, 70))

        velocidad_actual = constantes.VELOCIDAD

        teclas = pygame.key.get_pressed()
        delta_x = 0
        delta_y = 0

        if not pausa and not dialogo_joel_activo and not dialogo_segovia_activo and not minijuego_activo and not minijuego_instructivo:
            if teclas[pygame.K_w] or teclas[pygame.K_UP]:
                delta_y = -velocidad_actual

            if teclas[pygame.K_s] or teclas[pygame.K_DOWN]:
                delta_y = velocidad_actual

            if teclas[pygame.K_a] or teclas[pygame.K_LEFT]:
                delta_x = -velocidad_actual

            if teclas[pygame.K_d] or teclas[pygame.K_RIGHT]:
                delta_x = velocidad_actual

        salida_abajo = None
        salida_izquierda = None

        paredes, salida, salida_izquierda, salida_abajo = obtener_variables_mapa(mapas.mapa_actual)

        if mapas.mapa_actual == 1:
            bus.mover()
            bus.animar()
            bus.dibujar(ventana)
            if jugador.forma.colliderect(bus.rect):
                velocidad_actual = 2

        paredes_con_npcs = paredes.copy()
        if mapas.mapa_actual == 6:
           paredes_con_npcs.append(joel.hitbox)
        if mapas.mapa_actual == 5:
            paredes_con_npcs.append(segovia.hitbox)

        jugador.movimiento(delta_x, delta_y, paredes_con_npcs)

        # cambiar mapa
        cambio_mapa = False
        if cooldown_mapa == 0:

            if mapas.mapa_actual == 1:

                if jugador.forma.colliderect(salida):

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
                    # Entrar a biblioteca - activar musica biblioteca
                    if musica_actual != MUSICA_MAPA7:
                        musica_anterior = musica_actual
                        reproducir_musica(MUSICA_MAPA7)
                        musica_actual = MUSICA_MAPA7
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
                elif jugador.forma.colliderect(mapas.salida_mapa4_arriba):
                    mapas.mapa_actual = 6
                    posicionar_jugador_entrada(
                        mapas.salida_oficina_profesores,
                        "abajo",
                        jugador
                    )
                    if musica_actual != MUSICA_MAPA6:
                        musica_anterior = musica_actual
                        reproducir_musica(MUSICA_MAPA6)
                        musica_actual = MUSICA_MAPA6
                    cooldown_mapa = 30
                    cambio_mapa = True
                
            elif mapas.mapa_actual == 5 and jugador.forma.colliderect(salida):
                mapas.mapa_actual = 4
                posicionar_jugador_entrada(mapas.salida_mapa4_izquierda, "izquierda", jugador)
                cooldown_mapa = 30
                cambio_mapa = True
            elif mapas.mapa_actual == 6 and jugador.forma.colliderect(salida):
                mapas.mapa_actual = 4
                posicionar_jugador_entrada(mapas.salida_mapa4_arriba, "arriba", jugador)
                if musica_actual == MUSICA_MAPA6:
                    reproducir_musica(musica_anterior or MUSICA_JUEGO)
                    musica_actual = musica_anterior or MUSICA_JUEGO
                    musica_anterior = None
                cooldown_mapa = 30
                cambio_mapa = True
            elif mapas.mapa_actual == 7 and jugador.forma.colliderect(salida):
                mapas.mapa_actual = 3
                posicionar_jugador_entrada(mapas.salida_mapa3_derecha, "derecha", jugador)
                # Salir de biblioteca - restaurar musica anterior
                if musica_actual == MUSICA_MAPA7:
                    reproducir_musica(musica_anterior or MUSICA_JUEGO)
                    musica_actual = musica_anterior or MUSICA_JUEGO
                    musica_anterior = None
                cooldown_mapa = 30
                cambio_mapa = True
            elif mapas.mapa_actual == 7 and jugador.forma.colliderect(salida_abajo):
                mapas.mapa_actual = 9
                posicionar_jugador_entrada(mapas.salida_mapa9, "arriba", jugador)
                # Salir de biblioteca - restaurar musica anterior
                if musica_actual == MUSICA_MAPA7:
                    reproducir_musica(musica_anterior or MUSICA_JUEGO)
                    musica_actual = musica_anterior or MUSICA_JUEGO
                    musica_anterior = None
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
            # FADE OUT (oscurecer suave) 
            for alpha in range(0, 256, 12):
                ventana.fill((0, 0, 0))
                overlay = pygame.Surface((constantes.ANCHO_VENTANA, constantes.ALTO_VENTANA))
                overlay.set_alpha(alpha)
                ventana.blit(overlay, (0, 0))
                
                escalado = pygame.transform.scale(ventana, (constantes.ANCHO_PANTALLA, constantes.ALTO_PANTALLA))
                pantalla.blit(escalado, (0, 0))
                pygame.display.update()
                pygame.time.wait(30)
            
            # === CAMBIO DE MAPA ===
            mover_arriba = mover_abajo = mover_izquierda = mover_derecha = False
            paredes, salida, salida_izquierda, salida_abajo = obtener_variables_mapa(mapas.mapa_actual)
            pygame.time.wait(30)

            
            
            # === FADE IN (desvanecimiento inverso suave) ===
            for alpha in range(255, -1, -12):
                # Dibujar nuevo mapa
                if mapas.mapa_actual == 1:
                    camera_x = max(MAPA1_OFFSET_X, min(jugador.forma.centerx - constantes.ANCHO_VENTANA // 2, MAPA1_OFFSET_X + mapa1_w - constantes.ANCHO_VENTANA))
                    camera_y = max(MAPA1_OFFSET_Y, min(jugador.forma.centery - constantes.ALTO_VENTANA // 2, MAPA1_OFFSET_Y + mapa1_h - constantes.ALTO_VENTANA))
                    ventana.blit(mapa1_img, (MAPA1_OFFSET_X - camera_x, MAPA1_OFFSET_Y - camera_y))
                elif mapas.mapa_actual == 2:

                    ventana.fill((0,0,0))
                    ventana.blit(mapas.mapa2_img,(0,0))

                elif mapas.mapa_actual == 3:

                    ventana.fill((0,0,0))
                    ventana.blit(mapas.mapa3_img,(0,0))
                    
                elif mapas.mapa_actual == 4:
                    camera_x = max(MAPA4_OFFSET_X, min(jugador.forma.centerx - constantes.ANCHO_VENTANA // 2, MAPA4_OFFSET_X + mapa4_w - constantes.ANCHO_VENTANA))
                    camera_y = max(MAPA4_OFFSET_Y, min(jugador.forma.centery - constantes.ALTO_VENTANA // 2, MAPA4_OFFSET_Y + mapa4_h - constantes.ALTO_VENTANA))
                    ventana.blit(mapa4_img, (MAPA4_OFFSET_X - camera_x, MAPA4_OFFSET_Y - camera_y))
                elif mapas.mapa_actual == 5:
                    ventana.blit(mapa5_img, (0, 0))
                elif mapas.mapa_actual == 6:
                    camera_x = max(MAPA6_OFFSET_X, min(jugador.forma.centerx - constantes.ANCHO_VENTANA // 2, MAPA6_OFFSET_X + mapa6_w - constantes.ANCHO_VENTANA))
                    camera_y = max(MAPA6_OFFSET_Y, min(jugador.forma.centery - constantes.ALTO_VENTANA // 2, MAPA6_OFFSET_Y + mapa6_h - constantes.ALTO_VENTANA))
                    ventana.blit(mapa6_img, (MAPA6_OFFSET_X - camera_x, MAPA6_OFFSET_Y - camera_y))
                elif mapas.mapa_actual == 7:
                    camera_x = max(MAPA7_OFFSET_X, min(jugador.forma.centerx - constantes.ANCHO_VENTANA // 2, MAPA7_OFFSET_X + mapa7_w - constantes.ANCHO_VENTANA))
                    camera_y = max(MAPA7_OFFSET_Y, min(jugador.forma.centery - constantes.ALTO_VENTANA // 2, MAPA7_OFFSET_Y + mapa7_h - constantes.ALTO_VENTANA))
                    ventana.blit(mapa7_img, (MAPA7_OFFSET_X - camera_x, MAPA7_OFFSET_Y - camera_y))
                else:
                    ventana.fill((10, 10, 70))
                
                # Overlay fade in
                overlay = pygame.Surface((constantes.ANCHO_VENTANA, constantes.ALTO_VENTANA))
                overlay.fill((0, 0, 0))
                overlay.set_alpha(alpha)
                ventana.blit(overlay, (0, 0))
                
                escalado = pygame.transform.scale(ventana, (constantes.ANCHO_PANTALLA, constantes.ALTO_PANTALLA))
                pantalla.blit(escalado, (0, 0))
                pygame.display.update()
                pygame.time.wait(30)
        cambio_mapa = False
       
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

            # === TUTORIAL MAPA 1 - iconos de teclas WASD con fade ===
            if tutorial_timer > 0:
                dt_tut = reloj.get_time() / 1000.0
                tutorial_timer = max(0.0, tutorial_timer - dt_tut)
                if tutorial_timer < 1.5:
                    tutorial_alpha = max(0, int((tutorial_timer / 1.5) * 255))
                else:
                    tutorial_alpha = 255
                dibujar_teclas_tutorial(ventana, tutorial_alpha)


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

        elif mapas.mapa_actual == 5:

            #Camara mapa 5
            camera_x = jugador.forma.centerx - constantes.ANCHO_VENTANA // 2
            camera_y = jugador.forma.centery - constantes.ALTO_VENTANA // 2

            camera_x = max(
                MAPA5_OFFSET_X,
                min(camera_x, MAPA5_OFFSET_X + mapa5_w - constantes.ANCHO_VENTANA)
            )
            camera_y = max(
                MAPA5_OFFSET_Y,
                min(camera_y, MAPA5_OFFSET_Y + mapa5_h - constantes.ALTO_VENTANA)
            )

            ventana.fill((0, 0, 0))
            ventana.blit(
                mapa5_img,
                (MAPA5_OFFSET_X - camera_x, MAPA5_OFFSET_Y - camera_y)
            )
            segovia.animar()
            segovia.dibujar(ventana, camera_x, camera_y)
            segovia.hitbox.x = segovia.rect.x
            segovia.hitbox.y = segovia.rect.y

            cerca_segovia = jugador.forma.colliderect(
                pygame.Rect(segovia.rect.x - 150, segovia.rect.y - 100, 400, 350)
            )
            if cerca_segovia and not dialogo_segovia_activo:
                if joel_hablado:
                    prompt = fuente_dialogo.render("[ E ] Hablar", True, (100, 200, 255))
                else:
                    prompt = fuente_dialogo.render("Habla con Joel primero", True, (255, 120, 60))
                ventana.blit(prompt, (
                    segovia.rect.x - camera_x - 20,
                    segovia.rect.y - camera_y - 50
                ))
            if dialogo_segovia_activo:
                dibujar_dialogo_segovia(
                    ventana,
                    dialogo_segovia_textos[dialogo_segovia_pagina],
                    dialogo_segovia_pagina,
                    len(dialogo_segovia_textos)
                )
            



        elif mapas.mapa_actual == 6:
            camera_x = jugador.forma.centerx - constantes.ANCHO_VENTANA // 2
            camera_y = jugador.forma.centery - constantes.ALTO_VENTANA // 2

            camera_x = max(
                MAPA6_OFFSET_X,
                min(camera_x, MAPA6_OFFSET_X + mapa6_w - constantes.ANCHO_VENTANA)
            )
            camera_y = max(
                MAPA6_OFFSET_Y,
                min(camera_y, MAPA6_OFFSET_Y + mapa6_h - constantes.ALTO_VENTANA)
            )

            ventana.fill((0, 0, 0))
            ventana.blit(
                mapa6_img,
                (MAPA6_OFFSET_X - camera_x, MAPA6_OFFSET_Y - camera_y)
            )
            joel.animar()
            joel.dibujar(ventana, camera_x, camera_y)

            # prompt acercarse a joel
            zona_joel = pygame.Rect(joel.rect.x - 150, joel.rect.y - 100, 400, 350)
            jugador_en_pantalla = pygame.Rect(
                jugador.forma.x - camera_x,
                jugador.forma.y - camera_y,
                jugador.forma.width,
                jugador.forma.height
            )
            joel_en_pantalla = pygame.Rect(
                joel.rect.x - camera_x,
                joel.rect.y - camera_y,
                zona_joel.width,
                zona_joel.height
            )
            cerca_joel = jugador.forma.colliderect(
                pygame.Rect(joel.rect.x - 150, joel.rect.y - 100, 400, 350)
            )
            if cerca_joel and not dialogo_joel_activo:
                prompt = fuente_dialogo.render("[ E ] Hablar", True, (255, 255, 255))
                ventana.blit(prompt, (
                    joel.rect.x - camera_x - 20,
                    joel.rect.y - camera_y - 50
                ))

            if dialogo_joel_activo:
                dibujar_dialogo_joel(
                    ventana,
                    dialogo_joel_textos[dialogo_joel_pagina],
                    dialogo_joel_pagina,
                    len(dialogo_joel_textos)
                )
            

        elif mapas.mapa_actual == 7:
            if minijuego_instructivo:
                # Pausar musica biblioteca durante instructivo
                if musica_actual == MUSICA_MAPA7:
                    pygame.mixer.music.pause()
                paredes = []
                boton_iniciar = dibujar_instructivo_biblioteca(ventana)
            elif minijuego_activo:
                # Reproducir musica minijuego si no esta sonando
                if musica_actual != MUSICA_MINIJUEGO:
                    reproducir_musica(MUSICA_MINIJUEGO)
                    musica_actual = MUSICA_MINIJUEGO
                paredes = []
                dt = reloj.get_time() / 1000.0
                tiempo_minijuego -= dt
                libro_timer -= dt

                if libro_iluminado == -1:
                    libro_iluminado = random.randint(0, len(libros_hitboxes) - 1)
                    libro_timer = libro_tiempo_reaccion

                if libro_timer <= 0 and libro_iluminado >= 0:
                    tiempo_minijuego -= 3
                    libro_iluminado = random.randint(0, len(libros_hitboxes) - 1)
                    libro_timer = libro_tiempo_reaccion

                if tiempo_minijuego <= 0:
                    tiempo_minijuego = 0
                    minijuego_activo = False
                    # Restaurar musica biblioteca al terminar (tiempo agotado)
                    reproducir_musica(MUSICA_MAPA7)
                    musica_actual = MUSICA_MAPA7

                dibujar_minijuego_biblioteca(ventana, tiempo_minijuego, libros_correctos, libro_iluminado, libro_timer)
            else:
                # Cámara mapa 7
                camera_x = jugador.forma.centerx - constantes.ANCHO_VENTANA // 2
                camera_y = jugador.forma.centery - constantes.ALTO_VENTANA // 2

                camera_x = max(
                    MAPA7_OFFSET_X,
                    min(camera_x, MAPA7_OFFSET_X + mapa7_w - constantes.ANCHO_VENTANA)
                )
                camera_y = max(
                    MAPA7_OFFSET_Y,
                    min(camera_y, MAPA7_OFFSET_Y + mapa7_h - constantes.ALTO_VENTANA)
                )

                ventana.fill((0, 0, 0))
                ventana.blit(
                    mapa7_img,
                    (MAPA7_OFFSET_X - camera_x, MAPA7_OFFSET_Y - camera_y)
                )

                cerca_libreria = jugador.forma.colliderect(
                    pygame.Rect(2300, 400, 500, 800)
                )
                if cerca_libreria and mision_biblioteca_activa and not minijuego_completado:
                    prompt = fuente_dialogo.render("[ E ] Buscar libro", True, (80, 180, 255))
                    ventana.blit(prompt, (
                        jugador.forma.centerx - camera_x - prompt.get_width() // 2,
                        jugador.forma.top - camera_y - 60
                    ))

        else:
            camera_x = 0
            camera_y = 0

        # Dibujar logo ULagos en el mapa 2

        if mapas.mapa_actual == 2:

            ventana.blit(logo_ulagos, (800, 600))    

                # dibujar paredes mas colisiones
        for pared in paredes:
            # No dibujar paredes grises en mapas con imagen grande
            if mapas.mapa_actual not in (1, 4, 5, 6, 7, 10):
                pygame.draw.rect(ventana, (150, 150, 150), pared)

            # Mostrar hitbox ROJA siempre con offset de cámara en mapas grandes
            if mostrar_hitbox:
                if mapas.mapa_actual in (1, 4, 5, 6, 7):
                    draw_rect = pygame.Rect(
                        pared.x - camera_x,
                        pared.y - camera_y,
                        pared.width,
                        pared.height
                    )
                    pygame.draw.rect(ventana, (255, 0, 0), draw_rect, 3)
       
        # dibujar jugador
        if mapas.mapa_actual in (1, 4, 5, 6, 7):
            if not minijuego_activo and not minijuego_instructivo:
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
        if mostrar_hitbox and not minijuego_activo and not minijuego_instructivo:
            if mapas.mapa_actual in (1, 4, 5, 6, 7):
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

            elif mapas.mapa_actual == 7:

                if salida:
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

                if salida_abajo:
                    pygame.draw.rect(
                        ventana,
                        (0, 0, 255),
                        pygame.Rect(
                            salida_abajo.x - camera_x,
                            salida_abajo.y - camera_y,
                            salida_abajo.width,
                            salida_abajo.height
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
                    sonido_boton.play()
                    # fade negro antes de la intro
                    for alpha in range(0, 256, 8):
                        ventana.fill((0, 0, 0))
                        fade = pygame.Surface((constantes.ANCHO_VENTANA, constantes.ALTO_VENTANA))
                        fade.fill((0, 0, 0))
                        fade.set_alpha(alpha)
                        ventana.blit(fade, (0, 0))
                        escalado = pygame.transform.scale(ventana, (constantes.ANCHO_PANTALLA, constantes.ALTO_PANTALLA))
                        pantalla.blit(escalado, (0, 0))
                        pygame.display.update()
                        pygame.time.wait(15)
                    reproducir_musica(MUSICA_INTRO)
                    musica_actual = MUSICA_INTRO
                    estado_juego = "intro"
                    cambio_mapa = False
                    cooldown_mapa = 30
                    intro_linea_actual = 0
                    intro_char_actual = 0
                    intro_texto_visible = ""
                    intro_timer = 0
                    intro_espera = 0
                    intro_fade_alpha = 0
                    intro_fade_saliendo = False

                elif boton_salir.collidepoint(mouse_pos):
                    sonido_boton.play()
                    run = False

        if estado_juego == "jugando":
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_real = event.pos
                mouse_pos = (
                    mouse_real[0] * constantes.ANCHO_VENTANA // constantes.ANCHO_PANTALLA,
                    mouse_real[1] * constantes.ALTO_VENTANA // constantes.ALTO_PANTALLA
                )
                if minijuego_instructivo:
                    if boton_iniciar.collidepoint(mouse_pos):
                        minijuego_instructivo = False
                        minijuego_activo = True
                        libro_iluminado = random.randint(0, len(libros_hitboxes) - 1)
                        libro_timer = libro_tiempo_reaccion
                        # Arrancar musica del minijuego
                        reproducir_musica(MUSICA_MINIJUEGO)
                        musica_actual = MUSICA_MINIJUEGO
                elif minijuego_activo:
                    if libro_iluminado >= 0 and libro_iluminado < len(libros_hitboxes):
                        libro_correcto = libros_hitboxes[libro_iluminado]
                        if libro_correcto.collidepoint(mouse_pos):
                            tiempo_minijuego += 2
                            libros_correctos += 1
                            if libros_correctos >= libros_objetivo:
                                minijuego_activo = False
                                minijuego_completado = True
                                mision_biblioteca_activa = False
                                # Minijuego completado - restaurar musica biblioteca
                                reproducir_musica(MUSICA_MAPA7)
                                musica_actual = MUSICA_MAPA7
                            else:
                                libro_iluminado = random.randint(0, len(libros_hitboxes) - 1)
                                libro_timer = libro_tiempo_reaccion
                        else:
                            tiempo_minijuego -= 3

            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                   pausa = not pausa
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
                if event.key == pygame.K_e:
                    if mapas.mapa_actual == 6:
                        if dialogo_joel_activo:
                            dialogo_joel_pagina += 1
                            if dialogo_joel_pagina >= len(dialogo_joel_textos):
                                dialogo_joel_activo = False
                                dialogo_joel_pagina = 0
                                joel_hablado = True
                        elif cerca_joel:
                            dialogo_joel_activo = True
                            if joel_hablado:
                                dialogo_joel_textos = [
                                    "Estas esperando algo...?"
                                ]
                            else:
                                dialogo_joel_textos = [
                                    "Buena chiquillo, bienvenido a la Universidad de Los Lagos.\nMe llamo Joel, sere tu profesor de la facultad de ingenieria.",
                                    "En este momento no dare clases, estoy en mi descanso.\nPero revisando tu horario, Tienes Matematicas con el Profesor Segovia.",
                                    "Deberias ir a buscarlo, creo haberlo visto por el pasillo a la izquierda.\n Lo mas seguro es que fue a pedir un cafe.",
                                    "Pero bueno chico no te entretengo mas, suerte en tu primer dia de clases y cuidate."
                                ]
                    if mapas.mapa_actual == 5:
                        if dialogo_segovia_activo:
                            dialogo_segovia_pagina += 1
                            if dialogo_segovia_pagina >= len(dialogo_segovia_textos):
                                dialogo_segovia_activo = False
                                dialogo_segovia_pagina = 0
                                if not segovia_hablado:
                                    mision_biblioteca_activa = True
                                segovia_hablado = True
                        elif cerca_segovia and joel_hablado:
                            dialogo_segovia_activo = True
                            if minijuego_completado:
                                dialogo_segovia_textos = [
                                    "¡Excelente trabajo! Veo que conseguiste el libro, perfecto chico ya estas listo para la clase."
                                ]
                            elif segovia_hablado:
                                dialogo_segovia_textos = [
                                    "Ya te dije todo lo que necesitas saber. Ve a la biblioteca por el libro."
                                ]
                            else:
                                dialogo_segovia_textos = [
                                    "Ah, hola joven, asique eres el nuevo estudiante, bienvenido.\nSoy el profesor Segovia.",
                                    "Y la clases de primer año sera de introduccion a la Matematica.\nPero antes de nada, te recomiendo tener el libro intro a la matematica.",
                                    "tienes que ir a la biblioteca, se encuentra a la derecha saliendo de este edificio.\ny sera mejor que te des prisa.",
                                    "Porque nada mas me termine este cafe empezare la clase.",
                                    "Asique no tienes mucho tiempo que digamos.\nvuelve conmigo cuando ya lo tengas, suerte."
                                ]
                    if mapas.mapa_actual == 7:
                        if cerca_libreria and mision_biblioteca_activa and not minijuego_completado:
                            minijuego_instructivo = True
                            tiempo_minijuego = 17.0
                            libros_correctos = 0
                            libro_iluminado = -1
                    


                            

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