import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """ Un clase para manegar las balas disparadas por la nave"""

    def __init__(self, ai_settings, pantalla, nave):
        """Creamos un objeto bala en la posicion actual de la nave"""
        super(Bullet, self).__init__()
        self.pantalla = pantalla

        # Crear una recta de la bala en (0, 0) y luego configurar la posicion correcta
        self.recta = pygame.Rect(0, 0, ai_settings.bala_ancho,
            ai_settings.bala_altura)
        self.recta.centerx = nave.recta.centerx
        self.recta.top = nave.recta.top

        # Almacenar la posicion de las balas como valor decimal
        self.y = float(self.recta.y)

        self.color = ai_settings.bala_color
        self.velocidad_factor = ai_settings.bala_velocidad_factor

    def update(self):
        """Mover la bala hacia arriba de la pantalla"""
        # Actualziar la posicion decimal de la bala.
        self.y -= self.velocidad_factor
        # Actualizar la posicion de la recta.
        self.recta.y = self.y

    def dibujar_bala(self):
        """Dibujamos la bala en la pantalla"""
        pygame.draw.rect(self.pantalla, self.color, self.recta)
