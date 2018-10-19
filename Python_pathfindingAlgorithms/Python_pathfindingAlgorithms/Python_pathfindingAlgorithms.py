import random
import pygame
from utils.cell import cell
from utils.maze import maze
from utils.configuration import *

PROGRAM_END = False

pygame.init()
pygame.display.set_caption("Maciej Łacwik || maze generator + pathfinding")

maze1 = maze(mainWindow)
maze1.generate()
maze2 = maze(djikstra_window)
maze2.generate()

# -------- Main Program Loop -----------
while not PROGRAM_END:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            PROGRAM_END = True
    



    mainWindow.fill((20,20,20))
    djikstra_window.fill((20,20,20))

    maze1.draw()
    maze2.draw()

    maze1.mainGrid[5][5].color = LIGHT_GREEN





    pygame.display.flip()
    clock.tick(10)
pygame.quit()