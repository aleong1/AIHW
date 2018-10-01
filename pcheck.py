#! /usr/bin/python3

#Alexia Leong

import sys

class Pqueue():
  
  def __init__(self):
    self.queue = []
    
  def push(self, data):
    
    def compare(a,b):
      if a < b: return -1
      if a == b: return 0
      return 1
    
    def swap(a,b):
      temp = self.queue[a]
      self.queue[a] = self.queue[b]
      self.queue[b] = temp
    
    self.queue.append(data)   #add to queue at the end
    newPos = len(self.queue) - 1
    
    while newPos > 0:
      parentPos = int((newPos-1)/2)
      
      if compare(self.queue[newPos],self.queue[parentPos])< 0:  #if data is shorter than its parent
        swap(newPos, parentPos)
        newPos = parentPos  # keep comparing with parent
        
      else:
        break

      
  def peek(self):
    if len(self.queue) == 0:
      return None
    else:
      return self.queue[0]
  
    
  def pop(self):
      
    def minChild(pos):
        left = 2 * pos + 1
        right = 2 * pos + 2
        ret = 0
        
        if pos >= len(self.queue) or left >= len(self.queue):
            ret = -1   
        elif right >= len(self.queue):  #if no right child
            ret = left
        elif self.queue[left] < self.queue[right]:
            ret = left
        else:
            ret = right
        return ret
    
    if len(self.queue) == 0:
      return None
    
    retVal = self.peek()    #to be returned at end
    last = len(self.queue) - 1  #smallest child
    
    self.queue[0] = self.queue[last] 
    self.queue.pop(last)
    
    #bubble root down
    pos = 0
    
    while pos < len(self.queue):
        minSpot = minChild(pos)
        
        if minSpot == -1: break  #if no children
        elif self.queue[last-1] <= self.queue[minSpot]: break # if <= child
        else:
            temp = self.queue[pos]
            self.queue[pos] = self.queue[minSpot]
            self.queue[minSpot] = temp
            pos = minSpot
            
    return retVal
  
    
  def tolist(self):  
    ret = []
    for a in range(len(self.queue)):
        ret.append(self.pop())
    return ret

  def pcheck(self, input, output):
    inputFile = open(input,'r')   #read inputfile
    inputLines = inputFile.read().split('\n')  #spilt it into lines
    inputFile.close()

    outputLines = open(output, 'w')

    for line in range(len(inputLines)):  #traverse file
      temp = inputLines[line].split(',')
      
      if temp[0] == 'push':   #check first word of line for command
        for a in range(1, len(temp)):  #traverse for push method
          self.push(int(temp[a]))
            
      elif temp[0] == 'peek':
        outputLines.write(str(self.peek()) + '\n')

      elif temp[0] == 'pop':
        outputLines.write(str(self.pop()) + '\n')

      elif temp[0] == 'tolist':
        outputLines.write(str(self.tolist()) + '\n')

    outputLines.close()
          
def main():
  queue = Pqueue()
  queue.pcheck(sys.argv[1], sys.argv[2])

  
main()
