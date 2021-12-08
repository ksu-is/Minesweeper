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

def ContinueGame(score):
    print("Your score: ", score)
    isContinue = input("Try again? (y/n) :")
    if isContinue == 'n':
        return False
    return True
def Game():
    GameStatus = True
    while GameStatus:
        difficulty = input("Select difficulty (e, h):")
        if difficulty.lower() == 'e':
            a = 5
            z = 3
        else:
            a = 8
            z = 20
        
        minesweeper_map = MakeMines(a, z)
        player_map = GenerateMap(a)
        score = 0
        while True:
            if WinCheck(player_map) == False:
                print("Enter the block you want to open:")
                x = input("X (1 to 5) :")
                y = input("Y (1 to 5) :")
                x = int(x) - 1 # 0 based indexing
                y = int(y) - 1 # 0 based indexing
                if (minesweeper_map[y][x] == 'X'):
                    print("Game Over!")
                    OpenMap(minesweeper_map)
                    GameStatus = ContinueGame(score)
                    break
                else:
                    player_map[y][x] = minesweeper_map[y][x]
                    OpenMap(player_map)
                    score += 1
 
            else:
                OpenMap(player_map)
                print("Congratulations! You have Won!")
                GameStatus = ContinueGame(score)
                break
# Opening the Minesweeper Program
if __name__ == "__main__":
    try:
        Game()
    except KeyboardInterrupt:
        print('\nThe Concludes the Game. Bye!')