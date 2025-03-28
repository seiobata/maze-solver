from window import Point, Cell
from time import sleep
from random import seed, choice


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
            new_seed=None,
        ):
        self._x = x
        self._y = y
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cells = []
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = window
        if new_seed:
            seed(new_seed)

        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()

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
        sleep(0.01)

    def _break_entrance_and_exit(self):
        self._cells[0][0].top_wall = False
        self._cells[0][0].draw()    # call on Cell.draw() directly
        self._cells[-1][-1].bottom_wall = False
        self._cells[-1][-1].draw()

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            neighbors = []

            # adding neighbors of current cell as tuples
            if i > 0 and not self._cells[i - 1][j].visited:
                neighbors.append((i - 1, j)) # left neighbor
            if i < self._num_cols - 1 and not self._cells[i + 1][j].visited:
                neighbors.append((i + 1, j)) # right
            if j > 0 and not self._cells[i][j - 1].visited:
                neighbors.append((i, j - 1)) # top
            if j < self._num_rows - 1 and not self._cells[i][j + 1].visited:
                neighbors.append((i, j + 1)) # bottom

            # if no more neighbors to visit, return
            if len(neighbors) == 0:
                self._cells[i][j].draw()
                self._animate()
                return
            
            # pick a random direction
            neighbor = choice(neighbors)

            #knock down walls between current and next cell
            if neighbor[0] == i - 1: # left wall
                self._cells[i][j].left_wall = False
                self._cells[i - 1][j].right_wall = False
            if neighbor[0] == i + 1: # right
                self._cells[i][j].right_wall = False
                self._cells[i + 1][j].left_wall = False
            if neighbor[1] == j - 1: # top
                self._cells[i][j].top_wall = False
                self._cells[i][j - 1].bottom_wall = False
            if neighbor[1] == j + 1: # bottom
                self._cells[i][j].bottom_wall = False
                self._cells[i][j + 1].top_wall = False
            
            self._break_walls_r(neighbor[0], neighbor[1])

    def _reset_cells_visited(self):
        for columns in self._cells:
            for cell in columns:
                cell.visited = False

    def solve(self):
        return self._solve_r(0, 0)

    def _solve_r(self, i, j):
        self._animate()
        current = self._cells[i][j]
        current.visited = True
        if current == self._cells[-1][-1]: # if at end cell, we're done
            return True

        if ( # check if can move to left cell
            i > 0 and
            not current.left_wall and
            not self._cells[i - 1][j].visited
        ):
            if self._solve_helper(current, i - 1, j):
                return True
        
        if ( # check right cell
            i < self._num_cols - 1 and
            not current.right_wall and
            not self._cells[i + 1][j].visited
        ):
            if self._solve_helper(current, i + 1, j):
                return True

        if ( # check top cell
            j > 0 and
            not current.top_wall and
            not self._cells[i][j - 1].visited
        ):
            if self._solve_helper(current, i, j - 1):
                return True

        if ( # check bottom cell
            j < self._num_rows - 1 and
            not current.bottom_wall and
            not self._cells[i][j + 1].visited
        ):
            if self._solve_helper(current, i, j + 1):
                return True
        
        return False

    def _solve_helper(self, current, i, j):
        next = self._cells[i][j]
        current.draw_move(next)
        if self._solve_r(i, j):
            return True
        else:
            current.draw_move(next, True)
