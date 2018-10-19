import pygame
import random
from utils.configuration import cols, rows, cellWidth, WHITE, GREY, BLACK, PURPLE, RED

class cell(object):
    def __init__(self, x, y, grid, window):
        self.x = x*cellWidth
        self.y = y*cellWidth
        self.window = window
        self.grid = grid

        self.visited = False
        self.active = False
        self.cellWalls = [True,True,True,True]


        self.neighbors = []
        self.topNeighbor = 0
        self.bottomNeighbor = 0
        self.leftNeighbor = 0
        self.rightNeighbor = 0

        self.nextCell = 0

    def checkNeighbors(self):
        """solution based on Wilson's algorithm for generating a maze
            Returning self.nextCell next position in neighbors[] to check"""
        if(int(self.y / cellWidth) - 1 >= 0):
            self.topNeighbor = self.grid[int(self.y / cellWidth) - 1][int(self.x / cellWidth)]
        
        if(int(self.x / cellWidth) + 1 <= cols - 1):
            self.rightNeighbor = self.grid[int(self.y / cellWidth)][int(self.x / cellWidth) + 1]
        
        if(int(self.y / cellWidth) + 1 <= rows - 1):
            self.bottomNeighbor = self.grid[int(self.y / cellWidth) + 1][int(self.x / cellWidth)]
        
        if(int(self.x / cellWidth) - 1 >= 0):
            self.leftNeighbor = self.grid[int(self.y / cellWidth)][int(self.x / cellWidth) - 1]

        #adding to stack
        if self.topNeighbor != 0:
            if self.topNeighbor.visited == False:
                self.neighbors.append(self.topNeighbor)
        if self.rightNeighbor != 0:
            if self.rightNeighbor.visited == False:
                self.neighbors.append(self.rightNeighbor)
        if self.bottomNeighbor != 0:
            if self.bottomNeighbor.visited == False:
                self.neighbors.append(self.bottomNeighbor)
        if self.leftNeighbor != 0:
            if self.leftNeighbor.visited == False:
                self.neighbors.append(self.leftNeighbor)
        
        #randomly choosing next apex on stack
        if len(self.neighbors) > 0:
            self.nextCell = self.neighbors[random.randrange(0,len(self.neighbors))]
            return self.nextCell
        else:
            return False

    def draw(self):
        if(self.visited == True):
            pygame.draw.rect(self.window,WHITE,(self.x,self.y,cellWidth,cellWidth))
        elif(self.active == True):
            pygame.draw.rect(self.window,RED,(self.x,self.y,cellWidth,cellWidth))
        else:
            pygame.draw.rect(self.window,BLACK,(self.x,self.y,cellWidth,cellWidth))

        #WALLS
        if(self.cellWalls[0] == True):
            pygame.draw.line(self.window,BLACK,(self.x,self.y),((self.x + cellWidth),self.y),1)
        if(self.cellWalls[1] == True):
            pygame.draw.line(self.window,BLACK,((self.x + cellWidth),(self.y + cellWidth)),(self.x,(self.y + cellWidth)),1)
        if(self.cellWalls[2] == True):
            pygame.draw.line(self.window,BLACK,((self.x + cellWidth),(self.y + cellWidth)),((self.x + cellWidth),self.y),1) 
        if(self.cellWalls[3] == True):
            pygame.draw.line(self.window,BLACK,(self.x,self.y),(self.x,(self.y + cellWidth)),1) 

