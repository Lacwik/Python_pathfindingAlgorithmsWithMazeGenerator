import pygame
from utils.cell import cell
from utils.configuration import *



class maze(object):
    def __init__():
        mainGrid = []
        stack=[]
        for y in range(rows):
             mainGrid.append([])
        for x in range(cols):
             mainGrid[y].append(cell(x,y, mainGrid, mainWindow))
        currentCell = mainGrid[0][0]
        nextCell = 0

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

    def generate():
        currentCell.visited = True
        currentCell.active = True
    
        for y in range(rows):
            for x in range(cols):
                mainGrid[y][x].draw()
    
        nextCell = currentCell.checkNeighbors()
    
        if nextCell != False:
            currentCell.neighbors = []
        
            stack.append(currentCell)
        
            removeWalls(currentCell,nextCell)
        
            currentCell.active = False
        
            currentCell = nextCell
    
        elif len(stack) > 0:
            currentCell.active = False
            currentCell = stack.pop()
        
        elif len(stack) == 0:
            grid = []
        
            for y in range(rows):
                grid.append([])
                for x in range(cols):
                    grid[y].append(Cell(x,y))
        
            currentCell = grid[0][0]
            nextCell = 0