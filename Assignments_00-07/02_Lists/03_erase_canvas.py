import tkinter as tk

CELL_SIZE = 40
GRID_SIZE = 10

def erase(event):
    row, col = event.y // CELL_SIZE, event.x // CELL_SIZE
    canvas.itemconfig(grid[row][col], fill="white")

def main():
    global canvas, grid

    root = tk.Tk()
    root.title("Grid Eraser")

    canvas = tk.Canvas(root, width=GRID_SIZE * CELL_SIZE, height=GRID_SIZE * CELL_SIZE)
    canvas.pack()

    grid = [[canvas.create_rectangle(c * CELL_SIZE, r * CELL_SIZE, 
                                     (c + 1) * CELL_SIZE, (r + 1) * CELL_SIZE, 
                                     fill="blue", outline="black") 
             for c in range(GRID_SIZE)] for r in range(GRID_SIZE)]

    canvas.bind("<B1-Motion>", erase)

    root.mainloop()

if __name__ == '__main__':
    main()
