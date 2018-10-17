#! /usr/bin/python3
import sys

def main():
    fin = open('dictall.txt','r')
    finLines = fin.read().split('\n')

    inputFile = open(sys.argv[1], 'r')
    inputLines = inputFile.read().split('\n')
    inputFile.close()

    outputFile = open(sys.argv[2], 'w')

    dictionary = dict()
    for line in inputLines:    #for each word in inputFile
        neighbors = list()
        for word in finLines:  #for each word in long list of words
            if len(word) == len(line):  #same length
                similar = 0
                for character in range(len(line)):  #character in the word from inputFile
                    if line[character] == word[character]:
                        similar += 1
                if similar == len(word) - 1:
                    neighbors.append(word)
        dictionary[line] = neighbors
        outputFile.write(line + "," + str(len(neighbors)) + '\n')
    fin.close()
    outputFile.close()

main()
