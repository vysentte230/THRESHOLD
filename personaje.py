import pygame
import constantes
import os
class Personaje():
    def __init__(self, x, y):
        
     self.animaciones = {}
    
     self.animaciones["abajo"] = [
    pygame.image.load("assets/images/character/Player/Player.png"),
    pygame.image.load("assets/images/character/Player/frente2.png"),
    pygame.image.load("assets/images/character/Player/frente3.png"),
    pygame.image.load("assets/images/character/Player/frente4.png")
     ]

     self.animaciones["arriba"] = [
    pygame.image.load("assets/images/character/Player/Arriba1.png"),
    pygame.image.load("assets/images/character/Player/arriba2.png"),
    pygame.image.load("assets/images/character/Player/arriba3.png"),
    pygame.image.load("assets/images/character/Player/arriba4.png")
     ]

     self.animaciones["izquierda"] = [
    pygame.image.load("assets/images/character/Player/izquierda1.png"),
    pygame.image.load("assets/images/character/Player/izquierda2.png"),
    pygame.image.load("assets/images/character/Player/izquierda3.png"),
    pygame.image.load("assets/images/character/Player/izquierda4.png")
     ]

     self.animaciones["derecha"] = [
    pygame.image.load("assets/images/character/Player/derecha1.png"),
    pygame.image.load("assets/images/character/Player/derecha2.png"),
    pygame.image.load("assets/images/character/Player/derecha3.png"),
    pygame.image.load("assets/images/character/Player/derecha4.png")
     ]

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
        
        












        
