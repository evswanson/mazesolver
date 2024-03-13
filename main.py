from cell import Cell
from graphics import Line, Point, Window
from maze import Maze



        
def main():
    win = Window(800, 600)
    num_cols = 12
    num_rows = 10
    Maze(0, 10, num_rows, num_cols, 10, 10, win)
    win.wait_for_close()

if __name__ == '__main__':
    main()
