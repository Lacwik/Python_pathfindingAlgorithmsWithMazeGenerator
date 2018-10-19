import pygame

WHITE = (255,255,255)
GREY = (20,20,20)
BLACK = (0,0,0)
PURPLE = (100,0,100)
RED = (255,0,0)

cellWidth = 25
mazeSize = (701,701)
cols = int(mazeSize[0] / cellWidth)
rows = int(mazeSize[1] / cellWidth)

mainWindow = pygame.display.set_mode(mazeSize)
clock = pygame.time.Clock()