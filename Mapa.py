import pygame
from enemigos import enemigo
tamano = 30
azul = (152, 217, 234)
verde = (0, 170, 0)
blanco = (255,255,255)
negro = (0, 0, 0)
hueso = (230, 214, 144)
transparemte=()
class Mapa:
    pizo = pygame.image.load("data/imagenes/pizo.png")
    pizo2 = pygame.image.load("data/imagenes/pizo2.png")
    
    espacio = 0
    enemigos = []
    def init(self, pantalla):
        f = open("mapa.txt", "r")
        for (idx, fila) in enumerate(f):
            for(idx2, col) in enumerate(fila):
                posx = idx2 * tamano - self.espacio
                posy = idx * tamano
                if col == "e":
                    nuevo_enemigo = enemigo()
                    nuevo_enemigo.init(pantalla, posx, posy)
                    self.enemigos.append(nuevo_enemigo)
                if col == "r":
                    nuevo_enemigo = enemigo()
                    nuevo_enemigo.init(pantalla, posx, posy)
                    self.enemigos.append(nuevo_enemigo)
        f.close()   
    def Actualizar (self, mario):
        for enem in self.enemigos:
            enem.actualizar(mario, self.espacio)
    def dibujar (self, pantalla, mario):
        self.pared = pygame.image.load("data/imagenes/pared.png").convert_alpha()
        self.pared.set_colorkey((0, 0, 0))
        self.pared = self.pared.convert()

        W, H = 1000, 600
        nivel1 = pygame.image.load("data/imagenes/fondo.jpeg").convert_alpha()
        x= 0
        x_relativa = x % nivel1.get_rect().width
        pantalla.blit(nivel1, (0,0))
        if x_relativa < W:
            pantalla.blit(nivel1, (x_relativa, 0))
        x -= 1
        if mario.x > 650:
            mario.x = 650
            self.espacio += mario.velocidad
        if mario.x < 300 and self.espacio > 0:
            mario.x = 300
            self.espacio -= mario.velocidad
        if self.espacio < 0:
            self.espacio = 0
        f = open("mapa.txt", "r")
        for (idx, fila) in enumerate(f):
            for(idx2, col) in enumerate(fila):
                posx = idx2 * 30 - self.espacio
                posy = idx * 30
                if col == "2":
                    bloque = pygame.draw.rect(pantalla, hueso, (0, 0, 1300, 60))
                    pantalla.blit(pygame.transform.scale(self.pared, (tamano * 1, tamano)), (posy, posy))
                if col == "t":
                    rect = mario.parado.get_rect(x=mario.x, y=mario.y)
                    bloque = pygame.draw.rect(pantalla, 0, (posx, posy, tamano * 1, tamano))
                    pantalla.blit(pygame.transform.scale(self.pared, (tamano * 1, tamano)), (posx, posy))
                    if bloque.colliderect(rect):
                        if rect.x + rect.width > posx and rect.x < posx + tamano * 1:
                            if mario.direccion_actual == 1:
                                mario.x = posx - rect.width
                            else:
                                mario.x = posx + tamano * 1
                if col == "w" or col == "r":
                    rect = mario.parado.get_rect(x=mario.x, y=mario.y)
                    bloque = pygame.draw.rect(pantalla, verde, (posx, posy, tamano * 1, tamano))
                    pantalla.blit(pygame.transform.scale(self.pizo, (tamano * 1, tamano)), (posx, posy))
                    if bloque.colliderect(rect):
                        if rect.y + rect.height < posy + 10 and rect.x + rect.width > posx and rect.x < posx + (tamano * 1):
                            mario.tierra = True
                        elif rect.y > posy + tamano -20 and rect.x + rect.width > posx and rect.x < posx + (tamano * 1):
                            mario.velocidady = mario.gravedad
                        elif rect.x + rect.width > posx and rect.x < posx + tamano * 1:
                            if mario.direccion_actual == 1:
                                mario.x = posx - rect.width
                            else:
                                mario.x = posx + tamano * 1
                if col == "d"  or col == "e":
                    rect = mario.parado.get_rect(x=mario.x, y=mario.y)
                    bloque = pygame.draw.rect(pantalla, verde, (posx, posy, tamano * 1, tamano))
                    pantalla.blit(pygame.transform.scale(self.pizo2, (tamano * 1, tamano)), (posx, posy))
                    if bloque.colliderect(rect):
                        if rect.y + rect.height < posy + 10 and rect.x + rect.width > posx and rect.x < posx + (tamano * 1):
                            mario.tierra = True
                        elif rect.y > posy + tamano -20 and rect.x + rect.width > posx and rect.x < posx + (tamano * 1):
                            mario.velocidady = mario.gravedad
                        elif rect.x + rect.width > posx and rect.x < posx + tamano * 1:
                            if mario.direccion_actual == 1:
                                mario.x = posx - rect.width
                            else:
                                mario.x = posx + tamano * 1

        for enem in self.enemigos:
            enem.dibujar(pantalla, self.espacio)
        f.close()