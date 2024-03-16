import time

from cell import Cell


# A list of lists to hold cells
class Maze:
    def __init__(self, x1, y1, 
                 num_rows, num_cols,
                 cell_size_x, cell_size_y,
                 win=None, seed=None):
        self._cells = []
        # how many pixels from the top and left the maze should start from side of window
        self._x1 = x1
        self._y1 = y1
        # number of rows and columns
        self._num_rows = num_rows
        self._num_cols = num_cols
        # how big the cells should be
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._seed = seed
        self._create_cells()
        self._break_entrance_and_exit()
    
    def _create_cells(self):
        for col in range(self._num_cols):
            col_cells = []
            for row in range(self._num_rows):
                col_cells.append(Cell(self._win))
            self._cells.append(col_cells)
        
        for col in range(self._num_cols):
            for row in range(self._num_rows):
                self._draw_cell(col, row)
    
    def _draw_cell(self, i, j):
        if self._win is None:
            return
        x1 = self._x1 + i * self._cell_size_x
        y1 = self._y1 + j * self._cell_size_y
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()
    
    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        # entrance will always be top-top left
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0,0)
        # exit will always be bottom-bottom right
        self._cells[-1][-1].has_bottom_wall = False
        self._draw_cell(self._num_cols-1, self._num_rows-1)