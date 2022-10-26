import pygame
from enum import IntEnum

class direccion(IntEnum):
    Izq = 0
    der = 1

class condicion(IntEnum):
    parado = 0
    caminando = 1
    aire = 2

class jugador:
    direccion_actual = direccion["der"]
    x = 0
    y = 0
    velocidadx = 0
    velocidady = 0
    caminando = []
    estado = 1
    cuadro_actual = 0
    contador = 0
    parado = None
    aire = None
    gravedad = 0
    tierra = False
    invertir = False
    def init(self, pantalla):
        self.invertir = False
        self.gravedad = 7
        self.x = 50
        self.y = 518
        self.estado = condicion.aire
        self.velocidad = 5
        self.parado = pygame.image.load('data/imagenes/quieto.png').convert_alpha(pantalla)
        self.aire = pygame.image.load('data/imagenes/salto.png').convert_alpha(pantalla)
        self.caminando.append(pygame.image.load('data/imagenes/quieto.png').convert_alpha(pantalla))
        self.caminando.append(pygame.image.load('data/imagenes/caminando1.png').convert_alpha(pantalla))
        self.caminando.append(pygame.image.load('data/imagenes/caminando2.png').convert_alpha(pantalla))
        self.parado.set_colorkey((255, 255, 255))
        self.parado = self.parado.convert()
        self.aire.set_colorkey((255, 255, 255))
        self.aire = self.aire.convert()

        for (idx, i) in enumerate(self.caminando):
            i.set_colorkey((255, 255, 255))
            self.caminando[idx] = self.caminando[idx].convert()

        self.cuadro_actual = 0
    def eventos(self, event, pantalla):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and self.estado != condicion.aire:
                self.velocidady = -20
                self.estado = condicion.aire
                self.tierra = False
            if event.key == pygame.K_q:
                self.y = 0
            if event.key == pygame.K_LEFT:
                self.direccion_actual = direccion.Izq
                self.velocidadx = -self.velocidad
            if event.key == pygame.K_RIGHT:
                self.direccion_actual = direccion.der
                self.velocidadx = self.velocidad
            if event.key == pygame.K_SPACE and self.estado == 0:
                pass

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                self.velocidadx = 0
            if event.key == pygame.K_RIGHT:
                self.velocidadx = 0
    def actualizar(self):
        if self.tierra:
            self.velocidady = 0
            if self.velocidadx != 0:
                self.estado = condicion.caminando
            if self.velocidadx == 0:
                self.estado = condicion.parado
        self.x += self.velocidadx
        if self.tierra == False:
            self.estado = condicion.aire
        if self.estado == condicion.aire:
            self.velocidady += 1
            if self.velocidady > self.gravedad:
                self.velocidady = self.gravedad
            self.y += self.velocidady
        if self.direccion_actual == direccion.Izq:
            self.invertir = True
        else:
            self.invertir = False
        self.tierra = False
    def dibujar(self, pantalla):
        if self.estado == condicion.parado:
            pantalla.blit(pygame.transform.flip(self.parado, self.invertir, False), (self.x, self.y))
        if self.estado == condicion.aire:
            pantalla.blit(pygame.transform.flip(self.aire, self.invertir, False), (self.x, self.y))
        if self.estado == condicion.caminando:
            self.contador += 1
            if self.contador > 5:
                self.cuadro_actual += 1
                self.contador = 0
                if self.cuadro_actual > 2:
                    self.cuadro_actual = 0
            pantalla.blit(pygame.transform.flip(self.caminando[self.cuadro_actual], self.invertir, False), (self.x, self.y))