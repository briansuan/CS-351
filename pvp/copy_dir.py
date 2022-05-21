from antlr4 import *
from finalLexer import finalLexer
from finalParser import finalParser
from finalVisitor import finalVisitor
import subprocess

def main():
    
    lexer = finalLexer(FileStream('final_test'))
    token_stream = CommonTokenStream(lexer)
    parser = finalParser(token_stream)
    visitor = finalVisitor()

    
    while True:
        tree = parser.start()
        if tree.expr1() == None and tree.expr2() == None:
            break
        print(tree.toStringTree(recog=parser))
        visitor.visit(tree)
        


if __name__ == '__main__':
    main()
    
