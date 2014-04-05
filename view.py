from Tkinter import *


def initUI():
    master = Tk()
    master.title("2048")
    SIDE = 100
    w = Canvas(master, width=SIDE * 4, height=SIDE * 4)
    master.title = "2048"
    w.pack()


    # w.create_rectangle(0, 0, 100, 100)
    # w.create_rectangle(100, 0, 200, 100)
    # w.create_rectangle(200, 0, 300, 100)
    # w.create_rectangle(300, 0, 400, 100)

    for i in range(4):
        for j in range(4):
            rect = w.create_rectangle(SIDE * j, 0, SIDE * (j + 1), SIDE * (i + 1))
            w.create_text(SIDE * i + 50, SIDE * j + 50, text=str(i + 1) + ", " + str(j + 1))


# def layoutMatrix(matrix):
#     for row in matrix:
#         for cell in row:

initUI()
mainloop()