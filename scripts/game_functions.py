import sys
import pygame
def comprobar_eventos(nave):
    """Responder a las teclas y eventos del raton"""
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            sys.exit()
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_RIGHT:
                # Mover la nave a la derecha
                nave.recta.centerx += 1

def actualizar_pantalla(ai_settings, pantalla, nave):
    """Actualizar las imagenes en la pantalla and flip a nueva pantalla"""
    #Rerdibiujar la pantalla por cada pase del loop.
    pantalla.fill(ai_settings.bg_color)
    nave.blitme()
    # Crear el dibujo mas reciente de la pantalla
    pygame.display.flip()
