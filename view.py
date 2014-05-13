import Tkinter as tk


class GridView(tk.Frame):

    def __init__(self, grid, master=None):
        tk.Frame.__init__(self, master)
        self.grid = grid
        
        # Bind keys.
        for key in "<w>", "<a>", "<s>", "<d>":
            self.master.bind(key, self.callback)

        self.text_IDs = []
        self.SIDE = 100
        self.canvas = tk.Canvas(
            master, width=self.SIDE * 4, height=self.SIDE * 4)
        self.canvas.pack()

    def layout_matrix(self, matrix):
        '''Layout the internal representation of
         the grid to grid view.'''
        for ID in self.text_IDs:
            self.canvas.delete(ID)
        self.text_IDs = []
        
        for i in range(4):
            for j in range(4):
                current_rect = self.rects[i][j]
                currrent_cell = matrix[j][i]
                if currrent_cell == 0:
                    currrent_cell = ""
                text_ID = self.canvas.create_text(
                    current_rect[0], current_rect[1], text=currrent_cell)
                self.text_IDs.append(text_ID)

    def initUI(self, matrix):
        '''Handle initial drawing of the grid view.'''
        self.master = tk.Tk()
        self.master.title("2048")
        self.SIDE = 100
        self.canvas.pack()

        self.rects = []
        for row_index in range(4):
            row = []
            for cell_index in range(4):
                self.canvas.create_rectangle(self.SIDE * cell_index, 
                                            0, 
                                            self.SIDE * (cell_index + 1),
                                            self.SIDE * (row_index + 1))
                row.append([self.SIDE * row_index + 50, self.SIDE * cell_index + 50])
            self.rects.append(row)

        self.layout_matrix(matrix)

    def callback(self, event):
        '''Callback the grid object with respect 
        to the key pressed'''
        if event.char == "w":
            self.grid.slide("up")
        elif event.char == "a":
            self.grid.slide("left")
        elif event.char == "s":
            self.grid.slide("down")
        elif event.char == "d":
            self.grid.slide("right")
