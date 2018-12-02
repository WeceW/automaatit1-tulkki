import sys
import parser
from copy import deepcopy

#########################################################################
#              T U L K K I   L A U S E L O G I I K A L L E              #
#########################################################################
#                      T o n i    W e c k r o t h                       #
#                    weckroth.toni.j@student.uta.fi                     #
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#  Ohjelma hyväksyy seuraavat komentoriviparametrit:                    #
#      "lause"   : lauselogiikan lause, esim. "(p_1 & (q_1) <-> p_2)"   #
#      -t        : testataan tautologia                                 #
#                                                                       #
#  Mikäli edellä mainittuja komentoriviparametreja ei ole annettu,      #
#  ohjelma kysyy ne erikseen käyttäjältä ohjelman suorituksen aluksi.   #
#                                                                       #
#  Lisäksi ajon aikana kysytään aina muuttujien totuusarvot.            #
#########################################################################

def main():
    inputstring, tautology = getArgs()
    tokens, labels = parser.lexer(inputstring)
    if parser.T_INVALID not in tokens:
        print("   Leksikaalinen analyysi ok.")

        print('   Lause: ', inputstring.replace('v', ' v ').replace('&', ' & ').replace('->', ' -> ').replace('< ->', ' <-> '))
        original_labels = deepcopy(labels)
        # Set the truth-values for variables p & q in list 'labels'
        ids = parser.askTruthValues(labels, tokens)
        
        # Syntactic analysis returns valid parse tree if ok, else 'False'
        parseTree = parser.syntacticAnalysis(tokens, labels)
        if parseTree:
            print("   Syntaktinen analyysi ok.")
            parseTree.printTree()
            
            terms = [] # Use 'terms' as a stack of all the terms from the parse tree (in post order)
            parser.postorder(parseTree, terms)

            statement = ' '.join(labels).replace('~ ', '~').replace('( ', '(').replace(' )', ')')
            print("   Lause", statement, "ON", "TOSI" if parser.testStatement(terms) else "EPÄTOSI")

            if tautology:
                tautology = parser.checkTautology(tokens, original_labels, ids)
                print("   Lause", statement, "ON TAUTOLOGIA" if tautology else "EI OLE TAUTOLOGIA")

        else:
            print("   Tarkista syntaksi!")
    else: 
        for i, token in enumerate(tokens):
            if parser.T_INVALID == token:
                print("   Tarkista lause, termi nro %d virheellinen (%s)" % (i+1, labels[i]))


def getArgs():
    tautology = True if '-t' in sys.argv else False
    if not tautology:
        tautology = True if input("   Testaa tautologia? (k=kyllä):\n   ") == 'k' else False

    inputstring = ''
    if len(sys.argv) > 1:
        i = 1
        while len(sys.argv) > i and sys.argv[i][0] != '(':
            i += 1
        if len(sys.argv) > i and sys.argv[i][0] == '(':
            inputstring = sys.argv[i].replace(" ", "")
    if inputstring == '':
        inputstring = input("   Syötä lause:\n   ").replace(" ", "")

    return (inputstring, tautology)

if __name__ == '__main__':
    main()
