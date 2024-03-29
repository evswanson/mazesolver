from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.canvas = Canvas(self.__root, bg="white", height=height, width=width)
        self.canvas.pack(fill=BOTH, expand=1)
        self.is_running = False

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.is_running = True
        while self.is_running:
            self.redraw()
    
    def close(self):
        self.is_running = False

    def draw_line(self, line, fill_color="black"):
        line.draw(self.canvas, fill_color)


# Create a point
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


# Create a line between two points
class Line:
    def __init__(self, p1, p2):
        self.__p1 = p1
        self.__p2 = p2

    def draw(self, canvas:Canvas, fill_color):
        canvas.create_line(self.__p1.x, self.__p1.y, 
                           self.__p2.x, self.__p2.y, 
                           fill=fill_color, width=2
                           )
        canvas.pack(fill=BOTH, expand=1)