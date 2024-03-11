from cell import Cell
from graphics import Line, Point, Window



        
def main():
    win = Window(800, 600)

    p1 = Point(2, 20)
    p2 = Point(50, 16)
    line = Line(p1, p2)
    win.draw_line(line, "black")

    cell = Cell(win)
    cell.draw(30, 100, 90, 150)
    
    c = Cell(win)
    c.has_right_wall = False
    c.draw(125, 125, 200, 200)
    
    c.draw_move(cell)
    win.wait_for_close()

if __name__ == '__main__':
    main()
