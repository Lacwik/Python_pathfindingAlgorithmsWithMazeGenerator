import pygame
from utils.cell import cell
from utils.configuration import *

def removeWalls(currentCell,nextCell):
        x = int(currentCell.x / cellWidth) - int(nextCell.x / cellWidth)
        y = int(currentCell.y / cellWidth) - int(nextCell.y / cellWidth)
        if(x == -1): # right of current
            currentCell.cellWalls[1] = False
            nextCell.cellWalls[3] = False
        elif(x == 1): # left of current
            currentCell.cellWalls[3] = False
            nextCell.cellWalls[1] = False
        elif(y == -1): # bottom of current
            currentCell.cellWalls[2] = False
            nextCell.cellWalls[0] = False
        elif(y == 1): # top of current
            currentCell.cellWalls[0] = False
            nextCell.cellWalls[2] = False

class maze(object):
    def __init__(self, surface):
        self.mainGrid = []
        self.stack=[]
        self.surface = surface
        for y in range(rows):
             self.mainGrid.append([])
             for x in range(cols):
                  self.mainGrid[y].append(cell(x,y, self.mainGrid, WHITE, self.surface))
        self.currentCell = self.mainGrid[0][0]
        self.nextCell = 0
        self.stopGenerating = False

    def generate(self):
        while not self.stopGenerating:
            self.currentCell.visited = True
            self.currentCell.active = True
    
            self.nextCell = self.currentCell.checkNeighbors()
    
            if self.nextCell != False:
                self.currentCell.neighbors = []
        
                self.stack.append(self.currentCell)
        
                removeWalls(self.currentCell,self.nextCell)
        
                self.currentCell.active = False
        
                self.currentCell = self.nextCell
    
            elif len(self.stack) > 0:
                self.currentCell.active = False
                self.currentCell = self.stack.pop()
        
            elif len(self.stack) == 0:
                grid = []
                try:
                    for y in range(rows):
                        grid.append([])
                        for x in range(cols):
                            grid[y].append(Cell(x,y))
                except:
                    self.stopGenerating = True
                    return
                self.currentCell = grid[0][0]
                self.nextCell = 0

    def draw(self):
        for y in range(rows):
            for x in range(cols):
                self.mainGrid[y][x].draw()