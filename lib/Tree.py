
# Tämä on vain alustava hahmotelma / copy-paste StackOverflowsta...

class Tree():
  def __init__(self): # Parent-solmu parametrina rakentimelle, eikös silloin linkitys toimi ihan järkevästi?
    # self.parent = ? (Saisiko tähän ympättyä helposti parentin, niin ei tarvitsisi mitään pinojärjestelyä kehitellä?)
    self.left = None
    self.right = None
    self.data = None

  def left(self, tree):
    self.left = tree

  def left(self):
    return self.left

  def right(self, tree):
    self.right = tree

  def right(self):
    return self.right

  def parent(self):
    return self.parent

  def data(self):
    return self.data

  # jne..........


# You can use it like this:
# root = Tree()
# root.data = "root"
# root.left = Tree()
# root.left.data = "left"
# root.right = Tree()
# root.right.data = "right"