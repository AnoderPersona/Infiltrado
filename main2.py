import pygame
import sys
import os
import random
from pygame.locals import *


#================================================================
#                       Despliega matriz
#================================================================

def crea_cuadrado(x: int, y: int, color: tuple, alto_cuadrado: int, ancho_cuadrado:int):

    pygame.draw.rect(ventana, color, [x, y, ancho_cuadrado, alto_cuadrado ])

def despliega_matriz(alto_cuadrado: int, ancho_cuadrado: int, matrix: list):

    y = 0  # we start at the top of the screen
    for row in matrix:
        x = 0 # for every row we start at the left of the screen again
        for item in row:

            #pared
            if item == 0:
                crea_cuadrado(x, y, (255, 255, 255), alto_cuadrado, ancho_cuadrado) #blanco
            #pieza
            elif item == 1:
                crea_cuadrado(x, y, (200, 100, 60), alto_cuadrado, ancho_cuadrado) #naranjo
            #pasillo o ex-moneda
            elif item == 2:
                crea_cuadrado(x, y, (100, 200, 50), alto_cuadrado, ancho_cuadrado) #verde
            #obstaculo
            elif item == -1:
                crea_cuadrado(x, y, (200, 50, 100), alto_cuadrado, ancho_cuadrado) #rosado oscuro
            #moneda
            elif item == -2:
                crea_cuadrado(x, y, (200, 200, 20), alto_cuadrado, ancho_cuadrado) #verde amarillo


            x += ancho_cuadrado # for ever item/number in that row we move one "step" to the right
        y += alto_cuadrado   # for every new row we move one "step" downwards
    pygame.display.update()

#================================================================
#                       Generacion random
#================================================================

def agrega_obstaculos(mat: list, n: int):

    for i in range(n):

        x = random.randrange(0,len(mat))
        y = random.randrange(0,len(mat[0]))

        while (mat[y][x] != 1):
            x = random.randrange(0,len(mat))
            y = random.randrange(0,len(mat[0]))

        mat[y][x] = -1

    return mat

def agrega_monedas(mat: list, n: int):

    for i in range(n):

        x = random.randrange(0,len(mat))
        y = random.randrange(0,len(mat[0]))

        while (mat[y][x] < 1):
            x = random.randrange(0,len(mat))
            y = random.randrange(0,len(mat[0]))

        mat[y][x] = -2

    return mat

def posicion_amigos(mat: list, pos: list):

    x = random.randrange(0,len(mat))
    y = random.randrange(0,len(mat[0]))

    while (mat[y][x] < 1 or [y,x] in pos):
        x = random.randrange(0,len(mat))
        y = random.randrange(0,len(mat[0]))

    print([x,y], mat[y][x])
    return [x,y]


#================================================================
#                       Funciones pantallas
#================================================================

ANCHO_VENTANA = 1000
ALTO_VENTANA = 1000

pygame.init()

ventana = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
pygame.display.set_caption("Tutorial")
ventana.fill((195, 247, 126)) #color de fondo

def main_nivel():
    
    #-------------------------------------------------
    matrix = [
    [0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,0,0],
    [0,0,2,2,2,2,2,2,0,0,0,1,1,1,1,1,1,1,0,0],
    [1,1,2,0,0,0,0,2,0,0,0,1,1,1,1,1,1,1,0,0],
    [1,1,2,2,2,2,2,2,2,2,2,2,1,1,1,1,1,1,0,0],
    [1,1,1,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,0,0],
    [0,0,0,0,0,0,0,1,1,1,0,1,1,1,1,1,1,2,2,0],
    [0,2,2,2,2,2,2,2,1,1,0,0,1,1,1,1,1,0,2,0],
    [0,2,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,2,0],
    [0,2,0,0,0,0,0,0,2,2,2,2,2,2,2,2,2,2,2,0],
    [0,2,0,0,0,0,0,0,2,0,2,0,0,2,0,0,0,0,0,0],
    [0,2,2,2,2,2,2,2,2,0,2,0,0,2,0,1,1,1,1,1],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,1,1,1,1,1],
    [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,2,1],
    [2,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0],
    [2,0,2,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,0],
    [2,0,1,1,1,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0],
    [2,0,1,1,1,0,0,1,2,0,2,2,2,0,1,1,1,1,1,0],
    [0,0,0,0,0,0,0,0,2,0,2,0,2,0,1,1,1,1,1,0],
    [0,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,1,1,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0]
    ]

    ancho_cuadrado = 50  
    alto_cuadrado = 50
    cantidad_obstaculos = 10
    cantidad_monedas = 30
    n_personajes = 4 #minimo 1 para que haya un player
    posiciones = []
    rol_infiltrado = []

    matrix_nueva = agrega_obstaculos(matrix, cantidad_obstaculos)
    matrix_nueva = agrega_monedas(matrix_nueva, cantidad_monedas)

    for i in range(n_personajes):
        posiciones.append(posicion_amigos(matrix_nueva, posiciones))
        rol_infiltrado.append(0)

    #Puede que no sea necesario guardarlo en una lista, pero por ahora lo voy a dejar asi por si sirve
    indice_infiltrado = random.randrange(0, n_personajes)
    rol_infiltrado[indice_infiltrado] = 1 

    #-------------------------------------------------

    pygame.display.flip()
    
    reloj = pygame.time.Clock()
    despliega_matriz(alto_cuadrado, ancho_cuadrado, matrix_nueva)
    corriendo = True
    print()
    while corriendo:
    
        #Coloca cpus en el mapa en negro
        for i in range(n_personajes):
            x=0
            x = posiciones[i][0] * ancho_cuadrado
            y = posiciones[i][1] * alto_cuadrado

            if (i == indice_infiltrado):
                crea_cuadrado(x, y, (200, 0, 0), alto_cuadrado, ancho_cuadrado) #rojo

            else:
                crea_cuadrado(x, y, (0, 0, 0), alto_cuadrado, ancho_cuadrado) #negro
            
        reloj.tick(5) #Fuerza a correr a 60 FPS 

        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                corriendo = False
                
        pygame.display.flip()
                
    sys.exit()

#--------------------------------------------------------------------------------------------------------------------
def pantallaInstrucciones():

    ventana.fill((100, 150, 80)) #color de fondo

    fuente = pygame.font.SysFont('unispacebold', 32)

    vidasTxt = fuente.render("Aqui van las instrucciones, presione espacio para volver al menu", True, (255,255,255))
    ventana.blit(vidasTxt,(100,100))

    pygame.display.flip()
    
    corriendo = True
    while corriendo:
        for event in pygame.event.get():
            
                if (event.type == pygame.QUIT):
                    corriendo = False
                
                #Controlar jugador1
                elif (event.type == pygame.KEYDOWN):
                    
                    if event.key == K_SPACE: #mueve hacia arriba
                        main_menu()  
                            
                            
                    elif event.key == K_ESCAPE: #mueve hacia arriba
                        corriendo = False    

    sys.exit()

#--------------------------------------------------------------------------------------------------------------------
def main_menu():

    ventana.fill((195, 150, 200)) #color de fondo
    
    fuente = pygame.font.SysFont('unispacebold', 32)

    vidasTxt = fuente.render("menu principal, presione espacio para empezar, i para instrucciones", True, (255,255,255))
    ventana.blit(vidasTxt,(100,100))

    pygame.display.flip()
    
    corriendo = True
    while corriendo:
        for event in pygame.event.get():
            
                if (event.type == pygame.QUIT):
                    corriendo = False
                
                #Controlar jugador1
                elif (event.type == pygame.KEYDOWN):
                    
                    if event.key == K_SPACE: 
                        reiniciar = True
                        while reiniciar:
                            main_nivel()  
                            
                    elif event.key == K_ESCAPE: 
                        corriendo = False    
                        
                    elif event.key == K_i:
                        pantallaInstrucciones()
    sys.exit()

main_menu()