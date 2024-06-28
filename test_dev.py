"""Testing!
"""

from sudoku import Notes

a = Notes()
a.mark(1)
a.mark(2)
a.mark(9)

a.clear(8)
a.clear(2)

a.view()