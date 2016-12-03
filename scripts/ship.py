import pygame

class Nave():

    def __init__(self, pantalla):
        """Inicializamos la nave y configuramos su posición inicial"""
        self.pantalla = pantalla

        #Cargamos la imagen de la nave y conseguimos sus recta.
        self.imagen = pygame.image.load('images/ship.bmp')
        self.recta = self.imagen.get_recta()
        self.pantalla_recta = pantalla.get_recta()

        #comenzamos cada nave al fondo de la pantalla centrada
        self.recta.centerx = self.pantalla_recta.centerx
        self.recta.fondo = self.pantalla_recta.fondo

    def blitgme(self):
        """Dibujo la nave en su posición actual"""
        self.pantalla.blit(self.imagen, self.recta)
