from game import Grid

def test_shift_left():
    grid = Grid()
    assert(grid.shift_left([2, 0, 0, 0]) == [2, 0, 0, 0])
    assert(grid.shift_left([0, 0, 0, 2]) == [2, 0, 0, 0])
    assert(grid.shift_left([2, 2, 0, 0]) == [4, 0, 0, 0])
    assert(grid.shift_left([2, 0, 2, 0]) == [4, 0, 0, 0])
    assert(grid.shift_left([2, 0, 0, 2]) == [4, 0, 0, 0])
    assert(grid.shift_left([0, 0, 2, 2]) == [4, 0, 0, 0])
    assert(grid.shift_left([2, 2, 2, 0]) == [4, 2, 0, 0])
    assert(grid.shift_left([2, 4, 0, 0]) == [2, 4, 0, 0])
    assert(grid.shift_left([0, 0, 2, 4]) == [2, 4, 0, 0])
    assert(grid.shift_left([2, 2, 2, 2]) == [4, 4, 0, 0])
    assert(grid.shift_left([4, 4, 4, 4]) == [8, 8, 0, 0])
    assert(grid.shift_left([2, 0, 4, 4]) == [2, 8, 0, 0])
    assert(grid.shift_left([2, 2, 0, 2]) == [4, 2, 0, 0])
    assert(grid.shift_left([2, 2, 4, 4]) == [4, 8, 0, 0])
    assert(grid.shift_left([8, 8, 4, 2]) == [16, 4, 2, 0])
    print "Left tests passed."

def test_shift_right():
    grid = Grid()
    assert(grid.shift_right([2, 0, 0, 0]) == [0, 0, 0, 2])
    assert(grid.shift_right([2, 2, 0, 0]) == [0, 0, 0, 4])
    assert(grid.shift_right([2, 0, 2, 0]) == [0, 0, 0, 4])
    assert(grid.shift_right([2, 0, 0, 2]) == [0, 0, 0, 4])
    assert(grid.shift_right([0, 0, 2, 2]) == [0, 0, 0, 4])
    assert(grid.shift_right([2, 4, 0, 0]) == [0, 0, 2, 4])
    assert(grid.shift_right([2, 2, 2, 2]) == [0, 0, 4, 4])
    assert(grid.shift_right([4, 4, 4, 4]) == [0, 0, 8, 8])
    assert(grid.shift_right([2, 0, 4, 4]) == [0, 0, 2, 8])
    assert(grid.shift_right([2, 2, 0, 2]) == [0, 0, 2, 4])
    assert(grid.shift_right([2, 2, 4, 4]) == [0, 0, 4, 8])
    assert(grid.shift_right([8, 8, 4, 2]) == [0, 16, 4, 2])
    print "Right tests passed."

if __name__=="__main__":
    test_shift_left()
    test_shift_right()
