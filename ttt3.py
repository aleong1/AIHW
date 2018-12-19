import random

''' Layout positions:
0 1 2
3 4 5
6 7 8
'''
# Best future states according to the player viewing this board
ST_X = 1  # X wins
ST_O = 2  # O wins
ST_D = 3  # Draw

Wins = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]

AllBoards = {}   # This is primarily for debugging: key = layout, value = BoardNode

class BoardNode:

    def __init__(self, layout):
        self.layout = layout
        self.mover = 'x' if layout.count('x') == layout.count('o') else 'o'

        self.state = this_state(layout) # if final board, then ST_X, ST_O or ST_D, else None
        if self.state is None:
            self.best_final_state = None           # best achievable future state: ST_X, ST_O or ST_D
            self.best_move = None                  # 0-9 to achieve best state
            self.num_moves_to_final_state = None   # number of moves to best state
        else:
            self.best_final_state = self.state
            self.best_move = -1
            self.num_moves_to_final_state = 0

        self.children = set()

    def print_me(self):
        print('layout:',self.layout)
        print('mover:',self.mover)
        print('state:',str_state(self.state))
        print('best_final_state:',str_state(self.best_final_state))
        print('best_move:',self.best_move,BoardNode.str_move(self.best_move))
        print('num_moves_to_final_state:',self.num_moves_to_final_state)

    def print_layout(self):
        print('%s\n%s\n%s' % (' '.join(self.layout[0:3]),' '.join(self.layout[3:6]),' '.join(self.layout[6:9])))

    # =================== class methods  =======================
    def str_move(move):
        # human description of a move
        moves = ('top-left','top-center','top-right',\
                 'middle-left','middle-center','middle-right',\
                 'bottom-left','bottom-center','bottom-right')
        return 'done' if move == -1 else moves[move]

def str_state(state):
    # human description of a state
    return 'None' if state is None else ['x-wins','o-wins','draw'][state-1]

def this_state(layout):
    # classifies this layout as None if not final, otherwise ST_X or ST_O or ST_D
    for awin in Wins:
        if layout[awin[0]] != '_' and layout[awin[0]] == layout[awin[1]] == layout[awin[2]]:
            return ST_X if layout[awin[0]] == 'x' else ST_O
    if layout.count('_') == 0:
        return ST_D
    return None

def CreateAllBoards(layout):
     # Populate AllBoards with finally calculated BoardNodes

    if layout in AllBoards:
        return

    anode = BoardNode(layout)
    # if this is an end board, then all of its properties have already be calculated by __init__()
    if anode.state is not None:
        AllBoards[layout] = anode
        return

    # expand children if this is not a final state
    move = 'x' if layout.count('x') == layout.count('o') else 'o'
    for pos in range(9):
        if layout[pos] == '_':
            new_layout = layout[:pos] + move + layout[pos+1:]
            if new_layout not in AllBoards:
                CreateAllBoards(new_layout)
            anode.children.add(new_layout)

    # ==============================================================================
    # Your excellent code here to calculate the BoardNode properties below for this node
    #   best_move
    #   best_final_state
    #   num_moves_to_final_state
    # ==============================================================================

    def NodeProp(node, numMoves):
        if node.layout.count("_") == 9:
            node.best_final_state = ST_D
            node.num_moves_to_final_state = 9
            node.best_move = 0
            return

        if node.layout.count("_") == 0 or node.state is not None:
            node.best_final_state = this_state(node.layout)
            node.num_moves_to_final_state = numMoves
            node.best_move = None
            return

        for childNode in node.children:
            NodeProp(AllBoards[childNode], numMoves)
            numMoves += 1

            AllBoards[childNode].num_moves_to_final_state = numMoves
            AllBoards[childNode].state = this_state(childNode)

            posMoves = dict()
            opMoves = dict()
            if str_state(AllBoards[childNode].best_final_state) == "ST_" + move:
                if (AllBoards[childNode].num_moves_to_final_state) not in posMoves:
                    posMoves[(AllBoards[childNode].num_moves_to_final_state)] = list()
                posMoves[(AllBoards[childNode].num_moves_to_final_state)].append(AllBoards[childNode])
            else:
                if (AllBoards[childNode].num_moves_to_final_state) not in opMoves:
                    opMoves[(AllBoards[childNode].num_moves_to_final_state)] = list()
                opMoves[(AllBoards[childNode].num_moves_to_final_state)].append(AllBoards[childNode])

            sorted(posMoves)
            sorted(opMoves, reverse=True)

            bestNode = anode
            posKeys = list(posMoves.keys())
            if len(posKeys) >= 1:
                if len(posMoves[posKeys[0]]) >= 1:
                    bestNode = random.choice(posMoves[posKeys[0]])
                    node.best_final_state = bestNode.best_final_state
                    node.num_moves_to_final_state = posKeys[0]
                    for a in range(9):   #find the next move
                        if bestNode.layout[a] != node.layout[a]:
                            node.best_move = a
            else:
                opKeys = list(opMoves.keys())
                if len(opKeys) >= 1:
                    if len(opMoves[opKeys[0]]) >= 1:
                        bestNode = random.choice(opMoves[opKeys[0]])
                        node.best_final_state = bestNode.best_final_state
                        node.num_moves_to_final_state = opKeys[0]
                        for a in range(9):   #find the next move
                            if bestNode.layout[a] != node.layout[a]:
                                node.best_move = a

    NodeProp(anode,0)
    AllBoards[layout] = anode


#  Test me here...

AllBoards = {}
print('x should win this one in 3 moves')
b='x_o_o___x'
CreateAllBoards(b)
AllBoards[b].print_me()
AllBoards[b].print_layout()

AllBoards = {}
b='x__xoxo__'
print('\no should win this one in 1 move')
CreateAllBoards(b)
AllBoards[b].print_me()
AllBoards[b].print_layout()

AllBoards = {}
b='_________'
print('\nthis should be a draw in 9 moves')
CreateAllBoards(b)
AllBoards[b].print_me()
AllBoards[b].print_layout()
