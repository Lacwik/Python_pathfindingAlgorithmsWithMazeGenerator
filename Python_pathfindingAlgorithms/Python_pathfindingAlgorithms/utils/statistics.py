from utils.maze import *
from utils.configuration import *

x = int(windowWIDTH/2)
y = int(windowHEIGHT/2)

class Statistics:
    def __init__(self):
        self.astar_counter = 0
        self.djikstra_counter = 0
        self.bf_counter = 0

    def astar_iterate(self):
        self.astar_counter = self.astar_counter + 1

    def djikstra_iterate(self):
        self.djikstra_counter = self.astar_counter + 1

    def bf_iterate(self):
        self.bf_counter = self.bf_counter + 1

    def display(self):
       myfont = pygame.font.SysFont(None, 30)
       label_captions = myfont.render("                 A*    Dijkstra   Bellman-Ford", 1, (0,0,0))
       label_iterations = myfont.render("Iterations:     " + str(self.astar_counter) + "        " + str(self.djikstra_counter) + "          " + str(self.bf_counter), 1, (0,0,0))
       mainWindow.blit(label_iterations, (x+10, y+30))
       mainWindow.blit(label_captions, (x+30, y+10))

