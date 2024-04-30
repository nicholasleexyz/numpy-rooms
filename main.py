import numpy as np
import sys

np.set_printoptions(threshold=sys.maxsize)

CELL_WIDTH = 3
CELL_HEIGHT = 3
COLUMNS = 5
ROWS = 5

x_range = np.arange((CELL_WIDTH + 1) * COLUMNS + 1)
y_range = np.arange((CELL_HEIGHT + 1) * ROWS + 1)
xv, yv = np.meshgrid(x_range, y_range)

xv[xv % (CELL_WIDTH + 1) == 0] = 0
yv[yv % (CELL_HEIGHT + 1) == 0] = 0

###

a = np.multiply(xv, yv)
a[a > 0] = 1

print(a)
