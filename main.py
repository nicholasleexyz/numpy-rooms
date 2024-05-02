import numpy as np
import sys

np.set_printoptions(threshold=sys.maxsize)


def generate_maze(
        columns: np.int32 = 4,
        rows: np.int32 = 4) -> np.ndarray[np.int32, np.ndim(2)]:
    x_range = np.arange(columns * 2 + 1)
    y_range = np.arange(rows * 2 + 1)

    xv, yv = np.meshgrid(x_range, y_range)

    xv[xv % 2 == 0] = 0
    yv[yv % 2 == 0] = 0

    ###

    a = np.multiply(xv, yv)
    a[a > 0] = 1

    return a


def scale_maze(maze: np.ndarray[np.int32, np.ndim(2)], scale: np.int32) -> np.ndarray[np.int32, np.ndim(2)]:
    rows, columns = maze.shape
    c = (columns - 1) // 2
    r = (rows - 1) // 2

    x_range = np.arange((scale + 1) * c + 1)
    y_range = np.arange((scale + 1) * r + 1)

    xv, yv = np.meshgrid(x_range, y_range)

    xv[xv % (scale + 1) == 0] = 0
    yv[yv % (scale + 1) == 0] = 0
    a = np.multiply(xv, yv)
    a[a > 0] = 1
    return a


def draw_maze(maze: np.ndarray[np.int32, np.ndim(2)]) -> None:
    for y in range(maze.shape[0]):
        line = ""

        for x in range(maze.shape[1]):
            if maze[y, x] == 1:
                line += '. '
            elif maze[y, x] == 0:
                line += '# '

        print(line.strip())


def main():
    maze = generate_maze(4, 4)
    draw_maze(maze)
    print('\n')
    scaled = scale_maze(maze, 5)
    draw_maze(scaled)


if __name__ == '__main__':
    main()
