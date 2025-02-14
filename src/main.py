from graphics import Window
from maze import Maze

def main():
    win = Window(800, 600)

    #maze = Maze(20, 20, 2, 10, 50, 50, win)
    num_cols = 12
    num_rows = 10
    m1 = Maze(10, 10, num_rows, num_cols, 20, 20, win)

    m1.solve()

    win.wait_for_close()


main()
