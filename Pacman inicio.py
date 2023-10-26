import pygame, sys, random

# ----------------------------------------------------------- INICIALIZAR PYGAME -------------------------------------------------------

pygame.init()
pygame.mixer.init()
pantalla = pygame.display.set_mode((600, 700))
pygame.display.set_caption("Pac-Man")
reloj = pygame.time.Clock()
textoFuente = pygame.font.Font("Pixeltype.ttf", 50)

# ----------------------------------------------------------- IMAGENES Y OBJETOS -------------------------------------------------------

# Fondo

# Entidades

# Sonidos

# ---------------------------------------------------------------- CLASES ------------------------------------------------------------
class Fondo:
    titulo = ""

    def __init__(self, titulo):
        self.titulo = titulo

    def dibFondo(self, pantalla):
        pantalla.blit(self.titulo,(0,0))

class Jugador:
    posF = 0
    posC = 0
    velMov = 0
    ModoInicioPoder = False
    ModoFinalPoder = False
    imgJugador = ""

    def __init__(self, posX, posY):
        self.posX = posX
        self.posY = posY
        self.velMov = 0
        self.ModoInicioPoder = False
        self.ModoFinalPoder = False
        self.imgJugador = ""

    def get_posX(self):
        return self.posX

    def get_posY(self):
        return self.posY

    def get_ModoInicioPoder(self):
        return self.ModoInicioPoder

    def get_ModoFinalPoder(self):
        return self.ModoFinalPoder

    def set_posX(self, posX):
        self.posX = posX

    def set_posY(self, posY):
        self.posY = posY

    def set_ModoInicioPoder(self, ModoInicioPoder):
        self.ModoInicioPoder = ModoInicioPoder

    def set_ModoFinalPoder(self, ModoFinalPoder):
        self.ModoFinalPoder = ModoFinalPoder

    def set_imgJugador(self, imgJugador):
        self.imgJugador = imgJugador

    def dibPantalla(self, pantalla):
        pantalla.blit(self.imgJugador,(self.posX, self.posY))

    def mover(self, velMov):
        self.posX = self.posX + velMov

class Enemigo:
    posX = 0
    posY = 0
    ModoComibleIncio = False
    ModoComibleFinal = False
    imgEntidad = ""

    def __init__(self, posX, posY, imgEntidad):
        self.posX = posX
        self.posY = posY
        self.imgEntidad = imgEntidad

    def get_posX(self):
        return self.posX

    def get_posY(self):
        return self.posY

    def get_imgEntidad(self):
        return self.imgEntidad
    
    def get_ModoComibleIncio(self):
        return self.ModoComibleIncio
    
    def get_ModoComibleFinal(self):
        return self.ModoComibleFinal

    def set_posX(self, posX):
        self.posX = posX

    def set_posY(self, posY):
        self.posY = posY

    def set_imgEntidad(self, imgEntidad):
        self.imgEntidad = imgEntidad

    def set_ModoComibleIncio(self, ModoComibleIncio):
        self.ModoComibleIncio = ModoComibleIncio

    def set_ModoComibleFinal(self, ModoComibleFinal):
        self.ModoComibleFinal = ModoComibleFinal

    def dibPantalla(self, pantalla):
        pantalla.blit(self.imgEntidad,(self.posX, self.posY))

    def mover(self, velMov):
        self.posX += velMov

class Fantasma_Naranja(Enemigo):
    def __init__(self, posX, posY, imgEntidad):
        super().__init__(posX, posY, imgEntidad)
