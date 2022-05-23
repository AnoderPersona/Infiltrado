import pygame
import sys

ANCHO_VENTANA = 500
ALTO_VENTANA = 500

gridDisplay = pygame.display.set_mode((200, 200))
pygame.display.get_surface().fill((200, 200, 200))  # background

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
grid_node_width = 10  
grid_node_height = 10

def createSquare(x, y, color):
    pygame.draw.rect(gridDisplay, color, [x, y, grid_node_width, grid_node_height ])



def visualizeGrid():
    y = 0  # we start at the top of the screen
    for row in matrix:
        x = 0 # for every row we start at the left of the screen again
        for item in row:
            if item == 0:
                createSquare(x, y, (255, 255, 255))
            elif item == 1:
                createSquare(x, y, (200, 100, 60))
            else:
                createSquare(x, y, (100, 200, 50))

            x += grid_node_width # for ever item/number in that row we move one "step" to the right
        y += grid_node_height   # for every new row we move one "step" downwards
    pygame.display.update()


  # call the function    
# while True:
#     pass  # keeps the window open so you can see the result.

def main():
    
    pygame.init()
    
    ventana = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
    pygame.display.set_caption("Tutorial")
    ventana.fill((195, 247, 126)) #(255,255,255)
    
    pygame.display.flip()
    
    reloj = pygame.time.Clock()
    visualizeGrid()
    corriendo = True
    while corriendo:
    
        reloj.tick(60) #Fuerza a correr a 60 FPS 

        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                corriendo = False
                
        
        pygame.display.flip()
                
    sys.exit()

main()