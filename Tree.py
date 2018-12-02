
class Tree():

  def __init__(self, data=""):
    self.parent = None
    self.left = None
    self.right = None
    self.data = data

  def addLeft(self, data=""):
    self.left = Tree(data)
    self.left.parent = self
  
  def addRight(self, data=""):
    self.right = Tree(data)
    self.right.parent = self

  def addData(self, data):
    self.data = data

  def getLeft(self):
    return self.left

  def getRight(self):
    return self.right

  def getParent(self):
    if self.parent:
      return self.parent
    else: 
      return self

  def getData(self):
    return self.data

  def printTree(self, depth=0):
    if depth == 0: print('\n   PARSE TREE:\n   ----ROOT (%d): ' % depth, end='')
    print('|', depth*4*' ', self.data)
    if self.left:
      print('   ----left (%d): ' % (depth+1), end='')
      self.left.printTree(depth+1)
    if self.right:
      print('   ---right (%d): ' % (depth+1), end='')
      self.right.printTree(depth+1)
    if depth == 0: print()


  def __str__(self):
    return self.data
