import pygame, sys, math
from tablero import tableroNiv1, tableroNiv2
from PacmanBase import *

pygame.init()
pantalla = pygame.display.set_mode((685, 760))
pygame.display.set_caption("Ejemplo de matriz en Pygame")
reloj = pygame.time.Clock()

# Los valores que definen las dimensiones de las casillas
ANCHO = 18
ALTO = 18
MARGEN = 1
#jugador = PacMan(5*ANCHO, 1*ALTO)


# crear el objeto de la clase juego
juego = Juego()
nivel_actual = juego.get_nivel() 
matriz = juego.tablero

# Dibujar la matriz. Esta funcion se corre dentro del game loop para actualizar el tablero
def dibujarMatriz():
    for fila in range(40):
        for columna in range(36):
            if matriz[fila][columna] == 9: # linea vertical Oeste
                pantalla.blit(imgBordeOes, (columna*ANCHO, fila*ALTO))
            if matriz[fila][columna] == 8: # linea horizontal Este
                pantalla.blit(imgBordeEst, (columna*ANCHO, fila*ALTO))
            if matriz[fila][columna] == 7: # linea horizontal Sur
                pantalla.blit(imgBordeSur, (columna*ANCHO, fila*ALTO))
            if matriz[fila][columna] == 6: # linea vertical Norte
                pantalla.blit(imgBordeNor, (columna*ANCHO, fila*ALTO))
            if matriz[fila][columna] == 5: # esquina superior derecha
                pantalla.blit(imgBordeEsqSupDer, (columna*ANCHO, fila*ALTO))
            if matriz[fila][columna] == 4: # esquina superior izquierda
                pantalla.blit(imgBordeEsqSupIzq, (columna*ANCHO, fila*ALTO))
            if matriz[fila][columna] == 3: # esquina inferior derecha
                pantalla.blit(imgBordeEsqInfDer, (columna*ANCHO, fila*ALTO))
            if matriz[fila][columna] == 2: # esquina inferior izquierda
                pantalla.blit(imgBordeEsqInfIzq, (columna*ANCHO, fila*ALTO))
            if matriz[fila][columna] == 1: # bloque de 1x1 Vacio
                pantalla.blit(imgBloqueVacio, (columna*ANCHO, fila*ALTO))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                posX += ANCHO
            elif event.key == pygame.K_a:
                posX -= ANCHO
            elif event.key == pygame.K_w:
                posY -= ALTO
            elif event.key == pygame.K_s:
                posY += ALTO
    
    pantalla.fill("black")
    dibujarMatriz()
    # dibujar a pacman en la pantalla
    #pantalla.blit(jugador.imgJugador,(posX, posY))

    reloj.tick(60)
    pygame.display.update()
