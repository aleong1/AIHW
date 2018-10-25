#! /usr/bin/python3
import sys

fin = open('dictall.txt','r')
finLines = fin.read().split('\n')

inputFile = open(sys.argv[1], 'r')
inputWords = inputFile.read().strip().split('\n')
inputFile.close()
outputFile = open(sys.argv[2], 'w')

alphabet = list(map(chr, range(97, 123))) #list of all lowercase letters
pastLengths = list()
dictionary = dict()

for original in inputWords:   #words in inputFile
    wordLength = len(original)
    if wordLength not in pastLengths:   #if this is a new length word
        pastLengths.append(wordLength)
        sameLength = [x for x in finLines if len(x) == wordLength]
        setWords = set(sameLength)
        for word in sameLength:
            neighbors = list()
            for character in range(len(word)):
                for letter in alphabet:
                    if letter != word[character]:
                        newWord = word[:character] + letter + word[character + 1:]
                        if newWord in setWords:
                            neighbors.append(newWord)
                dictionary[word] = neighbors

    outputFile.write(original + "," + str(len(dictionary[original])) + '\n')

fin.close()
outputFile.close()
