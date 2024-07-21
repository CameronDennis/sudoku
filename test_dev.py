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
    board_0.view_ascii()
    with open("easy50.txt") as board_file:
        board_1 = list(board_file.readline())[:-1]
        board = Sudoku(board_1)
        board.view_ascii()

    for i in range(9):
        print(board.get_row(i))

    print("\n")

    for i in range(9):
        print(board.get_col(i))
    
    print("\n")

    board.view_ascii()

    for i in range(9):
        print(board.get_box(i))

    print(board.get_square(3,3))
    board.get_square(3,3).set_val(9)
    print(board.get_square(3,3))


board_basic()