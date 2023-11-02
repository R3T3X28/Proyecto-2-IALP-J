import pygame, sys, random
from tablero import tableroNiv1, tableroNiv2

# ----------------------------------------------------------- INICIALIZAR PYGAME -------------------------------------------------------

pygame.init()
pygame.mixer.init()
pantalla = pygame.display.set_mode((600, 700))
pygame.display.set_caption("Pac-Man")
reloj = pygame.time.Clock()
textoFuente = pygame.font.Font("Pixeltype.ttf", 50)

ANCHO = 18
ALTO = 18
MARGEN = 1

# ----------------------------------------------------------- IMAGENES Y OBJETOS -------------------------------------------------------

# Fondo

# Entidades

# Jugador
imgJugadorArr = pygame.image.load("imagenes/pacman_nor.gif")
imgJugadorArr = pygame.transform.scale(imgJugadorArr, (18, 18))
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
imgBordeEst = pygame.transform.scale(imgBordeEst, (18, 18))
imgBordeOes = pygame.image.load("Muros/Borde_O.png")
imgBordeOes = pygame.transform.scale(imgBordeOes, (18, 18))
imgBordeNor = pygame.image.load("Muros/Borde_N.png")
imgBordeNor = pygame.transform.scale(imgBordeNor, (18, 18))
imgBordeSur = pygame.image.load("Muros/Borde_S.png")
imgBordeSur = pygame.transform.scale(imgBordeSur, (18, 18))
imgBordeEsqSupDer = pygame.image.load("Muros/Esq_NE.png")
imgBordeEsqSupDer = pygame.transform.scale(imgBordeEsqSupDer, (18, 18))
imgBordeEsqSupIzq = pygame.image.load("Muros/Esq_NO.png")
imgBordeEsqSupIzq = pygame.transform.scale(imgBordeEsqSupIzq, (18, 18))
imgBordeEsqInfDer = pygame.image.load("Muros/Esq_SE.png")
imgBordeEsqInfDer = pygame.transform.scale(imgBordeEsqInfDer, (18, 18))
imgBordeEsqInfIzq = pygame.image.load("Muros/Esq_SO.png")
imgBordeEsqInfIzq = pygame.transform.scale(imgBordeEsqInfIzq, (18, 18))
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

# pacman = pygame.image.load("pacman.png")
# pacman = pygame.transform.scale(pacman, (ANCHO, ALTO))

# ---------------------------------------------------------------- CLASES ------------------------------------------------------------
class Fondo:
    titulo = ""

    def __init__(self, titulo):
        self.titulo = titulo

    def dibFondo(self, pantalla):
        pantalla.blit(self.titulo,(300,50))

class Juego:
    nivel = 1
    nJuego = 0
    tablero = []
    score = 0 

    def __init__(self):
        self.nivel = 1
        self.nJuego = 0
        self.tablero = tableroNiv1
        self.score = 0

    def set_nivel(self, nivel):
        self.nivel = nivel

    def get_nivel(self):
        return self.nivel

    def iniciarJuego(self):
        return 0

class PacMan:
    posY = 0
    posX = 0
    velMov = 0
    ModoInicioPoder = False
    ModoFinalPoder = False
    imgJugador = ""
    Estado = False

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

    def moverDere(self):
        if self.velMov == 1:
            self.posX += ANCHO
        else:
            self.posX += 2 * ANCHO
    
    def moverIzq(self):
        if self.velMov == 1:
            self.posX -= ANCHO
        else:
            self.posX -= 2 * ANCHO
    
    def moverArr(self):
        if self.velMov == 1:
            self.posY -= ALTO
        else:
            self.posY -= 2 * ALTO

    def moverAba(self):
        if self.velMov == 1:
            self.posY += ALTO
        else:
            self.posY += 2 * ALTO

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

class Fantasma_Rojo(Enemigo):
    def __init__(self, posX, posY, imgEntidad):
        super().__init__(posX, posY, imgEntidad)

class Fantasma_Celeste(Enemigo):
    def __init__(self, posX, posY, imgEntidad):
        super().__init__(posX, posY, imgEntidad)
    
class Fantasma_Rosado(Enemigo):
    def __init__(self, posX, posY, imgEntidad):
        super().__init__(posX, posY, imgEntidad)
