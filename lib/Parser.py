
class Parser():

  # Terminals
  T_LPAR = 0
  T_RPAR = 1
  T_ID = 2
  T_OP = 3
  T_END = 4
  T_NEG = 5
  T_INVALID = 6

  # OPERATORS   = ['~', '^', 'or', '->', '<->']
  # OPERANDS    = ['p', 'q']
  # PARENTHESES = ['(', ')']
  # LEXICON     = OPERATORS + OPERANDS + PARENTHESES

  def __init__(self):
    #self.lexicon = self.operators + self.operands + self.parentheses
    pass

  def lexicalAnalysis(self, inputstring):
    print('Lexical analysis') 
    tokens = []
    i = 0
    while i < len( inputstring ):
        c = inputstring[ i ]
        if c == '-':      # Check '->'
            i += 1
            c = inputstring[ i ]
            tokens.append(self.T_OP if c == '>' else self.T_INVALID)
        elif c == '<':      # Check '<->'
            i += 1
            c = inputstring[i]
            if c == '-':
                i += 1
                c = inputstring[i]
                tokens.append(self.T_OP if c == '>' else self.T_INVALID)
            else: tokens.append(self.T_INVALID)
        elif c == 'v': tokens.append(self.T_OP)
        elif c == '&': tokens.append(self.T_OP)
        elif c == 'p': tokens.append(self.T_ID)
        elif c == 'q': tokens.append(self.T_ID)
        elif c == '(': tokens.append(self.T_LPAR)
        elif c == ')': tokens.append(self.T_RPAR)
        elif c == '~': tokens.append(self.T_NEG)
        else: tokens.append(self.T_INVALID)
        i += 1
    tokens.append(self.T_END)
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