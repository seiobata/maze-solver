from window import Window, Point, Cell


def main():
    win = Window(800, 600)

    point1 = Point(100, 100)
    point2 = Point(200, 200)
    point3 = Point(300, 300)
    cell1 = Cell(point1, point2, win)
    cell2 = Cell(point2, point3, win)

    cell1.bottom_wall = False
    cell1.draw()

    cell2.right_wall = False
    cell2.top_wall = False
    cell2.draw()

    win.wait_for_close()


if __name__ == "__main__":
    main()