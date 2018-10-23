from utils.cell import cell
from utils.maze import maze
from utils.statistics import *
from utils.configuration import *
from utils.algorithms import *
from pygame.locals import *

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

algorithm = Algorithms()

iteration_counter = 0
end_x = cols-1
end_y = rows-1


# -------- Main Program Loop -----------
while not PROGRAM_END:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == K_SPACE:
            PAUSE = not PAUSE
        if event.type == pygame.KEYDOWN and event.key == K_s:
            SHOW_STATS = not SHOW_STATS
        if event.type == pygame.QUIT:
            PROGRAM_END = True

    if(not PAUSE and algorithm.astar_stop == False): 
        algorithm.astar(maze1.mainGrid[0][0],maze1.mainGrid[end_y][end_x], maze1)
        iteration_counter = iteration_counter + 1
            

    maze1.draw()
    maze2.draw()
    maze3.draw()

    maze1.mainGrid[end_y][end_x].color = PURPLE
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
    if(SHOW_STATS == True):
        Statistics.statictics_display(iteration_counter)

    pygame.display.flip()
    clock.tick(10)
pygame.quit()