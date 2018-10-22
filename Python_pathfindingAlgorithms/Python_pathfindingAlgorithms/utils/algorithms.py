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
        x = int(start.x/cellWidth) - int(end.x/cellWidth)
        y = int(start.y/cellWidth) - int(end.y/cellWidth)
        return 1 * max(abs(x),abs(y))

    @staticmethod
    def reconstruct_path(from_cell):
        try: 
            came_from[from_cell]
            p = Algorithms.reconstruct_path(came_from[from_cell])
            return_path = []
            return_path.extend(p)
            return_path.append(from_cell)
            return return_path
        except KeyError:
            return [from_cell]

    @staticmethod
    def astar(start, end, maze):
        startPoint = start
        endPoint = end

        G_cost[startPoint] = 0
        F_cost[startPoint] = G_cost[startPoint] + Algorithms.heuresticCost(startPoint, endPoint)
        openset.add(startPoint)

        while(Algorithms.count(openset)>0):
            F_cost_sorted = sorted(F_cost, key=lambda cell: G_cost[cell] + Algorithms.heuresticCost(cell, endPoint))
            i = 0
            for i in range(len(F_cost_sorted)-1):
                i = i+1
                if(F_cost_sorted[i] not in closedset):
                    break

            current = F_cost_sorted[i]

            if(current == endPoint):
                for cell in Algorithms.reconstruct_path(endPoint):
                    maze.mainGrid[int(cell.x/cellWidth)][int(cell.y/cellWidth)].color = LIGHT_BLUE
                return

            try:
                openset.remove(current)
            except KeyError:
                pass

            closedset.add(current)
            for neighbour in Algorithms.getNeighbours(current):
                if neighbour not in closedset:
                    G_cost_tmp = G_cost[current] + 1
                    if (neighbour not in openset) or (G_cost_tmp < G_cost[neighbour]): 
                        came_from[neighbour] = current
                        G_cost[neighbour] = G_cost_tmp
                        F_cost[neighbour] = G_cost[neighbour] + Algorithms.heuresticCost(neighbour,endPoint)
                        if neighbour not in openset:
                            openset.add(neighbour)


        




       
