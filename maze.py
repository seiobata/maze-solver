from window import Point, Cell
from time import sleep


class Maze():
    def __init__(
            self,
            x,
            y,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            window=None,
        ):
        self._x = x
        self._y = y
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cells = []
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = window

        self._create_cells()
        self._break_entrance_and_exit()

    def _create_cells(self):
        for i in range(    # starts at far left of maze, steps cell_size_x 
            self._x,       # wide and ends at far right of maze
            (self._num_cols + 1) * self._cell_size_x, 
            self._cell_size_x,
        ):
            column = []
            for j in range(
                self._y, 
                (self._num_rows + 1) * self._cell_size_y, 
                self._cell_size_y,
            ):
                point1 = Point(i,j)
                point2 = Point(
                    i + self._cell_size_x,
                    j + self._cell_size_y,
                )
                column.append(Cell(point1, point2, self._win))
            self._cells.append(column)
        self._draw_cell()
    
    def _draw_cell(self):
        if self._win is None:
            return
        for columns in self._cells:
            for cell in columns:
                cell.draw()
                self._animate()
    
    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        sleep(0.05)

    def _break_entrance_and_exit(self):
        self._cells[0][0].top_wall = False
        self._cells[0][0].draw()    # call on Cell.draw() directly
        self._cells[-1][-1].bottom_wall = False
        self._cells[-1][-1].draw()
