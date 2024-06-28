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

print(a.check(1))
print(a.check(2))

a.toggle(1)
a.toggle(2)

a.toggle(5)
a.toggle(5)

a.view()