# Generated from final.g4 by ANTLR 4.9
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\7")
        buf.write("\24\4\2\t\2\4\3\t\3\4\4\t\4\3\2\3\2\3\2\5\2\f\n\2\3\3")
        buf.write("\3\3\3\3\3\4\3\4\3\4\3\4\2\2\5\2\4\6\2\2\2\22\2\13\3\2")
        buf.write("\2\2\4\r\3\2\2\2\6\20\3\2\2\2\b\f\5\4\3\2\t\f\5\6\4\2")
        buf.write("\n\f\3\2\2\2\13\b\3\2\2\2\13\t\3\2\2\2\13\n\3\2\2\2\f")
        buf.write("\3\3\2\2\2\r\16\7\3\2\2\16\17\7\5\2\2\17\5\3\2\2\2\20")
        buf.write("\21\7\4\2\2\21\22\7\6\2\2\22\7\3\2\2\2\3\13")
        return buf.getvalue()


class finalParser ( Parser ):

    grammarFileName = "final.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'duration'", "'->'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "NUMBER", "PLAYER", 
                      "WS" ]

    RULE_start = 0
    RULE_expr1 = 1
    RULE_expr2 = 2

    ruleNames =  [ "start", "expr1", "expr2" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    NUMBER=3
    PLAYER=4
    WS=5

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class StartContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr1(self):
            return self.getTypedRuleContext(finalParser.Expr1Context,0)


        def expr2(self):
            return self.getTypedRuleContext(finalParser.Expr2Context,0)


        def getRuleIndex(self):
            return finalParser.RULE_start

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

        localctx = finalParser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_start)
        try:
            self.state = 9
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [finalParser.T__0]:
                self.enterOuterAlt(localctx, 1)
                self.state = 6
                self.expr1()
                pass
            elif token in [finalParser.T__1]:
                self.enterOuterAlt(localctx, 2)
                self.state = 7
                self.expr2()
                pass
            elif token in [finalParser.EOF]:
                self.enterOuterAlt(localctx, 3)

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


    class Expr1Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return finalParser.RULE_expr1

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class Get_durationContext(Expr1Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a finalParser.Expr1Context
            super().__init__(parser)
            self.duration = None # Token
            self.copyFrom(ctx)

        def NUMBER(self):
            return self.getToken(finalParser.NUMBER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGet_duration" ):
                listener.enterGet_duration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGet_duration" ):
                listener.exitGet_duration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGet_duration" ):
                return visitor.visitGet_duration(self)
            else:
                return visitor.visitChildren(self)



    def expr1(self):

        localctx = finalParser.Expr1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_expr1)
        try:
            localctx = finalParser.Get_durationContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 11
            self.match(finalParser.T__0)
            self.state = 12
            localctx.duration = self.match(finalParser.NUMBER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr2Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return finalParser.RULE_expr2

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class Get_playersContext(Expr2Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a finalParser.Expr2Context
            super().__init__(parser)
            self.players = None # Token
            self.copyFrom(ctx)

        def PLAYER(self):
            return self.getToken(finalParser.PLAYER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGet_players" ):
                listener.enterGet_players(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGet_players" ):
                listener.exitGet_players(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGet_players" ):
                return visitor.visitGet_players(self)
            else:
                return visitor.visitChildren(self)



    def expr2(self):

        localctx = finalParser.Expr2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_expr2)
        try:
            localctx = finalParser.Get_playersContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 14
            self.match(finalParser.T__1)
            self.state = 15
            localctx.players = self.match(finalParser.PLAYER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





