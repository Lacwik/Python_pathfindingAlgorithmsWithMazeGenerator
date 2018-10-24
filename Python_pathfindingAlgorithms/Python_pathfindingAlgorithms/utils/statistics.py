from utils.maze import *
from utils.configuration import *

x = int(windowWIDTH/2)
y = int(windowHEIGHT/2)

class Statistics:
    def __init__(self):
        self.astar_counter = 0
        self.djikstra_counter = 0

    def astar_iterate(self):
        self.astar_counter = self.astar_counter + 1

    def display(self):
       myfont = pygame.font.SysFont(None, 30)
       label = myfont.render("Iterations: " + str(self.astar_counter), 1, (0,0,0))
       mainWindow.blit(label, (x+10, y+10))

