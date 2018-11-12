#! /usr/bin/python3
import sys

allBoards = open(sys.argv[1], "r")
boards = allBoards.read().strip().split()
outputFile = open(sys.argv[2], "w")
name = sys.argv[3]

board = list()
for a in boards:
    board.append(a.split())

ctr = 0
sudoku = list()    #board to play with
while ctr < len(board):
    if board[ctr][0] == name:
        line = ctr + 1
        while line < (ctr + 10):
            sudoku += board[line][0].split(',')
            line += 1
    ctr += 10

#rows --> columns -->  cells
Cliques=[[0,1,2,3,4,5,6,7,8],\
[9,10,11,12,13,14,15,16,17],\
[18,19,20,21,22,23,24,25,26],\
[27,28,29,30,31,32,33,34,35],\
[36,37,38,39,40,41,42,43,44],\
[45,46,47,48,49,50,51,52,53],\
[54,55,56,57,58,59,60,61,62],\
[63,64,65,66,67,68,69,70,71],\
[72,73,74,75,76,77,78,79,80,],\
[0,9,18,27,36,45,54,63,72],\
[1,10,19,28,37,46,55,64,73],\
[2,11,20,29,38,47,56,65,74],\
[3,12,21,30,39,48,57,66,75],\
[4,13,22,31,40,49,58,67,76],\
[5,14,23,32,41,50,59,68,77],\
[6,15,24,33,42,51,60,69,78],\
[7,16,25,34,43,52,61,70,79],\
[8,17,26,35,44,53,62,71,80],\
[0,1,2,9,10,11,18,19,20],\
[3,4,5,12,13,14,21,22,23],\
[6,7,8,15,16,17,24,25,26],\
[27,28,29,36,37,38,45,46,47],\
[30,31,32,39,40,41,48,49,50],\
[33,34,35,42,43,44,51,52,53],\
[54,55,56,63,64,65,72,73,74],\
[57,58,59,66,67,68,75,76,77],\
[60,61,62,69,70,71,78,79,80]]

#dict for keys and neighbors
#key is pos in sudoku board,value is all the nums it could be in Cliques
nb = dict()
ctr = 0
while ctr < 81:    #numbering of cells from 0 --> 80
    nbs = set()
    for line in Cliques:
        if ctr in line:
            for num in line:
                nbs.add(num)
    nb[ctr] = nbs
    ctr += 1

#helper fxn to get actual nums from sudoku board using dict from cliques:
def helperCliques(pos):
    noGood = set()
    for num in nb[pos]:
        if sudoku[num] != '_':
            noGood.add(sudoku[num])
    return noGood

#recursive fxn
def sudokuSolver(pos, backtracks):
    if pos > 80:
        print(backtracks)
        return True
    if sudoku[pos] != '_':    #if not empty
        return sudokuSolver(pos + 1, backtracks + 1)

    for possibility in range(1,10):
        used = helperCliques(pos)
        if str(possibility) not in used:
            sudoku[pos] = str(possibility)

            #continue w/ recursion
            if sudokuSolver(pos + 1, backtracks):
                return True

            #no guesses worked
            sudoku[pos] = '_'
            backtracks += 1

    #backtrack again
    backtracks += 1
    return False

sudokuSolver(0,0)
ret = ''
for num in range(81):
    #make rows
    if (num+1)%9 == 0:
        ret += sudoku[num] + '\n'
    else:
        ret += sudoku[num] + ','

outputFile.write(name[:-8] + 'solved\n' + ret)
