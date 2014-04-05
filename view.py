from Tkinter import *

global layoutMatrix
def layoutMatrix(matrix, rects, w):
    for i in range(4):
        for j in range(4):
            current_rect = rects[i][j]
            w.create_text(current_rect[0], current_rect[1], text=str(matrix[i][j]))

def initUI(matrix):
    master = Tk()
    master.title("2048")
    SIDE = 100
    w = Canvas(master, width=SIDE * 4, height=SIDE * 4)
    master.title = "2048"
    w.pack()
    
    rects = []
    for i in range(4):
        row = []
        for j in range(4):
            w.create_rectangle(SIDE * j, 0, SIDE * (j + 1), SIDE * (i + 1))
            # w.create_text(SIDE * i + 50, SIDE * j + 50, text=str(i + 1) + ", " + str(j + 1))
            row.append([SIDE * i + 50, SIDE * j + 50])
        rects.append(row)

    global layoutMatrix
    layoutMatrix(matrix, rects, w)


matrix = [[0, 0, 0, 0],
          [0, 0, 2, 2],
          [0, 0, 0, 0],
          [4, 0, 0, 0]]

initUI(matrix)
mainloop()