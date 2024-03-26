import time
import random

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
        if seed:
            random.seed(seed)
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()
    
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

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            next_index_list = []
            # determine which cells to visit next
            #left 
            if i > 0 and not self._cells[i-1][j].visited:
                next_index_list.append((i-1, j))
            # right
            if i < self._num_cols - 1 and not self._cells[i+1][j].visited:
                next_index_list.append((i + 1, j))
            # up
            if j > 0 and not self._cells[i][j-1].visited:
                next_index_list.append((i, j-1))
            # down
            if j < self._num_rows - 1 and not self._cells[i][j+1].visited:
                next_index_list.append((i, j+1))
            
            # if there is nowhere to go just break out
            if len(next_index_list) == 0:
                # draw current cell
                self._draw_cell(i, j)
                return
            
            # randomly choose the next direction to go to
            direction_index = random.randrange(len(next_index_list))
            next_index = next_index_list[direction_index]

            # knock down current cell and chosen cell walls
            # right
            if next_index[0] == i + 1:
                self._cells[i][j].has_right_wall = False
                self._cells[i+1][j].has_left_wall = False
            # left
            if next_index[0] == i - 1:
                self._cells[i][j].has_left_wall = False
                self._cells[i-1][j].has_right_wall = False
            # down
            if next_index[1] == j + 1:
                self._cells[i][j].has_bottom_wall = False
                self._cells[i][j+1].has_top_wall = False
            # up 
            if next_index[1] == j - 1:
                self._cells[i][j].has_top_wall = False
                self._cells[i][j-1].has_bottom_wall = False

            # move to the chosen cell by recursion
            self._break_walls_r(next_index[0], next_index[1])

    def _reset_cells_visited(self):
        for col in range(self._num_cols):
            for row in range(self._num_rows):
                self._cells[col][row].visited = False
            