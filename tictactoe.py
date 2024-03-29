#tic tac toe
import random
def drawBoard(board):
    #this function prints out the board that was passed
    #board is a list of strings
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[1] + '|' + board[2] + '|' + board[3])

def inputPlayerLetter():
    #take player input
    # returns list with players letter as the first item and computer's as second item
    letter = ''
    while not(letter == 'X' or letter == 'O'):
        print('Do you want to be X or O')
        letter = input().upper()

        #the first element in th elist is players letter; second is computers letter

        if letter == 'X':
            return['X', 'O']
        else:
            print('Automatically assigning O to you')
            return['O', 'X']

def whoGoesFirst():
    #randomly picks who goes first
    if random.randint(0,1) == 0:
        return 'computer'
    else:
        return 'player'



def makeMove(board, letter, move):
    #Randomly choose who goes first
    board[move] = letter

def isWinner(bo, le):
    # Given a board and a player letter, this function returns true if that player has won.
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or
    (bo[4] == le and bo[5] == le and bo[6] == le) or
    (bo[1] == le and bo[2] == le and bo[3] == le) or
    (bo[7] == le and bo[4] == le and bo[1] == le) or
    (bo[8] == le and bo[5] == le and bo[2] == le) or
    (bo[9] == le and bo[6] == le and bo[3] == le) or
    (bo[7] == le and bo[5] == le and bo[3] == le) or
    (bo[9] == le and bo[5] == le and bo[1] == le))

def getBoardCopy(board):
    #make a copy of the board list and return it
    boardCopy = []
    for i in board:
        boardCopy.append(i)
    return boardCopy

def isSpaceFree(board, move):
    #return ture i the passed move is free on the passed board
    return board[move] == ' '

def getPlayerMove(board):
    #let player enter move
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        print('What is your next move? (1-9) ')
        move = input()
    return int(move)

def chooseRandomMoveFromList(board, moveList):
    # turenrs a valid move from the passed list on the passed board
    # returns none if there is no valid move
    possibleMoves = []
    for i in moveList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)
    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None

def getComputerMove(board, computerLetter):
    # given a board and the computer letter, determine where to move and return that move
    if computerLetter == 'X':
        playerLetter == 'O'
    else:
        playerLetter == 'X'

    for i in range(1, 10):
        boardCopy = getBoardCopy(board)
        if isSpaceFree(boardCopy, i):
            makeMove(boardCopy, playerLetter, i)
            if isWinner(boardCopy, computerLetter):
                return i

    for i in range(1, 10):
        boardCopy = getBoardCopy(board)
        if isSpaceFree(boardCopy, i):
            makeMove(boardCopy, playerLetter, i)
            if isWinner(boardCopy, playerLetter):
                return i

    move = chooseRandomMoveFromList(board, [1, 3, 7 ,9])
    if move != None:
        return move

    if isSpaceFree(board, 5):
        return 5

    return chooseRandomMoveFromList(board, [2, 4, 6 ,8])

def isBoardFull(board):
    for i in range(1, 10):
        if isSpaceFree(board, i):
            return False
    return True

while True:
    #reset the board
    theBoard = [' '] * 10
    playerLetter, computerletter = inputPlayerLetter()
    turn = whoGoesFirst()
    print('The ' + turn + ' will go first')
    gameIsPlaying = True

    while gameIsPlaying:
        if turn == 'player':
            #players turn
            drawBoard(theBoard)
            move = getPlayerMove(theBoard)
            makeMove(theBoard, playerLetter, move)

            if isWinner(theBoard, playerLetter):
                drawBoard(theBoard)
                print('You won')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('The game is a tie')
                    break
                else:
                    turn = 'computer'
        else:
            # computers turn
            move = getComputerMove(theBoard, computerletter)
            makeMove(theBoard, computerletter, move)

            if isWinner(theBoard, computerletter):
                drawBoard(theBoard)
                print('The computer has beaten you! You lose')
                gameIsPlaying = False

            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('The computer has beaten you, loser')
                    gameIsPlaying = False
                else:
                    if isBoardFull(theBoard):
                        drawBoard(theBoard)
                        print('The game is a tie')
                        break
                    else:
                        turn = 'player'

    print('Do you want to player again')
    if not input().lower().startswith('y')
        break

