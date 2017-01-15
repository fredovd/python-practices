import pygame
from settings import Settings
from ship import Nave
import game_functions as gf

def ejecutar_juego():
    #Inicializamos el juego y creamos el ojeto pantalla
    pygame.init()
    ai_settings = Settings()
    pantalla = pygame.display.set_mode(
        (ai_settings.pantalla_ancho, ai_settings.pantalla_alto))
    pygame.display.set_caption("Invasion Alien")

    bg_color = (230, 230, 230)
    # Hacer una nave
    nave = Nave(pantalla, ai_settings)

    #Comenzamos el loop principal del juego
    while True:
        gf.comprobar_eventos(nave)
        nave.actualizar()
        gf.actualizar_pantalla(ai_settings, pantalla, nave)

ejecutar_juego()
