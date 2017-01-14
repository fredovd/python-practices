import pygame

class Nave():

    def __init__(self, pantalla):
        """Inicializamos la nave y configuramos su posicion inicial"""
        self.pantalla = pantalla

        #Cargamos la imagen de la nave y conseguimos su recta.
        self.imagen = pygame.image.load('images/ship.bmp')
        self.recta = self.imagen.get_rect()
        self.pantalla_recta = pantalla.get_rect()

        #comenzamos cada nave al fondo de la pantalla centrada
        self.recta.centerx = self.pantalla_recta.centerx
        self.recta.bottom = self.pantalla_recta.bottom

        # Control del movimiento
        self.mover_derecha = False
        self.mover_izquierda = False

    def actualizar(self):
        """Actualizar la posicion de la nave basada en el control del movimiento"""
        if self.mover_derecha:
            self.recta.centerx += 1
        if self.mover_izquierda:
            self.recta.centerx -= 1

    def blitme(self):
        """Dibujo la nave en su posicion actual"""
        self.pantalla.blit(self.imagen, self.recta)
