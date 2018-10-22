import math
import sys
from utils.maze import *
from utils.cell import cell
from utils.configuration import *


G_cost = {}
F_cost = {}
came_from = {}
closedset = set()
openset = set()

class Algorithms:
    @staticmethod
    def count(collection):
        counter = 0
        for i in collection:
            counter = counter + 1
        return counter

    @staticmethod
    def getNeighbours(cell):
        neighbours = set()

        if cell.cellWalls[0] != True:
            neighbours.add(cell.topNeighbor)
        if cell.cellWalls[1] != True:
            neighbours.add(cell.bottomNeighbor)
        if cell.cellWalls[2] != True:
            neighbours.add(cell.rightNeighbor)
        if cell.cellWalls[3] != True:
            neighbours.add(cell.leftNeighbor)
        
        return neighbours

    @staticmethod
    def heuresticCost(start, end):
        x = start.x - end.x
        y = start.y - end.y
        return 1 * max(abs(x),abs(y))

    @staticmethod
    def astar(start, end, maze):
        startPoint = start
        endPoint = end

        G_cost[startPoint] = 0
        F_cost[startPoint] = G_cost[startPoint] + heuresticCost(startPoint, endPoint)
        openset.add(startPoint)

        while(count(openset)>0):
            F_cost_sorted = sorted(F_cost, key=lambda cell: G_cost[cell] + heuresticCost(cell, endPoint))
            i = 0
            for i in range(len(F_cost_sorted)-1):
                if(F_cost_sorted[i] not in closedset):
                    break

            current = F_cost_sorted[i]

            if(current == endPoint):
                print("EEEEEELLLLOOOOOO")

            try:
                openset.remove(current)
            except KeyError:
                pass

            closedset.add(current)
            for neighbour in getNeighbours(current):
                if neighbour not in closedset:
          
                    G_cost_tmp = G_cost[current] + 1
                    if (neighbour not in openset) or (G_cost_tmp < G_cost[neighbour]): 
                        came_from[neighbour] = current
                        G_cost[neighbour] = G_cost_tmp
                        F_cost[neighbour] = G_cost[neighbour] + heuresticCost(neighbour,endPoint)
            
                        if neighbour not in self.openset:
                            self.openset.add(neighbour)


        




       
