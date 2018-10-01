#! /usr/bin/python3

#Alexia Leong

import sys

class Pqueue():
  
  def __init__(self):
    self.queue = []
    
  def push(self, data):
    
    def compare(a,b):
      if len(self.queue[a]) < len(self.queue[b]): return -1
      if len(self.queue[a]) == len(self.queue[b]): return 0
      return 1
    
    def swap(a,b):
      temp = self.queue[a]
      self.queue[a] = self.queue[b]
      self.queue[b] = temp
    
    self.queue.append(data)   #add to queue at the end
    newPos = len(self.queue) - 1
    
    while newPos > 0:
      parentPos = int((newPos-1)/2)
      
      if compare(newPos, parentPos)< 0:  #if data is shorter than its parent
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
        
        if pos == 0 or pos >= len(self.queue) or left >= len(self.queue):
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
        minChild = minChild(pos)
        
        if minChild == -1: break  #if no children
        elif last <= self.queue[minChild]: break # if <= child
        else:
            temp = self.queue[pos]
            self.queue[pos] = self.queue[minChild]
            self.queue[minChild] = temp
            pos = minChild
            
    return retVal
  
    
  def tolist(self):
    if len(self.queue) == 0:
      return []
    
    ret = []
    while self.peek():
      ret.append(self.pop())
    
    return ret

  def main():
    inputed = sys.argv[1]  #input file
    output = sys.argv[2]  #output file

    inputFile = open(inputed,'r')   #read inputfile
    inputLines = inputFile.read().split('\n')  #spilt it into lines
    inputFile.close()

    outputLines = open(output, 'w')

    for line in range(len(inputLines)):  #traverse file
      temp = inputLines[line].split(',')
      
      for a in range(len(temp)):  #traverse line
        element = temp[a].strip()   #for each element in line
        

"""
uh = Pqueue()
uh.push([1,2,3,4,5,6,7])
uh.push(["bop","bop","bop"])
uh.push(["ya"])

print (uh.peek())  #should be [ya]
print (uh.pop())  #should be [ya]
print (uh.pop())  #should be ["bop","bop","bop"]
print (uh.tolist()) #should be [[1,2,3,4,5,6,7]]
print (uh.tolist()) #should be []
print (uh.pop())  #should be None
print (uh.peek())  #should be None
"""
