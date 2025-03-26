from window import Window, Point, Line


def main():
    win = Window(800, 600)

    point1 = Point(100, 100)
    point2 = Point(100, 200)
    point3 = Point(200,200)
    line1 = Line(point1, point2)
    line2 = Line(point2, point3)
    line3 = Line(point1, point3)
    for line in [line1, line2, line3]:
        win.draw_line(line, "black")

    win.wait_for_close()


if __name__ == "__main__":
    main()