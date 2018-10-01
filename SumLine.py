# Alexia Leong
# SumLine

#! /usr/bin/python3
import sys

def main():
    inputed = sys.argv[1]
    output = sys.argv[2]

    inputFile = open(inputed,'r')
    inputLines = inputFile.read().split('\n')
    inputFile.close()

    outputLines = open(output, 'w')

    for line in range(len(inputLines)):  #traverse file
        temp = inputLines[line].split(',') 
        sum = 0

        for a in range(len(temp)):  #traverse list
            element = temp[a].strip()   #for each element in line
            if element.isdigit() and int(element) > 0:   #to add + ints only
                sum += int(element)

        if sum > 0:
            outputLines.write(str(sum) + '\n')

    outputLines.close()

main()
