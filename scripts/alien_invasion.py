import sys

import pygame
from settings import Settings


def ejecutar_juego():
    #Inicializamos el juego y creamos el ojeto pantalla
    pygame.init()
    ai_settings = Settings()
    pantalla = pygame.display.set_mode((ai_settings.pantalla_ancho, ai_settings.pantalla_alto))
    pygame.display.set_caption("Invasion Alien")


    #Comenzamos el loop principalp del juego
    while True:

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                sys.exit()

                #Dibujamos la pantalla durante cada pase del loop
                pantalla.fill(ai_settings.bg_color)

                #Hacemos visible el dibujo de la pantalla mas reciente
                pygame.display.flip()

ejecutar_juego()
