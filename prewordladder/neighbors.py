#! /usr/bin/python3
import sys

fin = open('dictall.txt','r')
finLines = fin.read().split('\n')

inputFile = open(sys.argv[1], 'r')
inputLines = inputFile.read().split('\n')
inputFile.close()

outputFile = open(sys.argv[2], 'w')

dictionary = dict()
lenWords = list()

def simLength(input):
    length = len(input)
    for word in finLines:  #for each word in long list of words
        if len(word) == length:  #for same length words
            makeNeighbors(word)

def makeNeighbors(key):
    neighbors = list()
    for word in finLines:  #for each word in long list of words
        if len(word) == len(key):  #same length
            similar = 0
            for character in range(len(key)):  #character in the word from inputFile
                if key[character] == word[character]:
                    similar += 1
            if similar == len(word) - 1:
                neighbors.append(word)
    dictionary[key] = neighbors

for line in inputLines:    #for each word in inputFile
    if not dict() or len(line) not in lenWords:  #if dictionary is empty or word is a new length
        simLength(line)
        lenWords.append(len(line))   #put already used lengths in a list
    outputFile.write(line + "," + str(len(dictionary[line])) + '\n')

fin.close()
outputFile.close()
