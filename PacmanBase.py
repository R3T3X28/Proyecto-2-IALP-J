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

# Jugador
imgJugadorArr = pygame.image.load("imagenes/pacman_nor.gif")
imgJugadorDer = pygame.image.load("imagenes/pacman_est.gif")
imgJugadorIzq = pygame.image.load("imagenes/pacman_oes.gif")
imgJugadorAba = pygame.image.load("imagenes/pacman_sur.gif")
imgJugadorMuere = pygame.image.load("imagenes/pacman_die.gif")

# Enemigos
imgFantasmaVulnerable = pygame.image.load("imagenes/F1.gif")
imgFantasmaVulneFinal = pygame.image.load("imagenes/F1-2.gif")

    # Fantasma Naranja
imgFantasmaNaranjaArr = pygame.image.load("imagenes/Fnara_nor.gif")
imgFantasmaNaranjaAba = pygame.image.load("imagenes/Fnara_sur.gif")
imgFantasmaNaranjaDer = pygame.image.load("imagenes/Fnara_est.gif")
imgFantasmaNaranjaIzq = pygame.image.load("imagenes/Fnara_oes.gif")

    # Fantasma Rojo
imgFantasmaRojoArr = pygame.image.load("imagenes/Frojo_nor.gif")
imgFantasmaRojoAba = pygame.image.load("imagenes/Frojo_sur.gif")
imgFantasmaRojoDer = pygame.image.load("imagenes/Frojo_est.gif")
imgFantasmaRojoIzq = pygame.image.load("imagenes/Frojo_oes.gif")

    # Fantasma Celeste
imgFantasmaCelesteArr = pygame.image.load("imagenes/Fceles_nor.gif")
imgFantasmaCelesteAba = pygame.image.load("imagenes/Fceles_sur.gif")
imgFantasmaCelesteDer = pygame.image.load("imagenes/Fceles_est.gif")
imgFantasmaCelesteIzq = pygame.image.load("imagenes/Fceles_oes.gif")

    # Fantasma Rosa
imgFantasmaRosaArr = pygame.image.load("imagenes/Frosa_nor.gif")
imgFantasmaRosaAba = pygame.image.load("imagenes/Frosa_sur.gif")
imgFantasmaRosaDer = pygame.image.load("imagenes/Frosa_est.gif")
imgFantasmaRosaIzq = pygame.image.load("imagenes/Frosa_oes.gif")

# Frutas
imgFrutaCereza = pygame.image.load("imagenes/cereza.png")
imgFrutaManzana = pygame.image.load("imagenes/manzana.png")
imgFrutaNaranja = pygame.image.load("imagenes/naranja.png")
imgFrutaPera = pygame.image.load("imagenes/pera.png")
imgFrutaFresa = pygame.image.load("imagenes/fresa.png")

# Sonidos

# Escenario
imgBordeEst = pygame.image.load("Muros/Borde_E.png")
imgBordeOes = pygame.image.load("Muros/Borde_O.png")
imgBordeNor = pygame.image.load("Muros/Borde_N.png")
imgBordeSur = pygame.image.load("Muros/Borde_S.png")
imgBordeEsqSupDer = pygame.image.load("Muros/Esq_NE.png")
imgBordeEsqSupIzq = pygame.image.load("Muros/Esq_NO.png")
imgBordeEsqInfDer = pygame.image.load("Muros/Esq_SE.png")
imgBordeEsqInfIzq = pygame.image.load("Muros/Esq_SO.png")
imgBloque1x2 = pygame.image.load("Muros/Bloque_1x2.png")
imgBloque3x1 = pygame.image.load("Muros/Bloque_3x1.png")
imgBloque1x3 = pygame.image.load("Muros/Bloque_1x3.png")
imgBloqueL180 = pygame.image.load("Muros/Bloque_L180.png")
imgBloqueL360 = pygame.image.load("Muros/Bloque_L360.png")
imgBloqueRect = pygame.image.load("Muros/Bloque_rec4x3.png")
imgBloqueT90 = pygame.image.load("Muros/BloqueT90.png")
imgBloqueT180 = pygame.image.load("Muros/BloqueT180.png")
imgBloqueT270 = pygame.image.load("Muros/BloqueT270.png")
imgBloqueLadoTT = pygame.image.load("Muros/BloqueLadoTT.png")
imgBloqueLadoTT2 = pygame.image.load("Muros/BloqueLadoTT2.png")
imgBloqueLadoTT21 = pygame.image.load("Muros/BloqueLadoTT21.png")
imgBloqueLadoTT22 = pygame.image.load("Muros/BloqueLadoTT22.png")
imgBloqueVacio = pygame.image.load("Muros/Vacio.png")

# ---------------------------------------------------------------- CLASES ------------------------------------------------------------
class Fondo:
    titulo = ""

    def __init__(self, titulo):
        self.titulo = titulo

    def dibFondo(self, pantalla):
        pantalla.blit(self.titulo,(300,50))

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
