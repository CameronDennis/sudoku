"""Sudoku solver!
"""

import array as arr

GRID_SIZE = 9

class Notes(object):
    """Class for notes on squares within grid"""
    max_note = GRID_SIZE
    def __init__(self):
        self.note = 0
        pass
    
    def mark(self, value: int):
        self.note |= 1<<(value - 1)

    def clear(self, value: int):
        self.note &= (2**9 - 1) ^ (1<<(value - 1))

    def view(self):
        notes = []
        temp = self.note
        for val in range(1, GRID_SIZE+1):
            if temp % 2:
                notes.append(val)
            temp = temp >> 1
        print(notes)
    pass

class Square(object):
    """Class for squares within grid"""
    
    def __init__(self):
        self.value = 0
        pass

class Sudoku(object):
    """Class for Sudoku"""

    def __init__(self):
        pass

    pass

def main():
    pass

if __name__ == "__main__":
    main()
    pass


