from utils.cell import cell
from utils.maze import maze
from utils.statistics import *
from utils.configuration import *
from utils.algorithms import *

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

Algorithms.astar(maze1.mainGrid[2][2],maze1.mainGrid[5][6], maze1)


# -------- Main Program Loop -----------
while not PROGRAM_END:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            PROGRAM_END = True
    
    maze1.draw()
    maze2.draw()
    maze3.draw()

    maze2.mainGrid[8][8].color = LIGHT_GREEN
    maze3.mainGrid[3][6].color = LIGHT_GREEN
    maze1.mainGrid[1][1].color = LIGHT_GREEN

    #statistics window
    sub4.fill(LIGHT_BLUE)
    pygame.draw.line(sub4, GREY, (0,0),(0, int(windowHEIGHT/2)), 8)
    pygame.draw.line(sub4, GREY, (0,0),(int(windowWIDTH/2), 0), 8)



    mainWindow.blit(sub1, (0,0))
    mainWindow.blit(sub2, (int(windowWIDTH/2), 0))
    mainWindow.blit(sub3, (0, int(windowHEIGHT/2)))
    mainWindow.blit(sub4, (int(windowWIDTH/2), int(windowHEIGHT/2)))

    Statistics.texts()

    pygame.display.flip()
    clock.tick(10)
pygame.quit()