import pygame
import constantes
import os
class Personaje():
    def __init__(self, x, y):
        
     self.animaciones = {}
    
     self.animaciones["abajo"] = [
    pygame.image.load("assets/images/character/Player/Modelo_1/Abajo/abajo1_1.png"),
    pygame.image.load("assets/images/character/Player/Modelo_1/Abajo/abajo1_2.png"),
    pygame.image.load("assets/images/character/Player/Modelo_1/Abajo/abajo1_3.png"),
    pygame.image.load("assets/images/character/Player/Modelo_1/Abajo/abajo1_4.png"),
     ]

     self.animaciones["arriba"] = [
    pygame.image.load("assets/images/character/Player/Modelo_1/Arriba/arriba1_1.png"),
    pygame.image.load("assets/images/character/Player/Modelo_1/Arriba/arriba1_2.png"),
    pygame.image.load("assets/images/character/Player/Modelo_1/Arriba/arriba1_3.png"),
    pygame.image.load("assets/images/character/Player/Modelo_1/Arriba/arriba1_4.png"),
     ]

     self.animaciones["izquierda"] = [
    pygame.image.load("assets/images/character/Player/Modelo_1/Izquierda/izquierda1_1.png"),
    pygame.image.load("assets/images/character/Player/Modelo_1/Izquierda/izquierda1_2.png"),
    pygame.image.load("assets/images/character/Player/Modelo_1/Izquierda/izquierda1_3.png"),
    pygame.image.load("assets/images/character/Player/Modelo_1/Izquierda/izquierda1_4.png"),
     ]

     self.animaciones["derecha"] = [
    pygame.image.load("assets/images/character/Player/Modelo_1/Derecha/derecha1_1.png"),
    pygame.image.load("assets/images/character/Player/Modelo_1/Derecha/derecha1_2.png"),
    pygame.image.load("assets/images/character/Player/Modelo_1/Derecha/derecha1_3.png"),
    pygame.image.load("assets/images/character/Player/Modelo_1/Derecha/derecha1_4.png"),
     ]

     # Escalar todas las imágenes del personaje
     for direccion in self.animaciones:
         for i in range(len(self.animaciones[direccion])):
             self.animaciones[direccion][i] = pygame.transform.scale(
                 self.animaciones[direccion][i],
                 (
                     constantes.ANCHO_PERSONAJE,
                     constantes.ALTO_PERSONAJE
                 )
             )

     # dirección actual
     self.direccion = "abajo"

     # frame actual
     self.frame = 0

     # imagen inicial
     self.image = self.animaciones[self.direccion][self.frame]

     # velocidad animación
     self.contador_animacion = 0

     self.forma = pygame.Rect(0, 0, constantes.ANCHO_PERSONAJE,
                                 constantes.ALTO_PERSONAJE)
     self.forma.center = (x, y)
    
    def movimiento(self, delta_x, delta_y, paredes):

        # movimiento horizontal
        self.forma.x += delta_x

        for pared in paredes:
            if self.forma.colliderect(pared):

                if delta_x > 0:
                    self.forma.right = pared.left

                if delta_x < 0:
                    self.forma.left = pared.right

        # movimiento vertical
        self.forma.y += delta_y

        for pared in paredes:
            if self.forma.colliderect(pared):

                if delta_y > 0:
                    self.forma.bottom = pared.top

                if delta_y < 0:
                    self.forma.top = pared.bottom

        moviendo = False

        # dirección
        if delta_y > 0:
            self.direccion = "abajo"
            moviendo = True

        if delta_y < 0:
            self.direccion = "arriba"
            moviendo = True

        if delta_x < 0:
            self.direccion = "izquierda"
            moviendo = True

        if delta_x > 0:
            self.direccion = "derecha"
            moviendo = True

        # animación
        if moviendo:

            self.contador_animacion += 1

            if self.contador_animacion >= 10:

                self.frame += 1

                if self.frame >= 4:
                    self.frame = 0

                self.contador_animacion = 0

            self.image = self.animaciones[self.direccion][self.frame]
   
    def dibujar(self, interfaz):
        interfaz.blit(self.image, self.forma)
        
        












        
