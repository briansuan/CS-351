# Generated from final.g4 by ANTLR 4.9
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\7")
        buf.write("*\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\3\2\3\2")
        buf.write("\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\4\6\4\33\n")
        buf.write("\4\r\4\16\4\34\3\5\6\5 \n\5\r\5\16\5!\3\6\6\6%\n\6\r\6")
        buf.write("\16\6&\3\6\3\6\2\2\7\3\3\5\4\7\5\t\6\13\7\3\2\4\5\2\62")
        buf.write(";C\\c|\5\2\13\f\17\17\"\"\2,\2\3\3\2\2\2\2\5\3\2\2\2\2")
        buf.write("\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\3\r\3\2\2\2\5\26\3")
        buf.write("\2\2\2\7\32\3\2\2\2\t\37\3\2\2\2\13$\3\2\2\2\r\16\7f\2")
        buf.write("\2\16\17\7w\2\2\17\20\7t\2\2\20\21\7c\2\2\21\22\7v\2\2")
        buf.write("\22\23\7k\2\2\23\24\7q\2\2\24\25\7p\2\2\25\4\3\2\2\2\26")
        buf.write("\27\7/\2\2\27\30\7@\2\2\30\6\3\2\2\2\31\33\4\62;\2\32")
        buf.write("\31\3\2\2\2\33\34\3\2\2\2\34\32\3\2\2\2\34\35\3\2\2\2")
        buf.write("\35\b\3\2\2\2\36 \t\2\2\2\37\36\3\2\2\2 !\3\2\2\2!\37")
        buf.write("\3\2\2\2!\"\3\2\2\2\"\n\3\2\2\2#%\t\3\2\2$#\3\2\2\2%&")
        buf.write("\3\2\2\2&$\3\2\2\2&\'\3\2\2\2\'(\3\2\2\2()\b\6\2\2)\f")
        buf.write("\3\2\2\2\6\2\34!&\3\b\2\2")
        return buf.getvalue()


class finalLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    NUMBER = 3
    PLAYER = 4
    WS = 5

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'duration'", "'->'" ]

    symbolicNames = [ "<INVALID>",
            "NUMBER", "PLAYER", "WS" ]

    ruleNames = [ "T__0", "T__1", "NUMBER", "PLAYER", "WS" ]

    grammarFileName = "final.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


