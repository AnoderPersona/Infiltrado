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

def agrega_obstaculos(mat, n):

    for i in range(n):

        x = random.randrange(0,len(mat))
        y = random.randrange(0,len(mat[0]))

        while (mat[x][y] != 1):
            x = random.randrange(0,len(mat))
            y = random.randrange(0,len(mat[0]))

        mat[x][y] = -1

    return mat

def agrega_monedas(mat, n):

    for i in range(n):

        x = random.randrange(0,len(mat))
        y = random.randrange(0,len(mat[0]))

        while (mat[x][y] < 1):
            x = random.randrange(0,len(mat))
            y = random.randrange(0,len(mat[0]))

        mat[x][y] = -2

    return mat

def posicion_amigos(mat):

    x = random.randrange(0,len(mat))
    y = random.randrange(0,len(mat[0]))

    while (mat[x][y] < 1):
        x = random.randrange(0,len(mat))
        y = random.randrange(0,len(mat[0]))

    print([x,y], mat[x][y])
    return [x,y]


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

    ancho_cuadrado = 50  
    alto_cuadrado = 50
    cantidad_obstaculos = 10
    cantidad_monedas = 30
    n_cpus = 3
    posicion_cpu = []

    matrix = agrega_obstaculos(matrix, cantidad_obstaculos)
    matrix = agrega_monedas(matrix, cantidad_monedas)
    for i in range(n_cpus):
        posicion_cpu.append(posicion_amigos(matrix))
    #-------------------------------------------------

    pygame.display.flip()
    
    reloj = pygame.time.Clock()
    despliega_matriz(alto_cuadrado, ancho_cuadrado, matrix)
    corriendo = True
    print()
    while corriendo:
    
        #Coloca cpus en el mapa en negro
        #NO FUNCIONA POR ALGUNA RAZON?
        for i in range(n_cpus):
            
            x = posicion_cpu[i][0] * ancho_cuadrado
            y = posicion_cpu[i][1] * alto_cuadrado
            crea_cuadrado(x, y, (0, 0, 0), alto_cuadrado, ancho_cuadrado) #negro
            
        reloj.tick(60) #Fuerza a correr a 60 FPS 

        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                corriendo = False
                
        pygame.display.flip()
                
    sys.exit()

main()