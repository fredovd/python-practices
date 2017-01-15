import sys
import pygame
from bullet import Bullet

def comprobar_teclapulsada_eventos(evento, ai_settings, pantalla, nave, bullets):
    """Responder a la tecla presionada"""
    if evento.key == pygame.K_RIGHT:
        nave.mover_derecha = True
    elif evento.key == pygame.K_LEFT:
        nave.mover_izquierda = True
    elif evento.key == pygame.K_SPACE:
        disparar_bala(ai_settings, pantalla, nave, bullets)

def comprobar_teclasoltada_eventos(evento, nave):
    """Responde al dejar de pulsar la tecla"""
    if evento.key == pygame.K_RIGHT:
        nave.mover_derecha = False
    elif evento.key == pygame.K_LEFT:
        nave.mover_izquierda = False

def comprobar_eventos(ai_settings, pantalla, nave, bullets):
    """Responder a las teclas y eventos del raton"""
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            sys.exit()
        elif evento.type == pygame.KEYDOWN:
            comprobar_teclapulsada_eventos(evento, ai_settings, pantalla, nave, bullets)
        elif evento.type == pygame.KEYUP:
            comprobar_teclasoltada_eventos(evento, nave)

def disparar_bala(ai_settings, pantalla, nave, bullets):
    """Disparar una bala y anadirlo al grupo de las balas"""
    # Crear una nueva bala y anadirla al grupo de balas
    if len(bullets) < ai_settings.balas_permitidas:
        new_bullet = Bullet(ai_settings, pantalla, nave)
        bullets.add(new_bullet)

def actualizar_pantalla(ai_settings, pantalla, nave, bullets):
    """Actualizar las imagenes en la pantalla and flip a nueva pantalla"""
    #Rerdibiujar la pantalla por cada pase del loop.
    pantalla.fill(ai_settings.bg_color)
    # Redibujar todas las balas detras de la nave y los aliens
    for bullet in bullets.sprites():
        bullet.dibujar_bala()
    nave.blitme()

    # Crear el dibujo mas reciente de la pantalla
    pygame.display.flip()

def actualizar_balas(bullets):
    """Actualizar la posicion de las balas y deshacerse de las viejas."""
    # Actualizar la posicion de las balas
    bullets.update()

    #Deshacerse de las balas que han desaparedcido.
    for bullet in bullets.copy():
        if bullet.recta.bottom <= 0:
            bullets.remove(bullet)
