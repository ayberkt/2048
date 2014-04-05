from random import randint
from view import GridView


class Grid(object):

    def __init__(self):
        # empty_array = [0, 0, 0, 0]
        # self.matrix = [empty_array] * 4  # Array of four empty arrays.

        self.matrix = [[2, 0, 2, 0]]
        self.matrix.append([0, 0, 0, 8])
        self.matrix.append([0, 2, 0, 0])
        self.matrix.append([0, 0, 2, 4])

        self.grid_view = GridView(self)
        self.grid_view.initUI(self.matrix)
        self.grid_view.mainloop()
        # self.grid_view.layoutMatrix(self.matrix)

    def get_column(self, nth):
        column = []
        for row in self.matrix:
            column.append(row[nth])
        return column

    def set_column(self, nth, column):
        for i in range(4):
            self.matrix[i][nth] = column[i]

    def insert_random_num():
        x = randint(0, 4)
        y = randint(0, 4)

        while not self.matrix[y][x] == 0:
            x = randint(0, 4)
            y = randint(0, 4)

        self.matrix[y][x] == 2

    def slide(self, direction):
        ''' u for up, r for right, l for left, d for down '''
        if direction == "u":
            for i in range(4):
                column = self.get_column(i)
                column = self.shift_left(column)
                self.set_column(i, column)
        elif direction == "r":
            for i in range(4):
                row = self.matrix[i]
                row = self.shift_right(row)
                self.matrix[i] = row
        elif direction == "d":
            for i in range(4):
                column = self.get_column(i)
                column = self.shift_right(column)
                self.set_column(i, column)
        elif direction == "l":
            for i in range(4):
                row = self.matrix[i]
                row = self.shift_left(row)
                self.matrix[i] = row

        self.grid_view.layoutMatrix(self.matrix)

    def shift_left(self, array):
        # If empty no shift happens
        if sum(array) == 0:
            return array

        array = filter(lambda x: x != 0, array)

        for index in range(1, len(array)):
            if array[index - 1] == array[index]:
                array[index - 1] += array[index]
                array[index] = 0
        array = filter(lambda x: x != 0, array)

        while len(array) < 4:
            array.append(0)
        return array

    def shift_right(self, array):
        if sum(array) == 0:
            return array

        array = array[::-1]

        array = filter(lambda x: x != 0, array)

        for index in range(1, len(array)):
            if array[index - 1] == array[index]:
                array[index - 1] += array[index]
                array[index] = 0
        array = filter(lambda x: x != 0, array)

        while len(array) < 4:
            array.append(0)
        return array[::-1]

    def matrix_str(self):
        matrix_str = ""
        for row in self.matrix:
            row_str = ""
            for num in row:
                if num == 0:
                    row_str += " . "
                else:
                    row_str += " " + str(num) + " "
            row_str += "\n"
            matrix_str += row_str
        return matrix_str



if __name__ == "__main__":
    game_grid = Grid()
        