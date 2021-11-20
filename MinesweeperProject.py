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