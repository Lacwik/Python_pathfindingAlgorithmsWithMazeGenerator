import random
import pygame


WHITE = (255,255,255)
GREY = (20,20,20)
BLACK = (0,0,0)
PURPLE = (100,0,100)
RED = (255,0,0)

pygame.init()

mazeSize = (701,701)

mainWindow = pygame.display.set_mode(mazeSize)
clock = pygame.time.Clock()

cellWidth = 25
cols = mazeSize[0] / cellWidth
rows = mazeSize[1] / cellWidth


pygame.display.set_caption("Maciej Łacwik || maze generator + pathfinding")

class Cell():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.visited = False
        self.current = False
        self.cellWalls = [True,True,True,True]

        self.neighbours = []
        self.topNeighbour = 0
        self.bottomNeighbour = 0
        self.leftNeighbour = 0
        self.rightNeighbour = 0

        self.nextCell = 0

    def checkNeighbours(self):
        hddf = 0


    def draw(self):
        if(self.current==True):
            pygame.draw.rect(mainWindow,RED,(self.x,self.y,cellWidth,cellWidth))
        else:
            pygame.draw.rect(mainWindow,WHITE,(self.x,self.y,cellWidth,cellWidth))

        if(self.cellWalls[0] == True):
            pygame.draw.line(mainWindow,BLACK,(self.x,self.y),((self.x + cellWidth),self.y),1) #top cell wall
        if(self.cellWalls[1] == True):
            pygame.draw.line(mainWindow,BLACK,((self.x + cellWidth),(self.y + cellWidth)),(self.x,(self.y + cellWidth)),1) #bottom cell wall
        if(self.cellWalls[2] == True):
            pygame.draw.line(mainWindow,BLACK,((self.x + cellWidth),(self.y + cellWidth)),((self.x + cellWidth),self.y),1) #right cell wall
        if(self.cellWalls[3] == True):
            pygame.draw.line(mainWindow,BLACK,(self.x,self.y),(self.x,(self.y + cellWidth)),1) #left cell wall



#main grid generate + fill with cell object
mainGrid = []
for y in range(rows):
    mainGrid.append([])
    for x in range(cols):
        mainGrid[y].append(Cell(x,y))

currentCell = mainGrid[0][0]
nextCell = 0