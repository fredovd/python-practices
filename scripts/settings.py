class Settings():
    """ Una clase para almacenar la configuracion del juego"""
    def __init__(self):
        """Inicializamos la configuracion del juego"""
        # Configuracion de la pantalla
        self.pantalla_ancho = 1200
        self.pantalla_alto = 800
        self.bg_color = (230, 230, 230)
        # Configuracion de la nave
        self.nave_factor_velocidad = 1.5
        # Configuracion de las balas
        self.bala_velocidad_factor = 1
        self.bala_ancho = 3
        self.bala_altura = 15
        self.bala_color = 60, 60, 60
        self.balas_permitidas = 3
