# MineSweeper Game
import random
#  Randomly positioning the mines
def MakeMines(a,z):
    disp = [[0 for row in range(a)] for column in range(a)]
    for num in range(z):
        x = random.randint(0,a-1)
        y = random.randint(0,a-1)
        disp[y][x] = 'X'
        if (x >=0 and x <= a-2) and (y >= 0 and y <= a-1):
                # Center-Right
            if disp[y][x+1] != 'X':
                disp[y][x+1] += 1 
                # Center-Left
        if (x >=1 and x <= a-1) and (y >= 0 and y <= a-1):
            if disp[y][x-1] != 'X':
                disp[y][x-1] += 1 
                # Top-Left
        if (x >= 1 and x <= a-1) and (y >= 1 and y <= a-1):
            if disp[y-1][x-1] != 'X':
                disp[y-1][x-1] += 1 
                # Top-Right
        if (x >= 0 and x <= a-2) and (y >= 1 and y <= a-1):
            if disp[y-1][x+1] != 'X':
                disp[y-1][x+1] += 1 
                # Top-Center
        if (x >= 0 and x <= a-1) and (y >= 1 and y <= a-1):
            if disp[y-1][x] != 'X':
                disp[y-1][x] += 1 
                # Bottom-Right
        if (x >=0 and x <= a-2) and (y >= 0 and y <= a-2):
            if disp[y+1][x+1] != 'X':
                disp[y+1][x+1] += 1 
                # Bottom-Left
        if (x >= 1 and x <= a-1) and (y >= 0 and y <= a-2):
            if disp[y+1][x-1] != 'X':
                disp[y+1][x-1] += 1 
                # Bottom-Center
        if (x >= 0 and x <= a-1) and (y >= 0 and y <= a-2):
            if disp[y+1][x] != 'X':
                disp[y+1][x] += 1 

    return disp

def GenerateMap(a):
    disp = [['-' for row in range(a)] for column in range(a)]
    return disp

def OpenMap(map):
    for row in map:
        print(" ".join(str(cell) for cell in row))
        print("")

def WinCheck(map):
    for row in map:
        for cell in row:
            if cell == '-':
                return False
    return True