from random import randint

board = [
    ['.','.','.'],
    ['.','.','.'],
    ['.','.','.']
]

player = randint(1,2)
moves = 0

def move():
    global moves
    global player
    print(f"it is player {player}'s turn")
    
    row = -1 # using both of these to verify if the value is actually changed
    column = -1

    r = int(input('what row [0,1,2]: '))
    c = int(input('what column [0,1,2]: '))

    if board[r][c] == '.': # <-- if empty
        row = r
        column = c
        if player == 1:
            board[row][column] = 'x'
            winCon()
            draw()
            whoWon()
            moves += 1
            player = 2
            printBoard()
        else:
            board[row][column] = 'o'
            winCon()
            draw()
            whoWon()
            moves += 1
            player = 1
            printBoard()

def draw():
    if moves == 9:
        print('the game is a draw!\nnobody won!')
        quit()

def printBoard():
    print(board[0][0] + ' ' + board[0][1] + ' ' + board[0][2])
    print(board[1][0] + ' ' + board[1][1] + ' ' + board[1][2])
    print(board[2][0] + ' ' + board[2][1] + ' ' + board[2][2])

    if winCon() == True:
        quit()
    move()

def winCon():
    for i in range (0,3):
        if (board[i][0] == board[i][1] and board[i][2] != '.'): # rows
            return True
            
        elif (board[0][i] == board[1][i] and board[2][i] != '.'): # columns
            return True
            
    
    # diagonals

    if (board[0][0] == board[1][1] and board[2][2] != '.'): 
        return True
        
    elif (board[0][2] == board[1][1] and board[2][0] != '.'):
        return True
    
    else:
        return False
        
    
 # <-- if nobody has won

def whoWon():
    if winCon() == True:
        if player == 1:
            print('player 1 wins')
        else:
            print('player 2 wins')

printBoard()