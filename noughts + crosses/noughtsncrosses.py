board = [
    ['.','.','.'],
    ['.','.','.'],
    ['.','.','.']
]


def printBoard(): # <-- prints the board at the start of the game and after every move
    print(board[0][0] + board[0][1] + board[0][2])
    print(board[1][0] + board[1][1] + board[1][2])
    print(board[2][0] + board[2][1] + board[2][2])

    move()

player = random.randint(1,2)

def move():
    print(f"it is player {player}'s turn")
    
    row = -1 # using both of these to verify if the value is actually changed
    column = -1

    r = int(input('what row [0,1,2]'))
    c = int(input('what column [0,1,2]'))

    if board[r][c] == '.': # <-- if empty
        row = r
        column = c
        if player == 1:
            board[row][column] = 'x'
            player = 2
            printBoard()
        else:
            board[row][column] = 'o'
            player = 1
            printBoard()
        

printBoard()
         

