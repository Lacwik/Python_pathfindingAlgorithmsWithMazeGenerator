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

stack=[]

pygame.display.set_caption("Maciej Łacwik || maze generator + pathfinding")

class Cell():
    
    def __init__(self, x, y):
        self.x = x*cellWidth
        self.y = y*cellWidth
        self.visited = False
        self.current = False
        self.cellWalls = [True,True,True,True]

        self.neighbors = []
        self.topNeighbor = 0
        self.bottomNeighbor = 0
        self.leftNeighbor = 0
        self.rightNeighbor = 0

        self.nextCell = 0

    def checkNeighbours(self):
        """Wilson's algorithm for generating a maze
            Returning self.nextCell next position in neighbors[] to check"""
        if((self.y / cellWidth) - 1 >= 0):
            self.topNeighbor = grid[(self.y / cellWidth) - 1][(self.x / cellWidth)]
        
        if((self.x / cellWidth) + 1 <= cols - 1):
            self.rightNeighbor = grid[(self.y / cellWidth)][(self.x / cellWidth) + 1]
        
        if((self.y / cellWidth) + 1 <= rows - 1):
            self.bottomNeighbor = grid[(self.y / cellWidth) + 1][(self.x / cellWidth)]
        
        if((self.x / cellWidth) - 1 >= 0):
            self.leftNeighbor = grid[(self.y / cellWidth)][(self.x / cellWidth) - 1]

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
        if(self.current==True):
            pygame.draw.rect(mainWindow,RED,(self.x,self.y,cellWidth,cellWidth))
        else:
            pygame.draw.rect(mainWindow,WHITE,(self.x,self.y,cellWidth,cellWidth))

        #WALLS
        if(self.cellWalls[0] == True):
            pygame.draw.line(mainWindow,BLACK,(self.x,self.y),((self.x + cellWidth),self.y),1)
        if(self.cellWalls[1] == True):
            pygame.draw.line(mainWindow,BLACK,((self.x + cellWidth),(self.y + cellWidth)),(self.x,(self.y + cellWidth)),1)
        if(self.cellWalls[2] == True):
            pygame.draw.line(mainWindow,BLACK,((self.x + cellWidth),(self.y + cellWidth)),((self.x + cellWidth),self.y),1) 
        if(self.cellWalls[3] == True):
            pygame.draw.line(mainWindow,BLACK,(self.x,self.y),(self.x,(self.y + cellWidth)),1) 


    def removeWalls(currentCell,nextCell):
        x = (currentCell.x / cellWidth) - (nextCell.x / cellWidth)
        y = (currentCell.y / cellWidth) - (nextCell.y / cellWidth)
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


#MAIN GRID generate + fill with cell objects
mainGrid = []
for y in range(rows):
    mainGrid.append([])
    for x in range(cols):
        mainGrid[y].append(Cell(x,y))

currentCell = mainGrid[0][0]
nextCell = 0


# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    mainWindow.fill(GREY)
    
    currentCell.visited = True
    currentCell.current = True
    
    for y in range(rows):
        for x in range(cols):
            mainGrid[y][x].draw()
    
    nextCell = currentCell.checkNeighbors()
    
    if nextCell != False:
        current_cell.neighbors = []
        
        stack.append(currentCell)
        
        removeWalls(currentCell,nextCell)
        
        currentCell.current = False
        
        currentCell = nextCell
    
    elif len(stack) > 0:
        currentCell.current = False
        currentCell = stack.pop()
        
    elif len(stack) == 0:
        grid = []
        
        for y in range(rows):
            grid.append([])
            for x in range(cols):
                grid[y].append(Cell(x,y))
        
        currentCell = grid[0][0]
        nextCell = 0
    
    pygame.display.flip()
    
    clock.tick(60)

pygame.quit()