import sys

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

# Labels
L_LPAR = '('
L_RPAR = ')'
L_IMPL = '->'
L_EKVA = '<->'
L_NEG  = '~'
L_AND  = '&'
L_OR   = 'v'
L_INVALID = '#'

# Non-terminals
N_S = 0
N_F = 1
N_O = 2

#parse table
table = [# (   )   a   +   $   ~   invalid
         [ 0,  0,  0,  0,  0,  0, -1], # S
         [ 1, -1,  3, -1, -1,  2, -1], # F
         [-1, -1, -1,  4, -1, -1, -1], # O
        ]

rules = [
    [ (Rule, N_F) ],
    [ (Term, T_LPAR), (Rule,N_F), (Rule, N_O), (Rule, N_F), (Term, T_RPAR) ],
    [ (Term, T_NEG),  (Rule, N_F) ],
    [ (Term, T_ID) ], 
    [ (Term, T_OP) ] 
]


stack = [(Term,T_END), (Rule,N_S)]

def lexicalAnalysis(inputstring):
    print('Lexical analysis') 
    tokens = []
    labels = []
    i = 0
    while i < len( inputstring ):
        c = inputstring[ i ]
        if c == '-':      # Check '->'
            i += 1
            c = inputstring[ i ]
            tokens.append(T_OP if c == '>' else T_INVALID)
            labels.append(L_IMPL if c == '>' else L_INVALID)
        elif c == '<':      # Check '<->'
            i += 1
            c = inputstring[i]
            if c == '-':
                i += 1
                c = inputstring[i]
                tokens.append(T_OP if c == '>' else T_INVALID)
                labels.append(L_EKVA if c == '>' else L_INVALID)
            else: 
                tokens.append(T_INVALID)
                labels.append(L_INVALID)
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
                if c.isdigit():
                    p = 'p_'+c
                    i += 1
                    c = inputstring[i]
                    while True:
                        if not c.isdigit(): 
                            i -= 1
                            break
                        p += c
                        i += 1
                        c = inputstring[i]
                    print(p)
                    tokens.append(T_ID)
                    labels.append(p)
                else:
                    tokens.append(T_INVALID)
                    labels.append(L_INVALID)
            else: 
                tokens.append(T_INVALID)
                labels.append(L_INVALID)
        elif c == 'q':
            i += 1
            c = inputstring[i]
            if c == '_':
                i += 1
                c = inputstring[i]
                if c.isdigit():
                    q = 'q_'+c
                    i += 1
                    c = inputstring[i]
                    while True:
                        if not c.isdigit(): 
                            i -= 1
                            break
                        q += c
                        i += 1
                        c = inputstring[i]
                    print(q)
                    tokens.append(T_ID)
                    labels.append(p)
                else:
                    tokens.append(T_INVALID)
                    labels.append(L_INVALID)
            else:
                tokens.append(T_INVALID)
                labels.append(L_INVALID)
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
            labels.append(L_INVALID)
        i += 1
    tokens.append(T_END)
    print(tokens)
    print(labels)
    return tokens

def syntacticAnalysis(tokens):
    print('Syntactic analysis')
    position = 0
    while len(stack) > 0:
        (stype, svalue) = stack.pop()
        token = tokens[position]
        if stype == Term:
            if svalue == token:
                position += 1
                print('pop', svalue)
                if token == T_END:
                    print('input accepted')
            else:
                print('bad term on input:', token)
                break
        elif stype == Rule:
            print('svalue', svalue, 'token', token)
            rule = table[svalue][token]
            print('rule', rule)
            for r in reversed(rules[rule]):
                stack.append(r)
        print('stack', stack)


inputstring = sys.argv[1].replace(" ", "")
print("Input string: " + inputstring )

tokens = lexicalAnalysis( inputstring )

syntacticAnalysis( tokens )

