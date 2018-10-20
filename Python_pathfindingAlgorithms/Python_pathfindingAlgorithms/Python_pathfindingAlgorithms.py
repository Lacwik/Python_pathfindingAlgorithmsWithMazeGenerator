import random
import pygame
from utils.cell import cell
from utils.maze import maze
from utils.configuration import *

PROGRAM_END = False

pygame.init()
pygame.display.set_caption("Maciej Łacwik || maze generator + pathfinding")


sub1 = mainSurface.subsurface(p1_camera)
sub2 = mainSurface.subsurface(p2_camera)
sub3 = mainSurface.subsurface(p3_camera)
sub4 = mainSurface.subsurface(p4_camera)
maze1 = maze(sub1)
maze1.generate()
maze2 = maze(sub2)
maze2.generate()
maze3 = maze(sub3)
maze3.generate()
maze4 = maze(sub4)
maze4.generate()


# -------- Main Program Loop -----------
while not PROGRAM_END:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            PROGRAM_END = True
    



    mainWindow.fill(BLACK)

    maze1.draw()
    maze1.mainGrid[5][5].color = LIGHT_GREEN
    maze2.draw()
    maze2.mainGrid[5][5].color = LIGHT_GREEN
    maze3.draw()
    maze3.mainGrid[5][5].color = LIGHT_GREEN
    maze4.draw()
    maze4.mainGrid[5][5].color = LIGHT_GREEN



    mainWindow.blit(sub1, (0,0))
    mainWindow.blit(sub2, (int(windowWIDTH/2), 0))
    mainWindow.blit(sub3, (0, int(windowHEIGHT/2)))
    mainWindow.blit(sub4, (int(windowWIDTH/2), int(windowHEIGHT/2)))

    # Update the screen
    pygame.display.update()



    pygame.display.flip()
    clock.tick(10)
pygame.quit()