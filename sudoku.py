"""Sudoku solver!
"""

import array as arr

GRID_SIZE = 9
TOTAL_SQUARES = GRID_SIZE ** 2

class bcolors:
    MAGENTA = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

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

    def __repr__(self):
        output = ""
        if self.locked:
            output += bcolors.MAGENTA
        output += f"{self.value}"
        if self.locked:
            output += bcolors.ENDC
        return output

    def __init__(self, 
                 value: int = 0, 
                 row: int = None, col: int = None, box: int = None):
        # value is the assigned number for the square
        self.value = int(value)

        # zone is the set of all squares relative to this one
        # not including itself
        # ie, square (1,7) would include all squares in row 1, column 7, and box 3
        self.zone = set()

        self.row = row
        self.col = col
        self.box = box

        if self.value:
            self.locked = True
        else:
            self.locked = False

        self.notes = Notes()

    def get_val(self):
        return self.value
    
    def set_val(self, value):
        if not self.locked:
            self.value = value

    def add_to_zone(self, sqr):
        if sqr != self:
            self.zone.add(sqr)

    def get_zone(self):
        return self.zone

class Sudoku(object):
    """Class for Sudoku"""

    dim = GRID_SIZE
    
    def __init__(self, values = []):
        if (type(values) is list) and (len(values) == TOTAL_SQUARES):
            self.board = [ Square(value) for value in values ]
        else:
            self.board = [ Square() ] * (self.dim ** 2)

        pass

    def view_ascii(self):
        output = ""
        for val_ind in range(0, TOTAL_SQUARES):
            if self.board[val_ind].locked:
                output += f"{bcolors.MAGENTA}{self.board[val_ind].get_val()}{bcolors.ENDC} "

            else:
                output += str(self.board[val_ind].get_val())
                output += " "

            if (not (val_ind + 1)%3) and ((val_ind + 1) % GRID_SIZE):
                output += f"{bcolors.OKBLUE}| {bcolors.ENDC}"
            if not (val_ind + 1)%GRID_SIZE:
                output += "\n"
            if not (val_ind + 1)%(GRID_SIZE*3) and ((val_ind + 1) % GRID_SIZE**2):
                output += bcolors.OKBLUE
                output += "-" * (GRID_SIZE * 2 + 3)
                output += bcolors.ENDC
                output += "\n"
            
        print(output)

    def get_row(self, row_ind):
        return self.board[row_ind*GRID_SIZE:row_ind*GRID_SIZE+GRID_SIZE]
    
    def get_col(self, col_ind):
        column = []
        for row in range(GRID_SIZE):
            column.append(self.board[row*GRID_SIZE + col_ind]) 
        return column
    
    def get_box(self, box_ind):
        # rows correspond to box_ind // 3 
        # box 4 -> 4 // 3 = 1*3, 1*3+1, 1*3+2 -> 3,4,5
        # cols correspond to box_ind % 3
        # box 4 -> 4 % 3 = 1*3, 1*3+1, 1*3+2, -> 3,4,5
        box = []
        row_start = (box_ind//3)*3
        col_start = (box_ind%3)*3 
        for row_ind in range(row_start, row_start+3):
            for col_ind in range(col_start, col_start+3):
                box.append(self.board[row_ind*GRID_SIZE + col_ind])
        return box
    
    def get_square(self, row, col):
        return self.board[row*GRID_SIZE + col]
    
    def init_zone(self, square: Square):
        for sqr in self.get_row(row):
            square.add_to_zone(sqr)
        for sqr in self.get_col(col):
            square.add_to_zone(sqr)
        for sqr in self.get_box(box):
            square.add_to_zone(sqr)
        return self.zone
    
    def get_zone(self):
        return self.zone
    

def main():
    pass

if __name__ == "__main__":
    main()
    pass


