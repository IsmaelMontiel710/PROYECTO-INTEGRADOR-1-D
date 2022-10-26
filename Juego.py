import pygame,sys
from pygame import mixer
from Jugador import jugador
from Mapa import Mapa
import button

negro = (0, 0, 0)

pantalla_tamano = (1000, 600)
W,H = 1000, 600
pantalla = pygame.display.set_mode((W,H))
fps=600

pygame.display.set_caption('Monkey Guard')
icon = pygame.image.load('data/imagenes/icono.PNG')
pygame.display.set_icon (icon)

reloj = pygame.time.Clock()
Termino = False
#Inicializar
mapa=Mapa()
mario = jugador()
mario.init(pantalla)


pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.init()
pygame.mixer.quit()
pygame.mixer.init(22050, -16, 2, 512)
pygame.mixer.set_num_channels(32)
jump_sound = pygame.mixer.Sound('data/audio/jump.wav')
mixer.music.load('data/audio/fondo.wav')
mixer.music.play(-1) #El -1 sirve para hacer que se repita la cancion indefinidamente

sonido_arriba = pygame.image.load('data/audio/volume_up.jpg').convert_alpha()
sonido_abajo = pygame.image.load('data/audio/volumen_down.jpg').convert_alpha()
sonido_mute = pygame.image.load('data/audio/volume_muted.jpg').convert_alpha()
sonido_max = pygame.image.load('data/audio/volume_max.jpg').convert_alpha()

mapa.init(pantalla=pantalla)
while not Termino:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Termino = True
        #Eventos
        mario.eventos(event, pantalla)
    
    mario.actualizar()
    mapa.Actualizar(mario)
    pantalla.fill(negro)
    #Dibujar
    mapa.dibujar(pantalla, mario)
    mario.dibujar(pantalla)
    pygame.display.flip()
    reloj.tick(fps)

    keys = pygame.key.get_pressed()
	# Control del audio
	# Baja volumen
    if keys[pygame.K_9] and pygame.mixer.music.get_volume() > 0.0:
        pygame.mixer.music.set_volume(pygame.mixer.music.get_volume() -0.01)
        pantalla.blit(sonido_abajo, (850, 25))
    elif keys[pygame.K_9] and pygame.mixer.music.get_volume() == 0.0:
        pantalla.blit(sonido_mute, (850, 25))
    # Sube volumen
    if keys[pygame.K_0] and pygame.mixer.music.get_volume() < 1.0:
        pygame.mixer.music.set_volume(pygame.mixer.music.get_volume() + 0.01)
        pantalla.blit(sonido_arriba, (850, 25))
    elif keys[pygame.K_0] and pygame.mixer.music.get_volume() < 1.0:
        pantalla.blit(sonido_max, (850, 25))
    # Desactivar sonido
    elif keys[pygame.K_m]:
        pygame.mixer.music.set_volume(0.0)
        pantalla.blit(sonido_mute, (850, 25))
    # Reactivar el sonido
    elif keys[pygame.K_COMMA]:
        pygame.mixer.music.set_volume(1.0)
        pantalla.blit(sonido_max, (850, 25))
    pygame.display.update
    #Salir con boton Esc
    if keys[pygame.K_ESCAPE]:
        sys.exit()
# Salida del juego
pygame.quit()