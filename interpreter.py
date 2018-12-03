import sys
import parser

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
    print(' +' + '~'*45 + '+')
    print(' | T U L K K I   L A U S E L O G I I K A L L E |')
    print(' +' + '~'*45 + '+')

    inputstring, tautology = getArgs()
    tokens, labels = parser.lexer(inputstring)
    if parser.T_INVALID not in tokens:
        print("\n   Leksikaalinen analyysi ok.")

        parseTree = parser.syntacticAnalysis(tokens, labels)
        if parseTree:   # (Syntactic analysis returns valid parse tree if ok, else 'False')
            print("   Syntaktinen analyysi ok.")
            parseTree.printTree()
            
            print('   LAUSE:\n  ', inputstring.replace('v', ' v ').replace('&', ' & ').replace('->', ' -> ').replace('< ->', ' <-> '))
            ids = parser.askTruthValues(labels, tokens)
            terms = [] # Use 'terms' as a stack of all the terms from the parse tree (in post order)
            parser.getTermsInPostOrder(parseTree, terms, ids)

            # Form 'pretty' strings for output:
            statement = ' '.join(labels).replace('~ ', '~').replace('( ', '(').replace(' )', ')')
            statementWithThruthValues = statement
            for key, val in ids.items():
                statementWithThruthValues = statementWithThruthValues.replace(key, str(val))
            
            print(' +' + '~'*(len(statement)+28) + '|')
            print(" | Lause", statementWithThruthValues, "ON", "TOSI" if parser.testStatement(terms) else "EPÄTOSI")

            if tautology:
                tautology = parser.checkTautology(parseTree, ids)
                print(" | \n | Lause", statement, "ON TAUTOLOGIA" if tautology else "EI OLE TAUTOLOGIA")
            print(' +' + '~'*(len(statement)+28) + '|')
            print('   Ohjelma lopetettu.')

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
