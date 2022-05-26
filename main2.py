from turtle import pos
import pygame
import sys
import os
import random
from pygame.locals import *


# ================================================================
#                       Despliega matriz
# ================================================================

def crea_cuadrado(x: int, y: int, color: tuple, ALTO_CUADRADO: int, ANCHO_CUADRADO: int):

    pygame.draw.rect(ventana, color, [x, y, ANCHO_CUADRADO, ALTO_CUADRADO])


def despliega_matriz(ALTO_CUADRADO: int, ANCHO_CUADRADO: int, matrix: list):

    y = 0  # we start at the top of the screen
    for row in matrix:
        x = 0  # for every row we start at the left of the screen again
        for item in row:

            # pared
            if item == 0:
                crea_cuadrado(x, y, (255, 255, 255),
                              ALTO_CUADRADO, ANCHO_CUADRADO)  # blanco
            # pieza
            elif item == 1:
                crea_cuadrado(x, y, (200, 100, 60), ALTO_CUADRADO,
                              ANCHO_CUADRADO)  # naranjo
            # pasillo o ex-moneda
            elif item == 2:
                crea_cuadrado(x, y, (100, 200, 50), ALTO_CUADRADO,
                              ANCHO_CUADRADO)  # verde
            # obstaculo
            elif item == -1:
                crea_cuadrado(x, y, (200, 50, 100), ALTO_CUADRADO,
                              ANCHO_CUADRADO)  # rosado oscuro
            # moneda
            elif item == -2:
                crea_cuadrado(x, y, (200, 200, 20), ALTO_CUADRADO,
                              ANCHO_CUADRADO)  # verde amarillo

            x += ANCHO_CUADRADO  # for ever item/number in that row we move one "step" to the right
        y += ALTO_CUADRADO   # for every new row we move one "step" downwards
    # pygame.display.update()

# ================================================================
#                       Generacion random
# ================================================================


def agrega_obstaculos(mat: list, n: int):

    for i in range(n):

        x = random.randrange(0, len(mat))
        y = random.randrange(0, len(mat[0]))

        while (mat[y][x] != 1):
            x = random.randrange(0, len(mat))
            y = random.randrange(0, len(mat[0]))

        mat[y][x] = -1

    return mat


def agrega_monedas(mat: list, n: int):

    for i in range(n):

        x = random.randrange(0, len(mat))
        y = random.randrange(0, len(mat[0]))

        while (mat[y][x] < 1):
            x = random.randrange(0, len(mat))
            y = random.randrange(0, len(mat[0]))

        mat[y][x] = -2

    return mat


def posicion_amigos(mat: list, pos: list):

    x = random.randrange(0, len(mat))
    y = random.randrange(0, len(mat[0]))

    while (mat[y][x] < 1 or [y, x] in pos):
        x = random.randrange(0, len(mat))
        y = random.randrange(0, len(mat[0]))

    print([x, y], mat[y][x])
    return [x, y]

def movimiento_cpu(matrix: list, posiciones: list, n: int):

        movio = False

        while (not movio):

            direccion = random.randint(0, 7)

            #arriba
            if direccion == 0:
                #print([posiciones[0][0]][posiciones[0][1]-1], matrix[posiciones[0][0]][posiciones[0][1]-1])
                if posiciones[n][1] - 1 >= 0 and matrix[posiciones[n][1]-1][posiciones[n][0]] not in [0, -1]:
                    posiciones[n][1] -= 1
                    movio = True

            elif direccion == 1:
                #print(matrix[posiciones[n][0]-1][posiciones[n][1]])
                if posiciones[n][0] - 1 >= 0 and matrix[posiciones[n][1]][posiciones[n][0]-1] not in [0, -1]:
                    posiciones[n][0] -= 1
                    movio = True

            elif direccion == 2:
                #print(matrix[posiciones[n][0]][posiciones[n][1]+1])
                if posiciones[n][1] + 1 < 20 and matrix[posiciones[n][1]+1][posiciones[n][0]] not in [0, -1]:
                    posiciones[n][1] += 1
                    movio = True

            elif direccion == 3:

                if posiciones[n][0] + 1 < 20 and matrix[posiciones[n][1]][posiciones[n][0]+1] not in [0, -1]:
                    posiciones[n][0] += 1
                    movio = True
            #quieto
            if (direccion >= 4): movio = True
        
        return posiciones

# ================================================================
#                       Funciones pantallas
# ================================================================

ANCHO_VENTANA = 700
ALTO_VENTANA = 700
ANCHO_CUADRADO = 35
ALTO_CUADRADO = 35

pygame.init()

ventana = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
pygame.display.set_caption("Tutorial")
ventana.fill((195, 247, 126))  # color de fondo
pygame.key.set_repeat(500, 50) #Para permitir la repeticion de teclas, primer parametro es cuanto se demora en milisegundos la primera, y el segundo el resto

def main_nivel():

    # -------------------------------------------------

    matrix_const = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0],
        [0, 0, 2, 2, 2, 2, 2, 2, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0],
        [1, 1, 2, 0, 0, 0, 0, 2, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0],
        [1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 0, 0],
        [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 2, 2, 0],
        [0, 2, 2, 2, 2, 2, 2, 2, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 2, 0],
        [0, 2, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0],
        [0, 2, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0],
        [0, 2, 0, 0, 0, 0, 0, 0, 2, 0, 2, 0, 0, 2, 0, 0, 0, 0, 0, 0],
        [0, 2, 2, 2, 2, 2, 2, 2, 2, 0, 2, 0, 0, 2, 0, 1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 1, 1, 1, 1, 1],
        [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 2, 1],
        [2, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0],
        [2, 0, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0],
        [2, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [2, 0, 1, 1, 1, 0, 0, 1, 2, 0, 2, 2, 2, 0, 1, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 2, 0, 2, 0, 1, 1, 1, 1, 1, 0],
        [0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0]
    ]

    matrix = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0],
        [0, 0, 2, 2, 2, 2, 2, 2, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0],
        [1, 1, 2, 0, 0, 0, 0, 2, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0],
        [1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 0, 0],
        [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 2, 2, 0],
        [0, 2, 2, 2, 2, 2, 2, 2, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 2, 0],
        [0, 2, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0],
        [0, 2, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0],
        [0, 2, 0, 0, 0, 0, 0, 0, 2, 0, 2, 0, 0, 2, 0, 0, 0, 0, 0, 0],
        [0, 2, 2, 2, 2, 2, 2, 2, 2, 0, 2, 0, 0, 2, 0, 1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 1, 1, 1, 1, 1],
        [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 2, 1],
        [2, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0],
        [2, 0, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0],
        [2, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [2, 0, 1, 1, 1, 0, 0, 1, 2, 0, 2, 2, 2, 0, 1, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 2, 0, 2, 0, 1, 1, 1, 1, 1, 0],
        [0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0]
    ]

    cantidad_obstaculos = 10
    cantidad_monedas = 30
    monedas_obtenidas = 0
    n_personajes = 4  # minimo 1 para que haya un player
    posiciones = []
    rol_infiltrado = []
    muertos = []
    rip = False

    matrix_nueva = agrega_obstaculos(matrix, cantidad_obstaculos)
    matrix_nueva = agrega_monedas(matrix_nueva, cantidad_monedas)

    for i in matrix_nueva:
        print(i)

    for i in range(n_personajes):
        posiciones.append(posicion_amigos(matrix_nueva, posiciones))
        rol_infiltrado.append(0)
        muertos.append(0)

    # Puede que no sea necesario guardarlo en una lista, pero por ahora lo voy a dejar asi por si sirve
    indice_infiltrado = random.randrange(0, n_personajes)
    rol_infiltrado[indice_infiltrado] = 1

    # -------------------------------------------------

    pygame.display.flip()

    reloj = pygame.time.Clock()
    despliega_matriz(ALTO_CUADRADO, ANCHO_CUADRADO, matrix_nueva)
    corriendo = True
    print(posiciones)
    while corriendo:
        despliega_matriz(ALTO_CUADRADO, ANCHO_CUADRADO, matrix_nueva)

        # Coloca cpus en el mapa en negro
        for i in range(n_personajes):
            
            if (not muertos[i]):
            
                x = 0
                x = posiciones[i][0] * ANCHO_CUADRADO
                y = posiciones[i][1] * ALTO_CUADRADO

                if (i == indice_infiltrado):
                    crea_cuadrado(x, y, (200, 0, 0), ALTO_CUADRADO,
                                ANCHO_CUADRADO)  # rojo

                else:
                    crea_cuadrado(x, y, (0, 0, 0), ALTO_CUADRADO,
                                ANCHO_CUADRADO)  # negro

        reloj.tick(15)  # Fuerza a correr a 60 FPS

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                corriendo = False

            #Movimiento player
            elif (event.type == pygame.KEYDOWN):

                if event.key == K_w:
                    #print([posiciones[0][0]][posiciones[0][1]-1], matrix[posiciones[0][0]][posiciones[0][1]-1])
                    if posiciones[0][1] - 1 >= 0 and matrix[posiciones[0][1]-1][posiciones[0][0]] not in [0, -1]:
                        
                        posiciones[0][1] -= 1
                elif event.key == K_a:
                    #print(matrix[posiciones[0][0]-1][posiciones[0][1]])
                    if posiciones[0][0] - 1 >= 0 and matrix[posiciones[0][1]][posiciones[0][0]-1] not in [0, -1]:
                        posiciones[0][0] -= 1
                elif event.key == K_s:
                    #print(matrix[posiciones[0][0]][posiciones[0][1]+1])
                    if posiciones[0][1] + 1 < 20 and matrix[posiciones[0][1]+1][posiciones[0][0]] not in [0, -1]:
                        posiciones[0][1] += 1
                elif event.key == K_d:

                    if posiciones[0][0] + 1 < 20 and matrix[posiciones[0][1]][posiciones[0][0]+1] not in [0, -1]:
                        posiciones[0][0] += 1

                elif event.key == K_r:

                    if (rip):
                        return False, False
                    else:
                        return True, False

                    

        #matar
        if (posiciones.count(posiciones[indice_infiltrado]) > 1):

            print("matarr")
            f = posiciones.index(posiciones[indice_infiltrado])

            if (f == indice_infiltrado):
                f = posiciones.index(posiciones[indice_infiltrado],indice_infiltrado+1)

            muertos[f] = 1
            print(f"se murio muertos[{f}]")

        #movimiento cpu
        for i in range(n_personajes-1):

            if (not muertos[i+1]):
                posiciones = movimiento_cpu(matrix, posiciones, i+1)

        # posiciones = movimiento_cpu(matrix, posiciones, 2)
        # posiciones = movimiento_cpu(matrix, posiciones, 3)


        #chequear monedas
        for pos in posiciones:

            if (matrix[pos[1]][pos[0]] == -2):

                monedas_obtenidas += 1
                matrix[pos[1]][pos[0]] = matrix_const[pos[1]][pos[0]]
                print(monedas_obtenidas)

        if (monedas_obtenidas >= cantidad_monedas):
            
            if (indice_infiltrado != 0): 
                print("Felicidades, no quedan monedas")
                return False, True

            else: 
                print("Que mal, obtuvieron todas las monedas")
                return False, False

        #Chequear muertes
        if (muertos.count(1) >= n_personajes-1):
            
            if (indice_infiltrado != 0): 
                print("Que pena, murieron todos")
                return False, True

            else: 
                print("Felicidades, lograste matarlos a todos!")
                return False,True
        
        if (muertos[0] == 1):

            fuente = pygame.font.SysFont('unispacebold', 20)

            rip = True

            texto = fuente.render(
                "Que pena, te moriste, puedes ver como terminan tus amigos o reiniciar con r", True, (0, 0, 0))
            ventana.blit(texto, (100, 100))

        pygame.display.flip()
        pygame.display.update()

    sys.exit()

# --------------------------------------------------------------------------------------------------------------------


def pantallaInstrucciones():

    ventana.fill((100, 150, 80))  # color de fondo

    fuente = pygame.font.SysFont('unispacebold', 32)

    vidasTxt = fuente.render(
        "Aqui van las instrucciones, presione espacio para volver al menu", True, (255, 255, 255))
    ventana.blit(vidasTxt, (100, 100))

    pygame.display.flip()

    corriendo = True
    while corriendo:
        for event in pygame.event.get():

            if (event.type == pygame.QUIT):
                corriendo = False

            # Controlar jugador1
            elif (event.type == pygame.KEYDOWN):

                if event.key == K_SPACE:  
                    main_menu()

                elif event.key == K_ESCAPE:  
                    corriendo = False

    sys.exit()

# --------------------------------------------------------------------------------------------------------------------

def final(ganador):
    
    fuente = pygame.font.SysFont('unispacebold', 32)

    if ganador:
    #Imprime pantalla victoria
        ventana.fill((100, 150, 80))  # color de fondo
        texto = fuente.render(
        "ganaste, presione espacio para volver al menu", True, (255, 255, 255))

        ventana.blit(texto, (100,100))
        
    else:
    #imprime pantalla derrota
        ventana.fill((200, 100, 80))  # color de fondo
        texto = fuente.render(
        "perdiste, presione espacio para volver al menu", True, (255, 255, 255))

        ventana.blit(texto, (100,100))
    
    pygame.display.flip()
    corriendo = True
    
    while corriendo:
        for event in pygame.event.get():
            
                if (event.type == pygame.QUIT):
                    corriendo = False
                
                #Controlar jugador1
                elif (event.type == pygame.KEYDOWN):
                    
                    if event.key == K_r or event.key == K_SPACE: 
                        main_menu()
                            
                            
                    elif event.key == K_ESCAPE: 
                        corriendo = False   
    sys.exit(0)

# --------------------------------------------------------------------------------------------------------------------

def main_menu():

    ventana.fill((195, 150, 200))  # color de fondo

    fuente = pygame.font.SysFont('unispacebold', 32)

    vidasTxt = fuente.render(
        "menu principal, presione espacio para empezar, i para instrucciones", True, (255, 255, 255))
    ventana.blit(vidasTxt, (100, 100))

    pygame.display.flip()

    corriendo = True
    while corriendo:
        for event in pygame.event.get():

            if (event.type == pygame.QUIT):
                corriendo = False

            # Controlar jugador1
            elif (event.type == pygame.KEYDOWN):

                if event.key == K_SPACE:
                    reiniciar = True
                    while reiniciar:
                        reiniciar, ganador = main_nivel()
                    final(ganador)

                elif event.key == K_ESCAPE:
                    corriendo = False

                elif event.key == K_i:
                    pantallaInstrucciones()

    sys.exit()


main_menu()
