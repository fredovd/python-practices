import pygame

class Nave():

    def __init__(self, pantalla):
        """Inicializamos la nave y configuramos su posición inicial"""
        self.pantalla = pantalla

        #Cargamos la imagen de la nave y conseguimos sus recta.
        self.imagen = pygame.image.load('images/ship.bmp')
        self.recta = self.imagen.get.rect()
        self.pantalla_recta = pantalla.get_rect()
