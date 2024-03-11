from graphics import Line, Point

# Holds all data for an individual cell
class Cell:
    def __init__(self, win):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = win

    def draw(self, x1, y1, x2, y2):
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        if self.has_left_wall:
            line = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(line)
        if self.has_top_wall:
            line = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(line)
        if self.has_right_wall:
            line = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(line)
        if self.has_bottom_wall:
            line = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(line)
    
    # Draw path between 2 cells from one center to another
    def draw_move(self, to_cell, undo=False):
        fill_color = "red"
        if undo:
            fill_color = "gray"
        x_mid = (self._x2 + self._x1) / 2
        y_mid = (self._y2 + self._y1) / 2
        to_x_mid = (to_cell._x2 + to_cell._x1) / 2
        to_y_mid = (to_cell._y2 + to_cell._y1) / 2

        line = Line(Point(x_mid, y_mid), Point(to_x_mid, to_y_mid))
        self._win.draw_line(line, fill_color)