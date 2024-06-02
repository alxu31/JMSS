import random

#Finds the location of the blank square.
def find_location(board,x=0,y=0):
    for i in range(4):
        for j in range(4):
            if board[i][j] == "• ":
                x = j
                y = i
                return x, y

#Checks if the puzzle board is solvable.
def check_board(board,y):
    check = []
    for i in range(4):
        for j in range(4):
            check.append(board[i][j])
    if y % 2 == 0:
        if inversion_counter(check) % 2 == 1:
            #If the row the blank is in is even from the bottom and the inversion count is odd, the puzzle is solvable.
            return False
        
    if y % 2 == 1:
        if inversion_counter(check) % 2 == 0:
            #If the row the blank is in is odd from the bottom and the inversion count is even, the puzzle is solvable.
            return False
    #Otherwise the puzzle is not solvable.
    return True


#Counts the number of inversions on the puzzle board.
def inversion_counter(board):
    inversionCount = 0
    board.remove("• ")
    for i in range(15):
        for j in range(15):
            if j < 14-i:
                if int(board[14-i]) < int(board[j]):
                    inversionCount += 1
    return inversionCount

numbersList = ["1 ","2 ","3 ","4 ","5 ","6 ","7 ","8 ","9 ","10","11","12","13","14","15","• "]
correctBoard = [["1 ","2 ","3 ","4 "],["5 ","6 ","7 ","8 "],["9 ","10","11","12"],["13","14","15","• "]]
puzzleBoard = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
puzzleCheck = True
#Contines randomly generating the puzzle until a solvable one is created.
while puzzleCheck:
    random.shuffle(numbersList)
    z = 0
    for i in range(4):
        for j in range(4):
            puzzleBoard[i][j] = numbersList[z]
            z += 1
    location = find_location(puzzleBoard)
    y = location[1]
    puzzleCheck = check_board(puzzleBoard,y)
    


for i in range(4):
    print(" ".join(puzzleBoard[i]))

moveCount = 0
while True:
    #Asks the user which direction they want the blank space to move.
    nextMove = input("Which way would you like the blank space (circle) to move? (w,a,s,d) ")
    location = find_location(puzzleBoard)
    x = location[0]
    y = location[1]
    #Moves the blank space up.
    if nextMove == "w":
        if y != 0:
            dot = puzzleBoard[y][x]
            number = puzzleBoard[y-1][x]
            puzzleBoard[y-1][x] = dot
            puzzleBoard[y][x] = number
        else:
            print("Sorry that is not an option. Try again.")
    #Moves the blank space left.
    elif nextMove == "a":
        if x != 0:
            dot = puzzleBoard[y][x]
            number = puzzleBoard[y][x-1]
            puzzleBoard[y][x-1] = dot
            puzzleBoard[y][x] = number
        else:
            print("Sorry that is not an option. Try again.")
    #Moves the blank space down.
    elif nextMove == "s":
        if y != 3:
            dot = puzzleBoard[y][x]
            number = puzzleBoard[y+1][x]
            puzzleBoard[y+1][x] = dot
            puzzleBoard[y][x] = number
        else:
            print("Sorry that is not an option. Try again.")
    #Moves the blank space right.
    elif nextMove == "d":
        if x != 3:
            dot = puzzleBoard[y][x]
            number = puzzleBoard[y][x+1]
            puzzleBoard[y][x+1] = dot
            puzzleBoard[y][x] = number
        else:
            print("Sorry that is not an option. Try again.")
    else:
        print("Sorry that is not a valid move. Try again.")
    for i in range(4):
        print(" ".join(puzzleBoard[i]))
    moveCount += 1
    #Tells the user they won if the puzzle is complete.
    if puzzleBoard == correctBoard:
        print("Congratulations, you win!")
        print(f"It took you {moveCount} moves.")
        break
    


