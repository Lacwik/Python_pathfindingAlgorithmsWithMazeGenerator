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
statistics = Statistics()

end_x = rows-1
end_y = cols-1


# -------- Main Program Loop -----------
while not PROGRAM_END:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == K_SPACE:
            PAUSE = not PAUSE
        if event.type == pygame.KEYDOWN and event.key == K_s:
            SHOW_STATS = not SHOW_STATS
        if event.type == pygame.KEYDOWN and event.key == K_r:
            algorithm.reset(maze3)
            algorithm.reset(maze2)
            algorithm.reset(maze1)
        if event.type == pygame.QUIT:
            PROGRAM_END = True

    if(not PAUSE and algorithm.astar_stop == False): 
        #algorithm.astar(maze1.mainGrid[0][0],maze1.mainGrid[end_x][end_y], maze1)
        statistics.astar_iterate()

    if(not PAUSE and algorithm.djikstra_stop == False):
        algorithm.djikstra(maze1.mainGrid[0][0],maze1.mainGrid[end_x][end_y], maze1)
        statistics.djikstra_iterate()
        
            

    maze1.draw()
    maze2.draw()
    maze3.draw()


    #statistics window
    sub4.fill(LIGHT_BLUE)
    pygame.draw.line(sub4, GREY, (0,0),(0, int(windowHEIGHT/2)), 8)
    pygame.draw.line(sub4, GREY, (0,0),(int(windowWIDTH/2), 0), 8)



    mainWindow.blit(sub1, (0,0))
    mainWindow.blit(sub2, (int(windowWIDTH/2), 0))
    mainWindow.blit(sub3, (0, int(windowHEIGHT/2)))
    mainWindow.blit(sub4, (int(windowWIDTH/2), int(windowHEIGHT/2)))


    if(SHOW_STATS == True):
        statistics.display()

    pygame.display.flip()
    clock.tick(framerate)
pygame.quit()