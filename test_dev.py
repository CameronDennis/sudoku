"""Testing!
"""

from sudoku import Notes, Sudoku

def notes_basic():
    a = Notes()
    a.mark(1)
    a.mark(2)
    a.mark(9)

    a.clear(8)
    a.clear(2)

    a.view()

    print(a.check(1))
    print(a.check(2))

    a.toggle(1)
    a.toggle(2)

    a.toggle(5)
    a.toggle(5)

    a.view()


def board_basic():
    board_0 = Sudoku()
    board_0.view()
    with open("easy50.txt") as board_file:
        board_1 = list(board_file.readline())[:-1]
        board = Sudoku(board_1)
        board.view()


board_basic()