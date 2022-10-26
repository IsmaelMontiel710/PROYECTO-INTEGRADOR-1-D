import sys
import pygame
import button

# create display window
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1000

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Monkey Guard')

# load button images
level1_img = pygame.image.load('data/imagenes/level1.png').convert_alpha()
exit_img = pygame.image.load('data/imagenes/exit_btn.png').convert_alpha()
#fondo = pygame.image.load('fon<z<zzdo.jpeg').convert()

# create button instances
level1_button = button.Button(150, 200, level1_img, 0.8)
exit_button = button.Button(450, 200, exit_img, 0.8)

# game loop
run = True
while run:

    #screen.fill((202, 228, 241))

    if not level1_button.draw(screen):
        pass
    else:
        exec(open('./Juego.py', encoding="utf-8").read())
        sys.exit()
    if exit_button.draw(screen):
        pass
        exec(open('./button_main.py', encoding="utf-8").read())
        sys.exit()
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
