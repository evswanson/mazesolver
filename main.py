from tkinter import Tk, BOTH, Canvas


class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Window")
        self.__root.configure(width=width, height=height)
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.canvas = Canvas(self.__root)
        self.canvas.pack()
        self.is_running = False

    
    def redraw(self):
        print('redraw')
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.is_running = True
        while self.is_running:
            self.redraw()
    
    def close(self):
        self.is_running = False
        


class Point:
    def __init__(self):
        self.x = 0
        self.y = 0

def main():
    win = Window(800, 600)
    win.wait_for_close()

if __name__ == '__main__':
    main()
