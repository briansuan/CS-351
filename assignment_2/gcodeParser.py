# Generated from gcode.g4 by ANTLR 4.9
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\b")
        buf.write("\26\4\2\t\2\4\3\t\3\3\2\3\2\5\2\t\n\2\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\5\3\24\n\3\3\3\2\2\4\2\4\2\2\2\26")
        buf.write("\2\b\3\2\2\2\4\23\3\2\2\2\6\t\5\4\3\2\7\t\3\2\2\2\b\6")
        buf.write("\3\2\2\2\b\7\3\2\2\2\t\3\3\2\2\2\n\13\7\3\2\2\13\f\7\6")
        buf.write("\2\2\f\24\7\6\2\2\r\16\7\4\2\2\16\17\7\6\2\2\17\24\7\6")
        buf.write("\2\2\20\21\7\5\2\2\21\22\7\6\2\2\22\24\7\6\2\2\23\n\3")
        buf.write("\2\2\2\23\r\3\2\2\2\23\20\3\2\2\2\24\5\3\2\2\2\4\b\23")
        return buf.getvalue()


class gcodeParser ( Parser ):

    grammarFileName = "gcode.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'G01'", "'G02'", "'G28'", "<INVALID>", 
                     "'-'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "NUMBER", "NEG", "WS" ]

    RULE_start = 0
    RULE_expr = 1

    ruleNames =  [ "start", "expr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    NUMBER=4
    NEG=5
    WS=6

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class StartContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(gcodeParser.ExprContext,0)


        def getRuleIndex(self):
            return gcodeParser.RULE_start

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStart" ):
                listener.enterStart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStart" ):
                listener.exitStart(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStart" ):
                return visitor.visitStart(self)
            else:
                return visitor.visitChildren(self)




    def start(self):

        localctx = gcodeParser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_start)
        try:
            self.state = 6
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [gcodeParser.T__0, gcodeParser.T__1, gcodeParser.T__2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 4
                self.expr()
                pass
            elif token in [gcodeParser.EOF]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return gcodeParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class Draw_G02Context(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gcodeParser.ExprContext
            super().__init__(parser)
            self.rad = None # Token
            self.ext = None # Token
            self.copyFrom(ctx)

        def NUMBER(self, i:int=None):
            if i is None:
                return self.getTokens(gcodeParser.NUMBER)
            else:
                return self.getToken(gcodeParser.NUMBER, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDraw_G02" ):
                listener.enterDraw_G02(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDraw_G02" ):
                listener.exitDraw_G02(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDraw_G02" ):
                return visitor.visitDraw_G02(self)
            else:
                return visitor.visitChildren(self)


    class Draw_G01Context(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gcodeParser.ExprContext
            super().__init__(parser)
            self.x_cord = None # Token
            self.y_cord = None # Token
            self.copyFrom(ctx)

        def NUMBER(self, i:int=None):
            if i is None:
                return self.getTokens(gcodeParser.NUMBER)
            else:
                return self.getToken(gcodeParser.NUMBER, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDraw_G01" ):
                listener.enterDraw_G01(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDraw_G01" ):
                listener.exitDraw_G01(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDraw_G01" ):
                return visitor.visitDraw_G01(self)
            else:
                return visitor.visitChildren(self)


    class Draw_G28Context(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gcodeParser.ExprContext
            super().__init__(parser)
            self.x_cord = None # Token
            self.y_cord = None # Token
            self.copyFrom(ctx)

        def NUMBER(self, i:int=None):
            if i is None:
                return self.getTokens(gcodeParser.NUMBER)
            else:
                return self.getToken(gcodeParser.NUMBER, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDraw_G28" ):
                listener.enterDraw_G28(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDraw_G28" ):
                listener.exitDraw_G28(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDraw_G28" ):
                return visitor.visitDraw_G28(self)
            else:
                return visitor.visitChildren(self)



    def expr(self):

        localctx = gcodeParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_expr)
        try:
            self.state = 17
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [gcodeParser.T__0]:
                localctx = gcodeParser.Draw_G01Context(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 8
                self.match(gcodeParser.T__0)
                self.state = 9
                localctx.x_cord = self.match(gcodeParser.NUMBER)
                self.state = 10
                localctx.y_cord = self.match(gcodeParser.NUMBER)
                pass
            elif token in [gcodeParser.T__1]:
                localctx = gcodeParser.Draw_G02Context(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 11
                self.match(gcodeParser.T__1)
                self.state = 12
                localctx.rad = self.match(gcodeParser.NUMBER)
                self.state = 13
                localctx.ext = self.match(gcodeParser.NUMBER)
                pass
            elif token in [gcodeParser.T__2]:
                localctx = gcodeParser.Draw_G28Context(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 14
                self.match(gcodeParser.T__2)
                self.state = 15
                localctx.x_cord = self.match(gcodeParser.NUMBER)
                self.state = 16
                localctx.y_cord = self.match(gcodeParser.NUMBER)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





