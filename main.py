from cell import Cell
from graphics import Line, Point, Window
from maze import Maze



        
def main():
    win = Window(800, 600)

    Maze(0, 0, 2, 4, 2, 3, win)
    win.wait_for_close()

if __name__ == '__main__':
    main()
