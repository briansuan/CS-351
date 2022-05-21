# Generated from gcode.g4 by ANTLR 4.9
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .gcodeParser import gcodeParser
else:
    from gcodeParser import gcodeParser

# This class defines a complete listener for a parse tree produced by gcodeParser.
class gcodeListener(ParseTreeListener):

    # Enter a parse tree produced by gcodeParser#start.
    def enterStart(self, ctx:gcodeParser.StartContext):
        pass

    # Exit a parse tree produced by gcodeParser#start.
    def exitStart(self, ctx:gcodeParser.StartContext):
        pass


    # Enter a parse tree produced by gcodeParser#draw_G01.
    def enterDraw_G01(self, ctx:gcodeParser.Draw_G01Context):
        pass

    # Exit a parse tree produced by gcodeParser#draw_G01.
    def exitDraw_G01(self, ctx:gcodeParser.Draw_G01Context):
        pass


    # Enter a parse tree produced by gcodeParser#draw_G02.
    def enterDraw_G02(self, ctx:gcodeParser.Draw_G02Context):
        pass

    # Exit a parse tree produced by gcodeParser#draw_G02.
    def exitDraw_G02(self, ctx:gcodeParser.Draw_G02Context):
        pass


    # Enter a parse tree produced by gcodeParser#draw_G28.
    def enterDraw_G28(self, ctx:gcodeParser.Draw_G28Context):
        pass

    # Exit a parse tree produced by gcodeParser#draw_G28.
    def exitDraw_G28(self, ctx:gcodeParser.Draw_G28Context):
        pass



del gcodeParser