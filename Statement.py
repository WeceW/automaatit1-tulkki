
class Statement:
  def __init__(self, s, p=0, q=0, t=False):
    self.sentence = s
    self.p = p
    self.q = q
    self.checkTautology = t
    self.tokens = []
    # self.tree = ?

  def isTautology(self):
    # TODO (vai meneekö tämä Parseriin, vai selviääkö automaattiesti puuta muodostaessa?)
    return 0

  def __str__(self):
    return "%s\np = %d, \nq = %d, \n%s\n" % (self.sentence, self.p, self.q, ("Testataan tautologia" if self.checkTautology else "Ei testata tautologiaa"))
