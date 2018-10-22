from utils.maze import *
from utils.configuration import *

x = int(windowWIDTH/2)
y = int(windowHEIGHT/2)

class Statistics:
    @staticmethod
    def texts():
       myfont = pygame.font.SysFont(None, 30)
       label = myfont.render("Iterations:", 1, (0,0,0))
       mainWindow.blit(label, (x+10, y+10))


    @staticmethod
    def statictics_display(iteration_counner):
       myfont = pygame.font.SysFont(None, 30)
       label = myfont.render(str(iteration_counner), 1, (0,0,0))
       mainWindow.blit(label, (x+150, y+10))

