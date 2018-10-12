import numpy as np


print("hello world")

mainGrid = np.zeros((10,10), int)
print(mainGrid)
for x in mainGrid:
    mainGrid[x][x] = 1

print(mainGrid)