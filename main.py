from window import Window
from maze import Maze
from sys import setrecursionlimit


def main():
    num_rows = 12
    num_cols = 16
    margin = 50
    window_x = 800
    window_y = 600
    cell_size_x = (window_x - 2 * margin) // num_cols
    cell_size_y = (window_y - 2 * margin) // num_rows

    setrecursionlimit(10000)
    win = Window(window_x, window_y)

    print("Creating maze...")
    maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win, 7)
    print("Maze created. Solving...")
    solvable = maze.solve()

    if not solvable:
        print("This maze can't be solved!")
    else:
        print("Maze solved!")

    win.wait_for_close()


if __name__ == "__main__":
    main()