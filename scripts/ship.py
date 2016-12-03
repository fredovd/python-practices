import pygame

class Nave():

    def __init__(self, pantalla):
        """Inicializamos la nave y configuramos su posicion inicial"""
        self.pantalla = pantalla

        #Cargamos la imagen de la nave y conseguimos sus recta.
        self.imagen = pygame.image.load('images/ship.bmp')
        self.recta = self.imagen.get_rect()
        self.pantalla_recta = pantalla.get_rect()

        #comenzamos cada nave al fondo de la pantalla centrada
        self.recta.centerx = self.pantalla_recta.centerx
        self.recta.bottom = self.pantalla_recta.bottom

    def blitme(self):
        """Dibujo la nave en su posicion actual"""
        self.pantalla.blit(self.imagen, self.recta)
