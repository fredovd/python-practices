import sys
import pygame
def comprobar_eventos(nave):
    """Responder a las teclas y eventos del raton"""
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            sys.exit()
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_RIGHT:
                # Mover la nave a la derecha poniendo el estado del contro del movimiento en verdadero
                nave.mover_derecha = True
            elif evento.key == pygame.K_LEFT:
                nave.mover_izquierda = True

        #Si levantamos la mano de la tecla paramos el movimiento a la derecha. Valor a falso.
        elif evento.type == pygame.KEYUP:
            if evento.key == pygame.K_RIGHT:
                nave.mover_derecha = False
            elif evento.key == pygame.K_LEFT:
                nave.mover_izquierda = False

def actualizar_pantalla(ai_settings, pantalla, nave):
    """Actualizar las imagenes en la pantalla and flip a nueva pantalla"""
    #Rerdibiujar la pantalla por cada pase del loop.
    pantalla.fill(ai_settings.bg_color)
    nave.blitme()
    # Crear el dibujo mas reciente de la pantalla
    pygame.display.flip()
