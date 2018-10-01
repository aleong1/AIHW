class Node():

  def __init__(self, data):
    self.data = data
    self.left = None   #nodes
    self.right = None

  def value(self):
    return self.data

  def lvalue(self):
    return self.left

  def rvalue(self):
    return self.right


class BinTree():

  def __init__(self, A):
    self.root = Node(None)
    self.ltree =
    self.rtree =
    self.size = 0

    for i in A:
      self.insert(i)

  def insert(self, v):
    anode = Node(v)
    if self.size == 0:
      self.root = anode

    elif v < self.root.value():
      if self.root.left == None:  #if no left child
        self.root.left = anode
        self.ltree.root = self.root.left
      else:
        self.ltree.insert(v)   #recurse down left subtree

    else:
      if self.root.right == None:
        self.root.right = anode
        self.rtree.root = self.root.right
      else:
        self.rtree.insert(v)
    self.size += 1

  def has(self,v):
    if self.root:
      return False
    if self.root.value() == v:
      return True
    if v < self.root.value():
      self.ltree.has(v)
    else:
      self.rtree.has(v)

  def get_ordered_list(self):
    lout = []
    if self.left.root:
      lout.append(self.root.left.lvalue())
      self.left.get_ordered_list()
    if self.rtree.root:
      lout.append(self.root.right.rvalue())
      self.rtree.get_ordered_list()
    return lout

  def clear(self):   #postorder
    if self == None:
      return None
    self.ltree.clear()
    self.rtree.clear()


L = BinTree([1,1,1,7,2,7,3])
L.insert(4)
L.insert(9)
L.insert(5)

print()
