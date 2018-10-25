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
    def __init__(self):
        self.astar_stop = False
        self.astar_counter = 0

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
                    print("YELLOW: " + str(int(cell.x/cellWidth)) + "," + str(int(cell.y/cellWidth)))
                    maze.mainGrid[int(cell.y/cellWidth)][int(cell.x/cellWidth)].color = LIGHT_YELLOW
            F_cost_sorted = sorted(F_cost, key=lambda cell: G_cost[cell] + Algorithms.heuresticCost(cell, endPoint))
            i = 0
            for i in range(len(F_cost_sorted)-1):
                i = i+1
                if(F_cost_sorted[i] not in closedset):
                    break

            current = F_cost_sorted[i]
            if(current == endPoint):
                print("END")
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
            #for cell in closedset:
            #        maze.mainGrid[int(cell.x/cellWidth)][int(cell.y/cellWidth)].color = LIGHT_GREEN

            for neighbour in Algorithms.getNeighbours(current):
                maze.mainGrid[int(neighbour.y/cellWidth)][int(neighbour.x/cellWidth)].color = LIGHT_GREEN
                print("GREEN: " + str(int(neighbour.x/cellWidth)) + "," + str(int(neighbour.y/cellWidth)) )
                if neighbour not in closedset:
                    G_cost_tmp = G_cost[current] + 1
                    if (neighbour not in openset) or (G_cost_tmp < G_cost[neighbour]): 
                        came_from[neighbour] = current
                        G_cost[neighbour] = G_cost_tmp
                        F_cost[neighbour] = G_cost[neighbour] + Algorithms.heuresticCost(neighbour,endPoint)
                        if neighbour not in openset:
                            openset.add(neighbour)

    @staticmethod
    def count(collection):
        counter = 0
        for i in collection:
            counter = counter + 1
        return counter

    @staticmethod
    def getNeighbours(cell):
        neighbours = set()
        print("==========================")
        print(str(int(cell.x/cellWidth)) + ',' + str(int(cell.y/cellWidth)) + str(cell.cellWalls))

        if cell.cellWalls[0] == False:
            neighbours.add(cell.topNeighbor)
            print("ADD TOP: " + str(int(cell.topNeighbor.x/cellWidth)) + ',' + str(int(cell.topNeighbor.y/cellWidth)) + str(cell.topNeighbor.cellWalls))
        if cell.cellWalls[1] == False:
            neighbours.add(cell.rightNeighbor)
            print("ADD RIGHT: " + str(int(cell.rightNeighbor.x/cellWidth)) + ',' + str(int(cell.rightNeighbor.y/cellWidth)) + str(cell.rightNeighbor.cellWalls))
        if cell.cellWalls[2] == False:
            neighbours.add(cell.bottomNeighbor)
            print("ADD BOTTOM: " + str(int(cell.bottomNeighbor.x/cellWidth)) + ',' + str(int(cell.bottomNeighbor.y/cellWidth)) + str(cell.bottomNeighbor.cellWalls))
        if cell.cellWalls[3] == False:
            neighbours.add(cell.leftNeighbor)
            print("ADD LEFT: " + str(int(cell.leftNeighbor.x/cellWidth)) + ',' + str(int(cell.leftNeighbor.y/cellWidth)) + str(cell.leftNeighbor.cellWalls))
        
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

