import Tkinter as tk

class GridView(tk.Frame):

    def __init__(self, grid, master=None):
        tk.Frame.__init__(self, master)
        self.grid = grid
        self.master.bind("<w>", self.callback)
        self.master.bind("<a>", self.callback)
        self.master.bind("<s>", self.callback)
        self.master.bind("<d>", self.callback)

        self.text_IDs = []
        self.SIDE = 100
        self.canvas = tk.Canvas(master, width=self.SIDE * 4, height=self.SIDE * 4)
        self.canvas.pack()
        # self.initUI()

    def layoutMatrix(self, matrix):
        for ID in self.text_IDs:
            self.canvas.delete(ID)
        self.text_IDs = []
        for i in range(4):
            for j in range(4):
                current_rect = self.rects[i][j]
                currrent_cell = matrix[j][i]
                if currrent_cell == 0:
                    currrent_cell = ""
                text_ID = self.canvas.create_text(current_rect[0], current_rect[1], text=currrent_cell)
                self.text_IDs.append(text_ID)


    def initUI(self, matrix):
        self.master = tk.Tk()
        self.master.title("2048")
        self.SIDE = 100
        self.canvas.pack()
        
        self.rects = []
        for i in range(4):
            row = []
            for j in range(4):
                self.canvas.create_rectangle(self.SIDE * j, 0, self.SIDE * (j + 1), self.SIDE * (i + 1))
                # w.create_text(self.SIDE * i + 50, self.SIDE * j + 50, text=str(i + 1) + ", " + str(j + 1))
                row.append([self.SIDE * i + 50, self.SIDE * j + 50])
            self.rects.append(row)

        self.layoutMatrix(matrix)

    def callback(self, event):
        if event.char == "w":
            self.grid.slide("u")
        if event.char == "a":
            self.grid.slide("l")
        if event.char == "s":
            self.grid.slide("d")
        if event.char == "d":
            self.grid.slide("r")

if __name__=="__main__":
    grid_view = GridView()

    matrix = [[0, 0, 0, 0],
          [0, 0, 2, 2],
          [0, 0, 0, 0],
          [4, 0, 0, 0]]

    grid_view.initUI(matrix)
    grid_view.mainloop()