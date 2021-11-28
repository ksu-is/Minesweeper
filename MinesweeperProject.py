# MineSweeper Game
from random import randint
# Making mines 
mines = set()
# Making board 
board = [["-" for x in range(10)] for x in range(10)]

#  randomly positioning the mines
def make_mines(mines):

    a = (randint(0,10),randint(0,10))
    b = (randint(0,10),randint(0,10))
    c = (randint(0,10),randint(0,10))
    
    mines.add(a)
    mines.add(b)
    mines.add(c)

# Reavels the mines touching the accessed space's number
def border_nums(board, x, y):
    numMine = 0
    
    # Top-left Space
    if (x > 0 and y > 0):
        c = (x-1, y-1)
        if c in mines:
            numMine += 1

    # Top Space
    if (x > 0):
        c = (x-1, y)
        if c in mines:
            numMine += 1

     # Top-right Space
    if (x > 0 and y < 4):
        c = (x-1, y+1)
        if c in mines:
            numMine += 1
    # Left
    if (y > 0):
        c = (x, y-1)
        if c in mines:
            numMine += 1
    # Right
    if (y < 4):
        c = (x, y+1)
        if c in mines:
            numMine += 1
    # Bottom-left
    if (x < 4 and y > 0):
        c = (x+1, y-1)
        if c in mines:
            numMine += 1
    # Bottom
    if (x < 4):
        c = (x+1, y)
        if c in mines:
            numMine += 1
    # Bottom-right
    if (x < 4 and y < 4):
        c = (x+1, y+1)
        if c in mines:
            numMine += 1

   