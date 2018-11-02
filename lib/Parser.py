
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
        for c in part:
          if c in self.lexicon:
            tokens.append(c)

          # TODO:
          # Now spaces is required to split items with more than 1 character.
          # -> error when the statement is 'p->q' instead of 'p -> q'... :(

          elif c != ' ':
            # False symbols, statement not accepted
            return []
    return tokens

  def parseTree(self, tokens):
    return 1
    # return 0 kun error

  def translate(self, tree):
    return 0

