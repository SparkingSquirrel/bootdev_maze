from window import Window
from point import Point
from line import Line
from cell import Cell

def main():
    win = Window(800, 600)
    # p1 = Point(100, 100)
    # p2 = Point(100, 300)
    # p3 = Point(400, 300)
    # line1 = Line(p1, p2)
    # line2 = Line(p2, p3)
    # line3 = Line(p3, p1)
    # win.draw_line(line1, "Red")
    # win.draw_line(line2, "Green")
    # win.draw_line(line3, "Blue")

    c1 = Cell(400, 400, 500, 500)
    win.draw_cell(c1, "White")
    c2 = Cell(200, 200, 250, 250)
    c2.has_bottom_wall = False
    win.draw_cell(c2, "Green")



    win.wait_for_close()

main()