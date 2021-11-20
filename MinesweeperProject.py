# Creating MineSweeper Grid Layout 
def mine_grid():
    global mine_values
    global n 

    print()
    print("MineSweeper")

    st = "   "
    for i in range(n):
        st = st + "     " + str(i + 1)
    print(st)   
 
    for r in range(n):
        st = "     "
        if r == 0:
            for col in range(n):
                st = st + "______" 
            print(st)