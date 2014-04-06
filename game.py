from random import randint
from view import GridView


class Grid(object):

    def __init__(self):
        self.matrix = [ [2, 0, 2, 0],
                        [0, 0, 0, 8],
                        [0, 2, 0, 0],
                        [0, 0, 2, 4]]

        self.score = 0

        print "Play with WASD!"
        self.grid_view = GridView(self)
        self.grid_view.initUI(self.matrix)
        self.grid_view.mainloop()

    def get_column(self, nth):
        column = []
        for row in self.matrix:
            column.append(row[nth])
        return column

    def set_column(self, nth, column):
        for i in range(4):
            self.matrix[i][nth] = column[i]

    def insert_random_num(self):
        x = randint(0, 3)
        y = randint(0, 3)

        while not self.matrix[y][x] == 0:
            x = randint(0, 3)
            y = randint(0, 3)

        self.matrix[y][x] = 2

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

        print self.score
        self.insert_random_num()
        self.grid_view.layoutMatrix(self.matrix)

    def shift_left(self, array):
        # If empty no shift happens
        if sum(array) == 0:
            return array

        array = filter(lambda x: x != 0, array)

        for index in range(1, len(array)):
            if array[index - 1] == array[index]:
                array[index - 1] += array[index]
                self.score += array[index - 1]
                array[index] = 0
        array = filter(lambda x: x != 0, array)

        while len(array) < 4:
            array.append(0)
        return array

    def shift_right(self, array):
        # If left shift is applied to the reversed
        # array and then the output is reversed again
        # we get a right shift.
        array = self.shift_left(array[::-1])
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
