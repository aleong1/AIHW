''' Layout positions:
0 1 2
3 4 5
6 7 8
'''
# layouts look like "_x_ox__o_"

Wins = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]

xWins = 0
oWins = 0
draws = 0
notEnds = 0

AllBoards = {} # this is a dictionary with key = a layout, and value = its corresponding BoardNode

class BoardNode:
    def __init__(self,layout):
        self.layout = layout
        self.endState = None # if this is a terminal board, endState == 'x' or 'o' for wins, of 'd' for draw, else None
        self.parents = [] # all layouts that can lead to this one, by one move
        self.children = [] # all layouts that can be reached with a single move

    def print_me(self):
        print ('layout:',self.layout, 'endState:',self.endState)
        print ('parents:',self.parents)
        print ('children:',self.children)

def CreateAllBoards(layout,parent):
    # recursive function to manufacture all BoardNode nodes and place them into the AllBoards dictionary
    node = BoardNode(layout)
    node.parents.append(parent)
    AllBoards[layout] = node

    if solved(layout) or layout.count("_") == 0:
        node.endState = layout
        return

    next = 'x'
    if layout.count('o') == layout.count('x'):   ##create the boards
        next = 'o'
    for pos in range(9):
        if layout[pos] == "_":
            nboard = layout[:pos] + next + layout[pos+1:]
            CreateAllBoards(nboard, node.parents)
            node.children.append(node)


def solved(board):
    for win in Wins:
        if board[win[0]] == board[win[1]] and board[win[1]] == board[win[2]] and board[win[0]] != '_':  #if board is not empty
                return True
    return False

def countChildren():
    sumChildren = 0
    for k in AllBoards:
        sumChildren += len(AllBoards[k].children)
    print (sumChildren)

def whichWin():
    global xWins, oWins, draws

    for board in AllBoards.keys():
        for win in Wins:
            if board[win[0]] == board[win[1]] and board[win[1]] == board[win[2]] and board[win[0]] != '_':  #if there's a win
                if board[win[0]] == 'x':
                    oWins += 1
                if board[win[0]] == 'o':
                    xWins += 1
                break
        if board.count('_') == 0 and (board[win[0]] != board[win[1]] or board[win[1]] != board[win[2]]):
            draws += 1



CreateAllBoards('_________',None)
whichWin()
print(len(AllBoards))
print("children:")
countChildren()
print("x wins:")
print(xWins)
print("o wins:")
print(oWins)
print("draws:")
print(draws)
print("not ends:")
print(len(AllBoards)-xWins-oWins-draws)
