from utils.maze import *
from utils.configuration import *

x = int(windowWIDTH/2)
y = int(windowHEIGHT/2)

class Statistics:
    @staticmethod
    def texts():
       myfont = pygame.font.SysFont(None, 30)
       label = myfont.render("Some text!", 1, (0,0,0))
       mainWindow.blit(label, (x+10, y+10))