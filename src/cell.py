from line import Line
from point import Point

class Cell:
    def __init__(self, x1, y1, x2, y2):
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2

        self.__top_wall = Line(Point(x1, y1), Point(x2, y1))
        self.__right_wall = Line(Point(x2, y1), Point(x2, y2))
        self.__botom_wall = Line(Point(x1, y2), Point(x2, y2))
        self.__left_wall = Line(Point(x1, y1), Point(x1, y2))

        self.has_top_wall = True
        self.has_right_wall = True
        self.has_bottom_wall = True
        self.has_left_wall = True

    def draw(self, canvas, wall_color):
        if self.has_top_wall:
            self.__top_wall.draw(canvas, wall_color)
        if self.has_right_wall:
            self.__right_wall.draw(canvas, wall_color)
        if self.has_bottom_wall:
            self.__botom_wall.draw(canvas, wall_color)
        if self.has_right_wall:
            self.__left_wall.draw(canvas, wall_color)

