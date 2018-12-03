import sys
from Tree import Tree
from itertools import product

# Labels
L_LPAR = '('
L_RPAR = ')'
L_IMPL = '->'
L_EKVA = '<->'
L_NEG  = '~'
L_AND  = '&'
L_OR   = 'v'

#All constants are indexed from 0
Term = 0
Rule = 1

# Terminals
T_LPAR = 0
T_RPAR = 1
T_ID = 2
T_OP = 3
T_END = 4
T_NEG = 5
T_INVALID = 6

# Non-terminals
N_S = 0
N_F = 1 
N_O = 2

#parse table
table = [# (   )  id  op end   ~   invalid
         [ 0,  0,  0,  0,  0,  0, -1], # S
         [ 1, -1,  3, -1, -1,  2, -1], # F
         [-1, -1, -1,  4, -1, -1, -1], # O
]

# Grammar:
# 0: S -> F
# 1: F -> (FOF)
# 2: F -> ~F
# 3: F -> id
# 4: O -> op
rules = [
    [ (Rule, N_F) ],
    [ (Term, T_LPAR), (Rule,N_F), (Rule, N_O), (Rule, N_F), (Term, T_RPAR) ],
    [ (Term, T_NEG),  (Rule, N_F) ],
    [ (Term, T_ID) ], 
    [ (Term, T_OP) ] 
]



###########################################################
########               L E X I C A L               ########
####                  A N A L Y S I S                  ####
###########################################################
def lexer(inputstring):
    tokens = []
    labels = []
    i = 0

    if inputstring[0] != L_LPAR or inputstring[len(inputstring)-1] != L_RPAR:
        return [[T_INVALID], ["lause tulee alkaa merkillä '(' ja päättyä merkkiin ')'"]]

    while i < len( inputstring ):
        c = inputstring[ i ]
        if c == '-':      # Check '->'
            i += 1
            c = inputstring[ i ]
            tokens.append(T_OP if c == '>' else T_INVALID)
            labels.append(L_IMPL if c == '>' else c)
        elif c == '<':      # Check '<->'
            i += 1
            c = inputstring[i]
            if c == '-':
                i += 1
                c = inputstring[i]
                tokens.append(T_OP if c == '>' else T_INVALID)
                labels.append(L_EKVA if c == '>' else c)
            else: 
                tokens.append(T_INVALID)
                labels.append(c)
        elif c == 'v': 
            tokens.append(T_OP)
            labels.append(L_OR)
        elif c == '&': 
            tokens.append(T_OP)
            labels.append(L_AND)
        elif c == 'p': 
            i += 1
            c = inputstring[i]
            if c == '_':
                i += 1
                c = inputstring[i]
                p = 'p_'
                while True:
                    if not c.isdigit(): 
                        i -= 1
                        break
                    p += c
                    i += 1
                    c = inputstring[i]
                tokens.append(T_ID)
                labels.append(p)
            else: 
                tokens.append(T_INVALID)
                labels.append(c)
        elif c == 'q':
            i += 1
            c = inputstring[i]
            if c == '_':
                i += 1
                c = inputstring[i]
                q = 'q_'
                while True:
                    if not c.isdigit(): 
                        i -= 1
                        break
                    q += c
                    i += 1
                    c = inputstring[i]
                tokens.append(T_ID)
                labels.append(q)
            else:
                tokens.append(T_INVALID)
                labels.append(c)
        elif c == '(': 
            tokens.append(T_LPAR)
            labels.append(L_LPAR)
        elif c == ')': 
            tokens.append(T_RPAR)
            labels.append(L_RPAR)
        elif c == '~': 
            tokens.append(T_NEG)
            labels.append(L_NEG)
        else: 
            tokens.append(T_INVALID)
            labels.append(c)
        i += 1
    tokens.append(T_END)
    return (tokens, labels)


###########################################################
########             S Y N T A C T I C             ########
####                  A N A L Y S I S                  ####
###########################################################
def syntacticAnalysis(tokens, labels):
    stack = [(Term,T_END), (Rule,N_S)]
    parsetree = Tree()
    node = parsetree
    position = 0
    while len(stack) > 0:
        (stype, svalue) = stack.pop()
        token = tokens[position]

        if stype == Term:
            node = expandParseTree(node, token, labels, position)
            if svalue == token:
                position += 1
                if token == T_END:
                    return parsetree
            else:
                break

        elif stype == Rule:
            rule = table[svalue][token]
            for r in reversed(rules[rule]):
                stack.append(r)

    return False


###########################################################
########                E X P A N D                ########
####                P A R S E   T R E E                ####
###########################################################
def expandParseTree(node, token, labels, position):
    if token == T_LPAR:
        # print("T_LPAR: Lisää vasen lapsi ja siirry siihen")
        node.addLeft()
        node = node.getLeft()
    elif token == T_OP:
        # print("OP: Lisää data", labels[position], "ja luo/siirry oikeaan lapseen")
        node.addData(labels[position])
        node.addRight()
        node = node.getRight()
    elif token == T_ID:
        # print("ID: Lisää data", labels[position], "ja siirry vanhempaan")
        node.addData(labels[position])
        node = node.getParent()
        while node.getData() == L_NEG:
            # print("Kohdattiin negaatio, siirry edelleen seuraavaan vanhempaan")
            node = node.getParent()
    elif token == T_RPAR:
        # print("T_RPAR: Siirry vanhempaan")
        node = node.getParent()
        while node.getData() == L_NEG:
            # print("Kohdattiin negaatio, siirry edelleen seuraavaan vanhempaan")
            node = node.getParent()
    elif token == T_NEG:
        # print("T_NEG: Lisää data", labels[position], "ja luo/siirry vasempaan lapseen")
        node.addData(labels[position])
        node.addLeft()
        node = node.getLeft()
    return node



###########################################################
########                  P O S T                  ########
####                     O R D E R                     ####
#          (collect values from the parse tree)           #
###########################################################
def getTermsInPostOrder(tree, terms, ids):
    if tree != None:
        getTermsInPostOrder(tree.getLeft(), terms, ids)
        getTermsInPostOrder(tree.getRight(), terms, ids)
        if tree.getData() in ids:
            # add actual thruth value (1/0) instead of a variable name (e.g. p_1)
            terms.append(ids[tree.getData()])
        else:
            terms.append(tree.getData())


###########################################################
########                  T E S T                  ########
####                 S T A T E M E N T                 ####
#                      (true / false)                     #
###########################################################
def testStatement(terms):
    stack = []
    for term in terms:
        if term == L_AND or term == L_OR or term == L_IMPL or term == L_EKVA:
            q = stack.pop()
            p = stack.pop()
            if term == L_AND:
                stack.append(p and q)
            elif term == L_OR:
                stack.append(p or q)
            elif term == L_IMPL:
                stack.append(1 if p == q or q == 1 else 0)
            elif term == L_EKVA:
                stack.append(1 if p == q else 0)
        elif term == L_NEG:
            stack.append(0 if stack.pop() == 1 else 1)
        elif term == 0 or term == 1:
            stack.append(term)
        else:
            # TODO: Invalid term (Such a term should not be encountered at this point though...)
            pass
    return stack.pop()


###########################################################
########                  T E S T                  ########
####                 T A U T O L O G Y                 ####
#                      (true / false)                     #
###########################################################
def checkTautology(parseTree, ids):

    combinations = list(product([0, 1], repeat=len(ids)))
    for comb in combinations:
        c = {}
        for i, key in enumerate(ids.keys()):
            c[key] = comb[i]
        terms = []
        getTermsInPostOrder(parseTree, terms, c)
        if testStatement(terms) == 0:
            return False
    return True


###########################################################
########                   A S K                   ########
####              T R U T H   V A L U E S              ####
###########################################################
def askTruthValues(labels, tokens):
    variables = {}
    for i, token in enumerate(tokens):
        if token == T_ID:
            if labels[i] not in variables:
                while True:
                    val = input("   Anna totuusarvo (0/1) muuttujalle %s: " % (labels[i]))
                    print()
                    if val in ['0', '1']:
                        variables[labels[i]] = int(val)
                        break
                    else:
                        print("\n   Virheellinen totuusarvo!\n   ")
    return variables
