import math
import sys
import heapq
from utils.maze import *
from utils.cell import cell
from utils.configuration import *

# A*
G_cost = {}
F_cost = {}
came_from = {}
closedset = set()
openset = set()

# Djikstra
d_path = {}
previous = {}
queue = []


class Algorithms:
    def __init__(self):
        self.astar_stop = False
        self.djikstra_stop = False
        self.astar_counter = 0
        self.djikstra_counter = 0

    def djikstra(self, startPoint, endPoint, maze):
        maze.mainGrid[int(endPoint.y/cellWidth)][int(endPoint.x/cellWidth)].color = PURPLE
        maze.mainGrid[int(startPoint.y/cellWidth)][int(startPoint.x/cellWidth)].color = PURPLE
        if(self.djikstra_counter == 0):
           d_path[startPoint] = 0
           previous[startPoint] = None
           heapq.heappush(queue,(d_path[startPoint], startPoint))
           self.djikstra_stop = False

        if(Algorithms.count(queue)>0):
            tmp_distance,current = heapq.heappop(queue)
            maze.mainGrid[int(current.y/cellWidth)][int(current.x/cellWidth)].color = LIGHT_GREEN
            for neighbor in Algorithms.getNeighbours(current):
                tmp_wage = tmp_distance + 1
                if(neighbor not in d_path or tmp_wage < d_path[neighbor]):
                    maze.mainGrid[int(neighbor.y/cellWidth)][int(neighbor.x/cellWidth)].color = LIGHT_YELLOW
                    d_path[neighbor] = tmp_wage
                    heapq.heappush(queue,(d_path[neighbor], neighbor))

        if(current == endPoint):
            while(current):
                maze.mainGrid[int(current.y/cellWidth)][int(current.x/cellWidth)].color = LIGHT_BLUE
                current = prev[current]
            self.djikstra_stop = True
                

        

    def astar(self, startPoint, endPoint, maze):
        maze.mainGrid[int(endPoint.y/cellWidth)][int(endPoint.x/cellWidth)].color = PURPLE
        maze.mainGrid[int(startPoint.y/cellWidth)][int(startPoint.x/cellWidth)].color = PURPLE
        if(self.astar_counter==0):
            G_cost[startPoint] = 0
            F_cost[startPoint] = G_cost[startPoint] + Algorithms.heuresticCost(startPoint, endPoint)
            openset.add(startPoint)
            self.astar_stop = False

        if(Algorithms.count(openset)>0):
            self.astar_counter = self.astar_counter + 1
            for cell in openset:
                    maze.mainGrid[int(cell.y/cellWidth)][int(cell.x/cellWidth)].color = LIGHT_YELLOW
            F_cost_sorted = sorted(F_cost, key=lambda cell: G_cost[cell] + Algorithms.heuresticCost(cell, endPoint))
            i = 0
            for i in range(len(F_cost_sorted)-1):
                i = i+1
                if(F_cost_sorted[i] not in closedset):
                    break

            current = F_cost_sorted[i]
            if(current == endPoint):
                print("A* END")
                self.astar_stop = True
                for cell in Algorithms.reconstruct_path(endPoint):
                    maze.mainGrid[int(cell.y/cellWidth)][int(cell.x/cellWidth)].color = LIGHT_BLUE
                maze.mainGrid[int(endPoint.y/cellWidth)][int(endPoint.x/cellWidth)].color = PURPLE
                maze.mainGrid[int(startPoint.y/cellWidth)][int(startPoint.x/cellWidth)].color = PURPLE
                return

            try:
                openset.remove(current)
            except KeyError:
                pass

            closedset.add(current)

            for neighbour in Algorithms.getNeighbours(current):
                maze.mainGrid[int(neighbour.y/cellWidth)][int(neighbour.x/cellWidth)].color = LIGHT_GREEN
                if neighbour not in closedset:
                    G_cost_tmp = G_cost[current] + 1
                    if (neighbour not in openset) or (G_cost_tmp < G_cost[neighbour]): 
                        came_from[neighbour] = current
                        G_cost[neighbour] = G_cost_tmp
                        F_cost[neighbour] = G_cost[neighbour] + Algorithms.heuresticCost(neighbour,endPoint)
                        if neighbour not in openset:
                            openset.add(neighbour)

    def reset(self, maze):
        # A* reset
        self.astar_stop = False
        self.astar_counter = 0
        G_cost = {}
        F_cost = {}
        came_from = {}
        closedset.clear()
        openset.clear()
        # Djikstra reset
        self.djikstra_stop = False
        d_path = {}
        previous = {}
        queue = []

        for y in range(rows):
             for x in range(cols):
                  maze.mainGrid[y][x].color = WHITE

    @staticmethod
    def count(collection):
        counter = 0
        for i in collection:
            counter = counter + 1
        return counter

    @staticmethod
    def getNeighbours(cell):
        neighbours = set()

        if cell.cellWalls[0] == False:
            neighbours.add(cell.topNeighbor)
        if cell.cellWalls[1] == False:
            neighbours.add(cell.rightNeighbor)
        if cell.cellWalls[2] == False:
            neighbours.add(cell.bottomNeighbor)
        if cell.cellWalls[3] == False:
            neighbours.add(cell.leftNeighbor)
        
        return neighbours

    @staticmethod
    def heuresticCost(start, end):
        x = (int(start.x/cellWidth) - int(end.x/cellWidth))
        y = (int(start.y/cellWidth) - int(end.y/cellWidth))
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

