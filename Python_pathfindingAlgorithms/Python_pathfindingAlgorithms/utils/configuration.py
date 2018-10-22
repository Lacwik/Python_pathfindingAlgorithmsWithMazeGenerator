import pygame, random

WHITE = (255,255,255)
GREY = (20,20,20)
BLACK = (0,0,0)
PURPLE = (100,0,100)
RED = (255,0,0)
LIGHT_GREEN = (60,247,37)
LIGHT_BLUE = (37,198,247)

windowWIDTH = 800
windowHEIGHT = 600
cellWidth = 25
mazeSeed = 9001 #0 for separate seed for each maze

ASTAR = True
SHOW_STATS = False
PAUSE = False

mazeSize = (int(windowWIDTH/2),int(windowHEIGHT/2))
cols = int(mazeSize[0] / cellWidth)
rows = int(mazeSize[1] / cellWidth)

mainSurface = pygame.Surface((windowWIDTH, windowHEIGHT))
p1_camera = pygame.Rect(0,0,int(windowWIDTH/2),int(windowHEIGHT/2))
p2_camera = pygame.Rect(int(windowWIDTH/2),0,int(windowWIDTH/2),int(windowHEIGHT/2))
p3_camera = pygame.Rect(0,int(windowHEIGHT/2),int(windowWIDTH/2),int(windowHEIGHT/2))
p4_camera = pygame.Rect(int(windowWIDTH/2),int(windowHEIGHT/2),int(windowWIDTH/2),int(windowHEIGHT/2))

mainWindow = pygame.display.set_mode((windowWIDTH,windowHEIGHT), pygame.RESIZABLE)
clock = pygame.time.Clock()