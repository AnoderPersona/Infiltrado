import pygame
import sys
import os
import random


#================================================================
#                       Despliega matriz
#================================================================

def crea_cuadrado(x, y, color, alto_cuadrado, ancho_cuadrado):

    pygame.draw.rect(ventana, color, [x, y, ancho_cuadrado, alto_cuadrado ])

def despliega_matriz(alto_cuadrado, ancho_cuadrado, matrix):

    y = 0  # we start at the top of the screen
    for row in matrix:
        x = 0 # for every row we start at the left of the screen again
        for item in row:

            #pared
            if item == 0:
                crea_cuadrado(x, y, (255, 255, 255), alto_cuadrado, ancho_cuadrado)
            #pieza
            elif item == 1:
                crea_cuadrado(x, y, (200, 100, 60), alto_cuadrado, ancho_cuadrado)
            #pasillo
            elif item == 2:
                crea_cuadrado(x, y, (100, 200, 50), alto_cuadrado, ancho_cuadrado)
            #obstaculo
            else:
                crea_cuadrado(x, y, (200, 50, 100), alto_cuadrado, ancho_cuadrado)

            x += ancho_cuadrado # for ever item/number in that row we move one "step" to the right
        y += alto_cuadrado   # for every new row we move one "step" downwards
    pygame.display.update()

#================================================================
#                       Obstaculos
#================================================================

def agrega_obstaculos(mat, n):

    for i in range(n):

        x = random.randrange(0,len(mat))
        y = random.randrange(0,len(mat[0]))

        while (mat[x][y] < 1 or mat[x][y] == 2):
            x = random.randrange(0,len(mat))
            y = random.randrange(0,len(mat[0]))

        mat[x][y] = -1

    return mat

#================================================================
#                       Funcion principal
#================================================================

ANCHO_VENTANA = 1000
ALTO_VENTANA = 1000

pygame.init()

ventana = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
pygame.display.set_caption("Tutorial")
ventana.fill((195, 247, 126)) #color de fondo

def main():
    
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

    # we use the sizes to draw as well as to do our "steps" in the loops. 
    ancho_cuadrado = 50  
    alto_cuadrado = 50
    cantidad_obstaculos = 10

    matrix = agrega_obstaculos(matrix, cantidad_obstaculos)
    #-------------------------------------------------

    pygame.display.flip()
    
    reloj = pygame.time.Clock()
    despliega_matriz(alto_cuadrado, ancho_cuadrado, matrix)
    corriendo = True
    while corriendo:
    
        reloj.tick(60) #Fuerza a correr a 60 FPS 

        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                corriendo = False
                
        pygame.display.flip()
                
    sys.exit()

main()