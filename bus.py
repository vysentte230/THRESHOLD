import pygame

class Bus():

    def __init__(self, x, y):

        self.animaciones = [

            pygame.image.load("assets/images/objects/bus_1.png"),
            pygame.image.load("assets/images/objects/bus_2.png"),
            pygame.image.load("assets/images/objects/bus_3.png"),
            pygame.image.load("assets/images/objects/bus_4.png"),
            pygame.image.load("assets/images/objects/bus_5.png")

        ]

        self.frame = 0
        self.contador_animacion = 0

        self.image = self.animaciones[self.frame]

        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y

        self.velocidad = 5

    def mover(self):

        self.rect.y += self.velocidad

        # reaparecer arriba
        if self.rect.y > 1200:

            self.velocidad = 0

    def animar(self):

        self.contador_animacion += 1

        if self.contador_animacion >= 10:

            self.frame += 1

            if self.frame >= len(self.animaciones):

                self.frame = 0

            self.image = self.animaciones[self.frame]

            self.contador_animacion = 0

    def dibujar(self, ventana):

        ventana.blit(self.image, self.rect)