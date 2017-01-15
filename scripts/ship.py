import pygame

class Nave():

    def __init__(self, pantalla,ai_settings):
        """Inicializamos la nave y configuramos su posicion inicial"""
        self.pantalla = pantalla
        self.ai_settings = ai_settings

        #Cargamos la imagen de la nave y conseguimos su recta.
        self.imagen = pygame.image.load('images/ship.bmp')
        self.recta = self.imagen.get_rect()
        self.pantalla_recta = pantalla.get_rect()

        #comenzamos cada nave al fondo de la pantalla centrada
        self.recta.centerx = self.pantalla_recta.centerx
        self.recta.bottom = self.pantalla_recta.bottom

        #Almacenar un valor decimal para el centro de la nave
        self.center = float(self.recta.centerx)

        # Control del movimiento
        self.mover_derecha = False
        self.mover_izquierda = False

    def actualizar(self):
        """Actualizar la posicion de la nave basada en el control del movimiento"""
        #Actualizar el valor del centro de la nave, no la recta.
        if self.mover_derecha and self.recta.right < self.pantalla_recta.right:
            self.center += self.ai.setting.nave_factor_velocidad
        if self.mover_izquierda and self.recta.left > 0:
            self.center -= self.ai_settings.nave_factor_velocidad
        #Actualizar el objeto recta desde self.center
        self.recta.centerx = self.center

    def blitme(self):
        """Dibujo la nave en su posicion actual"""
        self.pantalla.blit(self.imagen, self.recta)
