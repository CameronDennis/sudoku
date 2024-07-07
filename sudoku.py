"""Sudoku solver!
"""

import array as arr

GRID_SIZE = 9
TOTAL_SQUARES = GRID_SIZE ** 2

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

    def toggle(self, value: int):
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
    
    def __init__(self, value: int = 0 ):
        self.value = int(value)
        self.notes = Notes()

    def val(self):
        return self.value
        pass

class Sudoku(object):
    """Class for Sudoku"""

    dim = GRID_SIZE
    
    def __init__(self, values = []):
        if (type(values) is list) and (len(values) == TOTAL_SQUARES):
            self.board = [ Square(value) for value in values ]
        else:
            self.board = [ Square() ] * (self.dim ** 2)

        pass

    def view(self):
        output = ""
        for val_ind in range(0, TOTAL_SQUARES):
            output += str(self.board[val_ind].val())
            output += " "

            if (not (val_ind + 1)%3) and ((val_ind + 1) % GRID_SIZE):
                output += "| "
            if not (val_ind + 1)%GRID_SIZE:
                output += "\n"
            if not (val_ind + 1)%(GRID_SIZE*3) and ((val_ind + 1) % GRID_SIZE**2):
                output += "-" * (GRID_SIZE * 2 + 3)
                output += "\n"
        print(output)

    pass

def main():
    pass

if __name__ == "__main__":
    main()
    pass


