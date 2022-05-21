from antlr4 import *
from gcodeLexer import gcodeLexer
from gcodeParser import gcodeParser
from gcodeVisitor import gcodeVisitor
import time

def main():
    
    lexer = gcodeLexer (FileStream("gcode_test"))
    token_stream = CommonTokenStream(lexer)
    parser = gcodeParser(token_stream)
    visitor = gcodeVisitor()
	

   
    while True:
         
        tree = parser.start()
        if tree.expr() == None:
            break
        print(tree.toStringTree(recog=parser))
        visitor.visit(tree)

    time.sleep(10)

if __name__ == '__main__':
    main()
