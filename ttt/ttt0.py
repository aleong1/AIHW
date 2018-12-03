
Games = 0
allBoards = set()

def tttSolver(board):
    global Games
    allBoards.add(board)

    if solved(board) or board.count("_") == 0:
        Games += 1
        return

    next = 'x'
    if board.count('o') == board.count('x'):
        next = 'o'
    for pos in range(9):
        if board[pos] == "_":
            nboard = board[:pos] + next + board[pos+1:]
            tttSolver(nboard)


Wins = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
def solved(board):
    for win in Wins:
        if board[win[0]] == board[win[1]] and board[win[1]] == board[win[2]] and board[win[0]] != '_':  #if board is not empty
            return True
    return False


emptyBoard = "_________"
tttSolver(emptyBoard)
print (Games)
print(len(allBoards))
