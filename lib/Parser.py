
class Parser():

  lexicon = ['', '~', '^', 'or', '->', '<->', '(', ')', 'p', 'q']

  def __init__(self):
    pass
    #self.lexicon = LEX

  def tokenize(self, statement_str):
    tokens = []
    for part in statement_str.split():
      if part in self.lexicon:
        tokens.append(part)
      else:
        # check each character of parts
        for char in part:
          if char in self.lexicon:
            tokens.append(char)

          # TODO:
          # Now spaces is required to split items with more than 1 character.
          # -> error when the statement is 'p->q' instead of 'p -> q'... :(
          # Should there actually supposed to be used some sort of an automata here?

          elif char != ' ':
            # False symbols, statement not accepted
            return []
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

