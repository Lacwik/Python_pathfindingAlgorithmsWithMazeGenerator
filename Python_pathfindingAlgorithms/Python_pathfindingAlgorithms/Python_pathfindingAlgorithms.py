import random
import pygame
from utils.cell import cell
from utils.maze import maze
from utils.configuration import *

PROGRAM_END = False

pygame.init()
pygame.display.set_caption("Maciej Łacwik || maze generator + pathfinding")


# -------- Main Program Loop -----------
while not PROGRAM_END:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            PROGRAM_END = True
    
    mainWindow.fill((20,20,20))
    
    maze1 = maze.generate()
    
    pygame.display.flip()
    
    clock.tick(10)

pygame.quit()