
class Parser():

  OPERATORS   = ['~', '^', 'or', '->', '<->']
  OPERANDS    = ['p', 'q']
  PARENTHESES = ['(', ')']
  LEXICON     = OPERATORS + OPERANDS + PARENTHESES

  def __init__(self):
    #self.lexicon = self.operators + self.operands + self.parentheses
    pass

  def lexicalAnalysis(self, statement_str):
    tokens = []
    st = statement_str.replace(' ', '')
    i = 0
    # TODO: 
    # This loop is now assuming that length of a word 
    # in the lexicon is between 1-3 characters. Could me more general...
    while i < len(st):
      char = st[i]
      if char in self.LEXICON:
        tokens.append(char)
      elif i+1 < len(st):
        i += 1
        char += st[i]
        if char in self.LEXICON:
          tokens.append(char)
        elif i+2 < len(st):
          i += 1
          char += st[i]
          if char in self.LEXICON:
            tokens.append(char)
          else:
            return []
        else:
          return []
      else:
        return []
      i += 1

    return tokens



  """
  Recursively checks if the statement is correctly structured
  e.g. 1. ((p -> q) <-> q)
       2. ((% -> %) <-> %)
       3. Change (% -> %) into % because this belongs to grammar
          Result now (% <-> %)
       4. Repeat until only % left (return True) or something else (return False)
  """
  def checkStructure(self, statement_str):
    st = statement_str.replace('p', '%').replace('q', '%')
    st = self.structureRecursion(st)
    if st == '%':
      return True
    return False

  def structureRecursion(self, st):
    # TODO: Puuttuu konnektiiveja!
    #       Voisiko puun rakentaa tässä samalla rekursoidessa?
    #       Tosin nyt matchataan merkkijonoja kun pitäisi käsitellä varmaankin niitä tokeneita...?
    st_orig = st
    st = st.replace('~%', '%').replace('~%', '%')
    st = st.replace('(% <-> %)', '%').replace('(% -> %)', '%')
    if st != '%' and st_orig != st:
      st = self.structureRecursion(st)
    return st


  def parseTree(self, tokens):
    return 1
    # return 0 kun error

  def translate(self, tree):
    return 0

  def printMsg(self, msg):
    if msg == "syntax_error":
      return "Virheellinen syntaksi. Sallitut sanat ovat " + ", ".join(self.LEXICON)