import pygame
import constantes
from personaje import Personaje
import mapas

jugador = Personaje(200, 200,)

pygame.init()
pygame.mixer.init()

fondo_menu = pygame.image.load("assets//images/Menu//Menu.png")
pygame.mixer.music.load("assets//music//musica//EmptyTown_DELTARUNE.mp3")
pygame.mixer.music.play(-1) 


fondo_menu = pygame.transform.scale(fondo_menu,( constantes.ANCHO_VENTANA,constantes.ALTO_VENTANA))

ventana = pygame.display.set_mode((constantes.ANCHO_VENTANA,
                                   constantes.ALTO_VENTANA))

pygame.display.set_caption("A WAY OUT (nombre en desarrollo)")

estado_juego = "menu"

# variables movimiento
mover_arriba = False
mover_abajo = False
mover_izquierda = False
mover_derecha = False

# controlar frame rate
reloj = pygame.time.Clock()

#fuentes para crear letras :p
fuente_titulo = pygame.font.SysFont("Arial", 120)
fuente_boton = pygame.font.SysFont("Arial", 50)

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

     texto_titulo = fuente_titulo.render ("A WAY OUT", True,(255, 255, 255))

     ventana.blit(texto_titulo, (600, 180))
     boton_jugar = pygame.Rect(760, 420, 400, 100)

     pygame.draw.rect(ventana,(50, 120, 255), boton_jugar)

     texto_jugar = fuente_boton.render("JUGAR", True, (255, 255, 255))

     ventana.blit(texto_jugar, (885, 445))
     boton_salir = pygame.Rect(760, 570, 400, 100)

     pygame.draw.rect(ventana, (150, 50, 50), boton_salir)

     texto_salir = fuente_boton.render( "SALIR", True, (255, 255, 255))

     ventana.blit(texto_salir, (900, 595))
    
    elif estado_juego == "jugando":

        ventana.fill((10, 10, 70))

        delta_x = 0
        delta_y = 0

        if mover_arriba:
            delta_y = -constantes.VELOCIDAD

        if mover_abajo:
            delta_y = constantes.VELOCIDAD

        if mover_izquierda:
            delta_x = -constantes.VELOCIDAD

        if mover_derecha:
            delta_x = constantes.VELOCIDAD

        # elegir mapa
        if mapas.mapa_actual == 1:

            paredes = mapas.paredes_mapa1
            salida = mapas.salida_mapa1

        else:

            paredes = mapas.paredes_mapa2
            salida = mapas.salida_mapa2

        # mover jugador
        jugador.movimiento(delta_x, delta_y, paredes)

        # cambiar mapa
        if jugador.forma.colliderect(salida) and cooldown_mapa == 0:

            if mapas.mapa_actual == 1:

                mapas.mapa_actual = 2

                jugador.forma.x = constantes.ANCHO_VENTANA // 2
                jugador.forma.y = 100
                cooldown_mapa = 30

            else:

                mapas.mapa_actual = 1

                jugador.forma.x = constantes.ANCHO_VENTANA // 2
                jugador.forma.y = constantes.ALTO_VENTANA - 200
                cooldown_mapa = 30

        
        # dibujar paredes + colisiones
        for pared in paredes:

            # pared visible
            pygame.draw.rect(
                ventana,
                (150, 150, 150),
                pared
            )

               # mostrar hitbox paredes
            if mostrar_hitbox:
                   pygame.draw.rect(
                    ventana,
                    (255, 0, 0),
                    pared,
                    3
                )
            
             
        # dibujar salida
        pygame.draw.rect(
            ventana,
            (0, 0, 120),
            salida
        )

        # dibujar jugador
        ventana.blit(
            jugador.image,
            jugador.forma
        )

        # hitbox jugador
        if mostrar_hitbox:
              pygame.draw.rect(
                ventana,
                (0, 255, 0),
                jugador.forma,
                3
            )

        # eventos
    for event in pygame.event.get():

        # cerrar ventana
        if event.type == pygame.QUIT:
            run = False

        # click mouse
        if event.type == pygame.MOUSEBUTTONDOWN:

            if estado_juego == "menu":

                if boton_jugar.collidepoint(event.pos):

                    pygame.mixer.music.load("assets//music//musica//Awake_Celeste.mp3")
                    pygame.mixer.music.play(-1)

                    estado_juego = "jugando"

                if boton_salir.collidepoint(event.pos):

                    run = False

        # tecla presionada
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_c:
                mostrar_hitbox = not mostrar_hitbox

            if event.key == pygame.K_a:
                mover_izquierda = True

            if event.key == pygame.K_d:
                mover_derecha = True

            if event.key == pygame.K_w:
                mover_arriba = True

            if event.key == pygame.K_s:
                mover_abajo = True

        # tecla soltada
        if event.type == pygame.KEYUP:

            if event.key == pygame.K_a:
                mover_izquierda = False

            if event.key == pygame.K_d:
                mover_derecha = False

            if event.key == pygame.K_w:
                mover_arriba = False

            if event.key == pygame.K_s:
                mover_abajo = False

    pygame.display.update()

pygame.quit()