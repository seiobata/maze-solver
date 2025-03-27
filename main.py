from window import Window, Point, Cell


def main():
    win = Window(800, 600)

    point1 = Point(100, 100)
    point2 = Point(200, 200)
    point3 = Point(200, 100)
    point4 = Point(300, 200)
    cell1 = Cell(point1, point2, win)
    cell2 = Cell(point3, point4, win)

    cell1.bottom_wall = False
    cell1.right_wall = False
    cell1.draw()

    cell2.left_wall = False
    cell2.top_wall = False
    cell2.draw()

    cell1.draw_move(cell2)

    win.wait_for_close()


if __name__ == "__main__":
    main()