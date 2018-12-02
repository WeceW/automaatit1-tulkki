import sys
import parser

def main():
    tautology = True if '-t' in sys.argv else False
    inputstring = input("   Syötä lause:\n").replace(" ", "")

    tokens, labels = parser.lexer(inputstring)
    if parser.T_INVALID not in tokens:
        print("   Leksikaalinen analyysi ok.")

        # Set the truth-values for variables p & q in list 'labels'
        parser.askTruthValues(labels, tokens)
        
        # Syntactic analysis returns valid parse tree if ok, else 'False'
        parseTree = parser.syntacticAnalysis(tokens, labels)
        if parseTree:
            print("   Syntaktinen analyysi ok.")
            parseTree.printTree()
            
            terms = [] # Use 'terms' as a stack of all the terms from the parse tree (in post order)
            parser.postorder(parseTree, terms)
            
            statement = ' '.join(labels).replace('~ ', '~').replace('( ', '(').replace(' )', ')')
            print("   Lause", statement, "on", "TOSI" if parser.testStatement(terms) else "EPÄTOSI")

            if tautology:
                print("\n   TODO: Tarkista tautologia")
                parser.checkTautology(tokens, labels)

        else:
            print("   Tarkista syntaksi!")
    else: 
        for i, token in enumerate(tokens):
            if parser.T_INVALID == token:
                print("   Tarkista lause, termi nro %d virheellinen (%s)" % (i+1, labels[i]))


if __name__ == '__main__':
    main()