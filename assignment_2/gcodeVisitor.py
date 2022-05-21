# Brian Suan
# Generated from gcode.g4 by ANTLR 4.9
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .gcodeParser import gcodeParser
else:
    from gcodeParser import gcodeParser

# This class defines a complete generic visitor for a parse tree produced by gcodeParser.
import turtle
skk = turtle.Turtle()


class gcodeVisitor(ParseTreeVisitor):
    
    # Visit a parse tree produced by gcodeParser#start.
    def visitStart(self, ctx:gcodeParser.StartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gcodeParser#draw_G01.
    def visitDraw_G01(self, ctx:gcodeParser.Draw_G01Context):
        target_x = int(ctx.x_cord.text)
        target_y = int(ctx.y_cord.text)
        cur_pos = skk.pos() 
        
        # Original Algorithm 
        """
        if target_x > cur_pos[0]:
            skk.right(target_x - cur_pos[0])
        else:
            skk.left(cur_pos[0] - target_x)

        if target_y > cur_pos[0]:
            skk.forward(target_y - cur_pos[0])
        else:
            skk.backward(cur_pos[0] - target_y)
        """

        # Fixed Algorithm
        if target_x > cur_pos[0]:
            skk.right(target_x)
        else:
            skk.left(target_x)

        if target_y > 0:
            skk.forward(target_y)
        else:
            skk.backward(target_y)

        return self.visitChildren(ctx)


    # Visit a parse tree produced by gcodeParser#draw_G02.
    def visitDraw_G02(self, ctx:gcodeParser.Draw_G02Context):
        rad = int(ctx.rad.text)
        ext = int(ctx.ext.text)

        skk.circle(rad, ext)

        return self.visitChildren(ctx)


    # Visit a parse tree produced by gcodeParser#draw_G28.
    def visitDraw_G28(self, ctx:gcodeParser.Draw_G28Context):
        target_x = int(ctx.x_cord.text)
        target_y = int(ctx.y_cord.text)
        

        skk.penup()
        skk.goto(target_x, target_y)
        skk.pendown()        
        return self.visitChildren(ctx)

    
del gcodeParser








