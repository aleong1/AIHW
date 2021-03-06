#! /usr/bin/python3
import sys

class PQueue:    #mr.brook's
    def __init__(self, is_min=True, compare=None, startlist=[]):
        self.size = 0
        self.datalist = [0]
        self.is_min = is_min

        if compare is not None:
            self.compare = compare
        else:
            self.compare = self._normal_cmp

        for element in startlist:
            self.push(element)


    def push(self,data):
        # if there's empty room at the end of the datalist (from previous pops), put it there, otherwise append it
        if len(self.datalist) <= self.size + 1:
            self.datalist.append(data)
        else:
            self.datalist[self.size + 1] = data
        self.size += 1

        # Bubble up from the data's current position
        self._bubble_up(self.size)

    def pop(self):
        if self.size == 0:
            return None

        if self.size == 1:
            self.size = 0
            return self.datalist[1]

        # save the answer
        answer = self.datalist[1]
        # Move last into root and bubble down from the top (position = 1)
        self.datalist[1] = self.datalist[self.size]
        self.size -= 1
        self._bubble_down(1)

        return answer

    def peek(self):
        # returns root
        if self.size== 0:
            return None
        return self.datalist[1]

    def size(self):
        return self.size

    def to_list(self):
        answer = []
        while True:
            best = self.pop()
            if best is not None:
                answer.append(best)
            else:
                return answer

    # This is the default comparison function
    def _normal_cmp(self,a,b):
        if a < b: return -1
        if a > b: return 1
        return 0

    def _swap(self,pos1,pos2):
        # swapper
        temp = self.datalist[pos1]
        self.datalist[pos1] = self.datalist[pos2]
        self.datalist[pos2] = temp

    def _bubble_up(self,position):
        # bubble up from the position if necessary
        child = position
        parent = position // 2
        while parent > 0:
            result = self.compare(self.datalist[child],self.datalist[parent])
            if self.is_min and result == -1:  # it's a min-queue and child is smaller than parent
                self._swap(parent,child)
            elif not self.is_min and result == 1:  # it's a max-queue and child is larger than parent
                self._swap(parent,child)
            else:
                break
            child = parent
            parent = child // 2

    def _bubble_down(self, position):
        # bubble down from position if necessary
        parent = position
        while True:
            left_child = parent * 2
            if left_child > self.size:
                return
            result_left = self.compare(self.datalist[left_child],self.datalist[parent])

            right_child = left_child + 1
            if right_child > self.size:
                # there's only the left child
                if self.is_min and result_left == -1:  # it's a min-queue and child is smaller than parent
                    self._swap(parent,left_child)
                elif not self.is_min and result_left == 1:  # it's a max-queue and child is larger than parent
                    self._swap(parent,left_child)
                else:
                    return
                parent = left_child
                continue

            # both children exist
            result_right = self.compare(self.datalist[right_child],self.datalist[parent])

            # decide which child to swap with, if we do end up swapping
            result_left_right = self.compare(self.datalist[left_child],self.datalist[right_child])
            if result_left_right == 0:
                swap_with = left_child # by convention
            elif self.is_min:
                if result_left_right == -1:  # it's a min_queue and left_child is smaller
                    swap_with = left_child
                else:                        # it's a min-queue and right_child is smaller
                    swap_with = right_child
            else:
                if result_left_right == -1:  # it's a max-queue and left_child is smaller
                    swap_with = right_child
                else:                        # it's a max-queue and right_child is smaller
                    swap_with = left_child

            # now compare the parent with the child we may swap with
            result_swap = self.compare(self.datalist[swap_with],self.datalist[parent])
            if self.is_min and result_swap == -1:  # it's a min-queue and child is smaller
                self._swap(swap_with,parent)
            elif not self.is_min and result_swap == 1:  # it's a max-queue and child is larger
                self._swap(swap_with,parent)
            else:
                return
            parent = swap_with


def compare(a,b):  #new compare fxn
    if a.value < b.value: return -1
    elif a.value == b.value: return 0
    return 1

class Node:
    def __init__(self, name):
        self.name = name
        self.value = 1
        self.path = name

fin = open('dictall.txt','r')
finLines = fin.read().split('\n')
inputFile = open(sys.argv[1], 'r')
inputLines = inputFile.read().strip().split('\n')
inputFile.close()
outputFile = open(sys.argv[2], 'w')

alphabet = list(map(chr, range(97, 123))) #list of all lowercase letters
dictionary = dict()

def makeDictionary(length):
    wordLength = length
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
    return dictionary

def distance(word, end):
    dif = 0
    for char in range(len(word)):
        if word[char] != end[char]:
            dif += 1
    return dif

def WordLadder(start, target):
    explored = set()
    frontier = PQueue(True, compare, [])
    frontier.push(Node(start))

    while frontier.peek() != None:
        temp = frontier.pop()
        if temp.name in explored:
            continue

        if temp.name == target:
            return temp.path

        #find neighbors
        listKey = dictionary[temp.name]
        for neighbor in listKey:
            newNode = Node(neighbor)
            newNode.path = temp.path + ',' + neighbor
            newNode.value = temp.value +  distance(neighbor, temp.name)
            frontier.push(newNode)

        explored.add(temp.name)

    return start + ',' + target

makeDictionary(len(list(inputLines[0].strip().split(','))[0]))
for lines in inputLines:
    Llines = list(lines.strip().split(','))
    outputFile.write(str((WordLadder(Llines[0], Llines[1]))) + '\n')
fin.close()
outputFile.close()
