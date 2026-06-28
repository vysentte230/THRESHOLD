import pygame
import constantes

class Joel():
    def __init__(self, x, y):

        self.animaciones = [
            pygame.image.load("assets/images/character/Npc/Prof.Joel/Joel_1.png"),
            pygame.image.load("assets/images/character/Npc/Prof.Joel/Joel_2.png"),
            pygame.image.load("assets/images/character/Npc/Prof.Joel/Joel_3.png"),
            pygame.image.load("assets/images/character/Npc/Prof.Joel/Joel_4.png"),
            pygame.image.load("assets/images/character/Npc/Prof.Joel/Joel_5.png"),
            pygame.image.load("assets/images/character/Npc/Prof.Joel/Joel_6.png"),
            pygame.image.load("assets/images/character/Npc/Prof.Joel/Joel_7.png"),
            pygame.image.load("assets/images/character/Npc/Prof.Joel/Joel_8.png"),
        ]

        for i in range(len(self.animaciones)):
            self.animaciones[i] = pygame.transform.scale(
                self.animaciones[i],
                (constantes.ANCHO_PERSONAJE * 1.5, constantes.ALTO_PERSONAJE * 1.5)
           )

        self.frame = 0
        self.contador_animacion = 0
        self.image = self.animaciones[self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.hitbox = pygame.Rect(x, y, int(constantes.ANCHO_PERSONAJE * 1.5), int(constantes.ALTO_PERSONAJE * 1.5))

    def animar(self):
        self.contador_animacion += 1
        if self.contador_animacion >= 10:
            self.frame = (self.frame + 1) % len(self.animaciones)
            self.image = self.animaciones[self.frame]
            self.contador_animacion = 0

    def dibujar(self, ventana, camera_x, camera_y):
        ventana.blit(
            self.image,
            (self.rect.x - camera_x, self.rect.y - camera_y)
        )