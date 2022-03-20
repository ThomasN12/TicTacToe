board = [' ' for i in range(10)]

#insert 'O' or 'X' to pos
def insertLetter(letter, pos):
    board[pos] = letter

# Check if board[pos] is free or not
def spaceisFree(pos):
    return board[pos] == ' '        #" " and ' '

def printBoard(board):
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' +board[3])
    print('   |   |')
    print('----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' +board[6])
    print('   |   |')
    print('----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' +board[9])
    print('   |   |')
    print('----------')


def isWinner(bo, le):
    return (bo[1] == bo[2] == bo[3] == le) or (bo[4] == bo[5] == bo[6] == le) or (bo[1] == bo[4] == bo[7] == le) or (bo[2] == bo[5] == bo[8] == le) or (bo[3] == bo[6] == bo[9] == le) or (bo[1] == bo[5] == bo[9] == le) or (bo[3] == bo[5] == bo[7] == le)

def playerMove():
    test = True
    while test:
        move = input('Please type your input: ')
        try:
            move = int(move)    #Convert string input to int
            if (move > 0 or move <= 9):
                if (spaceisFree(move)):
                    test = False
                    insertLetter('X', move)
                else:
                    print('Sorry, the spot is occupied')
            else:
                print('Please type a number in range')
        except:
            print('Please type a number')


def compMove():
    possibleMoves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]            #Important
    move = 0

    # Check if the new move will declare the WINNER
    for let in ('O','X'):
        for i in possibleMoves:
            boardCopy = board[:]  #Clone!!!
            boardCopy[i] = let
            if isWinner(boardCopy, let):
                move = i
                return move
    
    #Priority of bot moving: center, corners, and edges

    if 5 in possibleMoves:
        move = 5
        return move
    
    cornersOpen = []
    for i in possibleMoves:
        if i in [1,3,7,9]:
            cornersOpen.append(i)
    
    if len(cornersOpen) > 0:
        move = selectRandom(cornersOpen)
        return move
    
    
    edgesOpen = []
    for i in possibleMoves:
        if i in [2,4,6,8]:
            edgesOpen.append(i)
    
    if len(edgesOpen) > 0:
        move = selectRandom(edgesOpen)
        return move
    return move
    

def selectRandom(li):
    import random
    ln = len(li)
    r = random.randrange(0, ln)     #return a random number between 0 and ln-1
    return li[r]

def isBoardFull(board):     #Double-check
    if board.count(' ') > 1:
        return False
    else:
        return True


def main():
    test = True
    print('Please type your name:')
    n = input()
    print('Hi,' + n + '. Welcome to Tic-Tac-Toe')

    while (not isBoardFull(board)):
        if not isWinner(board, 'O'):
            playerMove()
            printBoard(board)
        else:
            print('That \'s\' close! Do you want to try again?')
            break
        
        if not isWinner(board, 'X'):
            move = compMove()  
            if move == 0:
                print('Tie game')
                test = False
                break
            else:
                insertLetter('O', move)    
                print('Computer placed an \'O\' in position', move, ':')
                printBoard(board)
        else:
            print('Congratulations! You are the most intelligent in the world!!!')
            break
    
    if (isBoardFull(board) and test):
        print("Tie game")

main()
while True: # Why while True? Because continue to request play again until the answer is No
    answer = input('Do you want to play again? (Y/N)')
    if answer.lower() == 'y' or answer.lower == 'yes':
        board = [' ' for x in range(10)]    # if 'yes', reset the board
        print('-----------------------------------')
        main()  # if 'yes', re-perform main
    else:
        break