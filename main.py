from window import Window
from maze import Maze


def main():
    num_rows = 12
    num_cols = 16
    margin = 50
    window_x = 800
    window_y = 600
    cell_size_x = (window_x - 2 * margin) // num_cols
    cell_size_y = (window_y - 2 * margin) // num_rows
    win = Window(window_x, window_y)

    maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win)

    win.wait_for_close()


if __name__ == "__main__":
    main()