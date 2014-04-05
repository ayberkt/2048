import Tkinter as tk
# class GridView(Canvas):

#     def __init__(self):
#         self.master = Tk()
#         self.SIDE = 100
#         self.width = self.height = self.SIDE * 4
#         self.master.title("2048")
#         self.pack()

#     def layoutMatrix(self, matrix, rects):
#         for i in range(4):
#             for j in range(4):
#                 current_rect = rects[i][j]
#                 self.create_text(current_rect[0], current_rect[1], text=str(matrix[i][j]))

#     def initUI(self, matrix):
#         rects = []
#         for i in range(4):
#             row = []
#             for j in range(4):
#                 self.create_rectangle(self.SIDE * j, 0, self.SIDE * (j + 1), self.SIDE * (i + 1))
#                 # w.create_text(self.SIDE * i + 50, self.SIDE * j + 50, text=str(i + 1) + ", " + str(j + 1))
#                 row.append([self.SIDE * i + 50, self.SIDE * j + 50])
#             rects.append(row)

#         self.layoutMatrix(matrix, rects)

class GridView(tk.Frame):

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.SIDE = 100
        self.canvas = tk.Canvas(master, width=self.SIDE * 4, height=self.SIDE * 4)
        # self.initUI()

    def layoutMatrix(self, matrix):
        for i in range(4):
            for j in range(4):
                current_rect = self.rects[i][j]
                self.canvas.create_text(current_rect[0], current_rect[1], text=str(matrix[i][j]))

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
        
grid_view = GridView()
grid_view.initUI(matrix)
grid_view.mainloop()