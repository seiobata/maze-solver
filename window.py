from tkinter import Tk, BOTH, Canvas


class Window():
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__root.protocol("WM_DELETE_WINDOW", self.close())
        self.__canvas = Canvas(self.__root, bg="white", width=width, height=height)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__is_running = False

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__is_running = True
        while self.__is_running:
            self.redraw()

    def close(self):
        self.__is_running = False

    def draw_line(self, line, fill_color="black"):
        line.draw(self.__canvas, fill_color)


class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line():
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def draw(self, canvas, fill_color="black"):
        canvas.create_line(
            self.point1.x, self.point1.y, self.point2.x, self.point2.y, 
            fill=fill_color, width=2,
        )


class Cell():
    def __init__(self, point1, point2, window=None): # Cell made with 2 Points
        self.left_wall = True
        self.right_wall = True
        self.top_wall = True
        self.bottom_wall = True
        self.visited = False
        self._x1 = point1.x   # left x
        self._x2 = point2.x   # right x
        self._y1 = point1.y   # top y
        self._y2 = point2.y   # bottom y
        self._win = window

    def draw(self):
        if self._win is None:
            return
        top_left = Point(self._x1, self._y1)
        top_right = Point(self._x2, self._y1)
        bot_left = Point(self._x1, self._y2)
        bot_right = Point(self._x2, self._y2)
        if self.left_wall:
            line = Line(top_left, bot_left)
            self._win.draw_line(line)
        else:
            line = Line(top_left, bot_left)
            self._win.draw_line(line, "white")
        if self.right_wall:
            line = Line(top_right, bot_right)
            self._win.draw_line(line)
        else:
            line = Line(top_right, bot_right)
            self._win.draw_line(line, "white")
        if self.top_wall:
            line = Line(top_left, top_right)
            self._win.draw_line(line)
        else:
            line = Line(top_left, top_right)
            self._win.draw_line(line, "white")
        if self.bottom_wall:
            line = Line(bot_left, bot_right)
            self._win.draw_line(line)
        else:
            line = Line(bot_left, bot_right)
            self._win.draw_line(line, "white")

    def draw_move(self, to_cell, undo=False):
        source = Point(
            (self._x2 - self._x1)//2 + self._x1,
            (self._y2 - self._y1)//2 + self._y1,
        )
        dest = Point(
            (to_cell._x2 - to_cell._x1)//2 + to_cell._x1,
            (to_cell._y2 - to_cell._y1)//2 + to_cell._y1,
        )
        line = Line(source, dest)
        if undo:
            self._win.draw_line(line, fill_color="gray")
        else:
            self._win.draw_line(line, fill_color="red")
