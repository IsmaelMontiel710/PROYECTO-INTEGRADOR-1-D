import sys
import pygame
import button

# create display window
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1000

pygame.display.set_caption('data/imagenes/icono.PNG')
icon = pygame.image.load('data/imagenes/icono.PNG')
pygame.display.set_icon (icon)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Monkey Guard')
fondo = pygame.image.load('data/imagenes/Background.jpeg')
# load button images
start_img = pygame.image.load('data/imagenes/start_btn.png').convert_alpha()
exit_img = pygame.image.load('data/imagenes/exit_btn.png').convert_alpha()
#fondo = pygame.image.load('fon<z<zzdo.jpeg').convert()

# create button instances
start_button = button.Button(200, 425, start_img, 0.8)
exit_button = button.Button(200, 550, exit_img, 0.8)

# game loop
run = True
while run:

    screen.blit(fondo, [0, 0])

    if not start_button.draw(screen):
        pass
    else:

        exec(open('./Niveles.py', encoding="utf-8").read())
        sys.exit()
    if exit_button.draw(screen):
        sys.exit()
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
