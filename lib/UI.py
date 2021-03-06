import lib.Statement as st
import lib.Parser as prs

class UI():
  
  def __init__(self, name):
    self.printHeader(name)

  def run(self):
    stop = False
    while not stop:
      print(50*'-')
      statement = self.readInput()
      print(statement)

      parser = prs.Parser()
      statement.tokens = parser.lexicalAnalysis(statement.sentence)
      if not statement.tokens:
        print(parser.printMsg("syntax_error"))
      else:
        # Statement has acceptable words (and only those)
        print(statement.tokens)

        if parser.checkStructure(statement.sentence):
          print(">>>>>> LAUSE OK")
        else:
          print(parser.printMsg("syntax_error"))

        # TODO
        statement.tree = parser.parseTree(statement.tokens)
        if not statement.tree:
          print(parser.printMsg("syntax_error")) # = EI OLE TAUTOLOGIA?
        else:
          # TODO
          parser.translate(statement)

      print()
      stop = True if input("Lopeta? (k/e): \n") == 'k' else False
      print()
    print("Ohjelma lopetettu.")



  # Reding the input
  def readInput(self):
    l = input("Syötä lause: \n")
    t = input("Tarkista onko lause tautologia? (k/e): \n")
    p = input("Lausemuuttujan p arvo (0/1): \n")
    q = input("Lausemuuttujan q arvo (0/1): \n")
    #p = 0 if t else input("Lausemuuttujan p arvo (0/1): \n")
    #q = 0 if t else input("Lausemuuttujan q arvo (0/1): \n")
    print()
    return st.Statement(l, int(p), int(q), (True if t == 'k' else False))


  # Print header for the program
  def printHeader(self, name):
    length = 50
    print()
    for i in range(6):
      print(int(length/5*i)*'*')
    print(length*'*')
    emptyspace = ((int)(length/2)-3-(int)(len(name)/2))
    print('***' + emptyspace*' ' + name + emptyspace*' ' + '***')
    print(length*'*')
    for i in range(5, -1, -1):
      print(int(length/5*i)*'*')
    print()
