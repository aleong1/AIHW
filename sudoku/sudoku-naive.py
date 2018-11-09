#! /usr/bin/python3
import sys

allBoards = open(sys.argv[1], "r")
boards = allBoards.strip().split()
outputFile = open(sys.argv[2], "w")
name = sys.argv[3]

board = list()

for a in boards:
    board.append(a.split("\n")
