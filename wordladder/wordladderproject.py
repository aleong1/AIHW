#! /usr/bin/python3
import sys
import csv

inputFile = open(sys.argv[1], 'r')
inputLines = inputFile.read().strip().split('\n')
inputFile.close()
outputFile = open(sys.argv[2], 'w')

for a in inputLines:
    count = 0
    for word in a[2]:
        count += 1

    outputFile.write(str(a[0]), str(a[1]), str(a[2]), str(count))
