"""Sudoku solver!
"""

import array as arr

GRID_SIZE = 9

class Notes(object):
    """Class for notes on squares within grid
Notes are stored on a single variable using bitmasking
"""
    max_note = GRID_SIZE
    def __init__(self):
        self.note = 0
        pass
    
    def mark(self, value: int):
        self.note |= 1<<(value - 1)

    def clear(self, value: int):
        self.note &= (2**GRID_SIZE - 1) ^ (1<<(value - 1))

    def check(self, value: int):
        if self.note & (1<<(value-1)):
            return True
        return False

    def toggle(self, value):
        if self.check(value):
            self.clear(value)
        else: 
            self.mark(value)

    def view(self):
        notes = []
        temp = self.note
        for val in range(1, GRID_SIZE+1):
            if self.check(val):
                notes.append(val)
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


