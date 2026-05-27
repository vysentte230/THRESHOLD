import pygame
import constantes
from personaje import Personaje

jugador = Personaje(50, 50,)

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

while run == True:

    # indicar que vaya a 60 fps
    reloj.tick(constantes.FPS)

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
    
    if estado_juego == "jugando":

        #mov jugador
        delta_x = 0
        delta_y = 0

        if mover_arriba == True:
            delta_y = -5

        if mover_abajo == True:
            delta_y = 5

        if mover_izquierda == True:
            delta_x = -5

        if mover_derecha == True:
            delta_x = 5

        # movimiento jugador
        jugador.movimiento(delta_x, delta_y)

        jugador.dibujar(ventana)


    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if estado_juego == "menu":
                if boton_jugar.collidepoint(event.pos):
                    pygame.mixer.music.load("assets//music//musica//Awake_Celeste.mp3")
                    pygame.mixer.music.play(-1)
                    
                    estado_juego = "jugando"
                if boton_salir.collidepoint(event.pos):
                    run = False    

        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_a:
                mover_izquierda = True

            if event.key == pygame.K_d:
                mover_derecha = True

            if event.key == pygame.K_s:
                mover_abajo = True

            if event.key == pygame.K_w:
                mover_arriba = True

        # para que al soltar la tecla el personaje se detenga
        if event.type == pygame.KEYUP:

            if event.key == pygame.K_a:
                mover_izquierda = False

            if event.key == pygame.K_d:
                mover_derecha = False

            if event.key == pygame.K_s:
                mover_abajo = False

            if event.key == pygame.K_w:
                mover_arriba = False

    pygame.display.update()



pygame.quit()
