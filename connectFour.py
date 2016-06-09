#connect-four

import pickle

def make_board(board, rows, cols):
    for i in range(rows):
        board.append([])
        for j in range(cols):
            board[i].append(0)
    return board

def print_board():
    line = ""
    for i in range(len(gameboard)):
        for j in range(len(gameboard[i])):
            line = line + str(gameboard[i][j]) + " "
        print line
        line = ""
    return

def play_column(col, token):
    for i in range(len(gameboard)):
        try:
            if gameboard[i+1][col-1] != 0:
                break
        except IndexError:
            break
        
    gameboard[i][col-1] = token


def swap_player():
    global currentPlayer
    print""
    if currentPlayer == 1:
        print "PLAYER 2's TURN"
        currentPlayer = 2
        
    elif currentPlayer == 2:
        print "PLAYER 1's TURN"
        currentPlayer = 1

#winning conditions
def check():
    for i in range(noOfRows-3):#checks for vertical win
        for j in range(noOfColumns):
            if gameboard[i][j] == currentPlayer and gameboard[i + 1][j] == currentPlayer and gameboard[i+2][j] == currentPlayer and gameboard[i+3][j] == currentPlayer:
                return True
    for i in range(noOfRows):#checks for horizontal win
        for j in range(noOfColumns-3):
            if gameboard[i][j] == currentPlayer and gameboard[i][j+1] == currentPlayer and gameboard[i][j+2] == currentPlayer and gameboard[i][j+3] == currentPlayer:
                return True
    for i in range(noOfRows-3):
        for j in range(noOfColumns-3):#checks for diagonal: NW - SE
            if gameboard[i][j] == currentPlayer and gameboard[i+1][j+1] == currentPlayer and gameboard[i+2][j+2] == currentPlayer and gameboard[i+3][j+3] == currentPlayer:
                return True
    for i in range(noOfRows-3):
        for j in range(3, noOfColumns):#checks for diagonal: NE - SW
            if gameboard[i][j] == currentPlayer and gameboard[i+1][j-1] == currentPlayer and gameboard[i+2][j-2] == currentPlayer and gameboard[i+3][j-3] == currentPlayer:
                return True

def save():
    f = open("save game.txt", "w")
    pickle.dump(gameboard, f)#preserves structure of game.
    f.close
    print "GAME SAVED"
    print""

def load():
    global gameboard
    f = open("save game.txt", "r")
    gameboard = pickle.load(f)
    f.close
    print "GAME LOADED"
    print_board()

noOfRows = int(raw_input("rows "))
noOfColumns = int(raw_input("columns "))

gameboard = []
currentPlayer = 1

gameboard = make_board(gameboard, noOfRows, noOfColumns)


print "PLAYER 1 STARTS"
print "at any point of the game press 's' to save or 'l' to load game."
print_board()

while True:
    
    x = raw_input("play column: ")
    if x == "s":
        save()
        continue

    elif x == "l":
        load()
        continue

    
    else:
        x = int(x) #expects board columns rather than save or load.
        play_column(x, currentPlayer)
        print_board()
        if check():
            print "You won the game!"
            break
        swap_player()


