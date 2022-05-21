# Generated from final.g4 by ANTLR 4.9
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .finalParser import finalParser
else:
    from finalParser import finalParser

# This class defines a complete listener for a parse tree produced by finalParser.
class finalListener(ParseTreeListener):

    # Enter a parse tree produced by finalParser#start.
    def enterStart(self, ctx:finalParser.StartContext):
        pass

    # Exit a parse tree produced by finalParser#start.
    def exitStart(self, ctx:finalParser.StartContext):
        pass


    # Enter a parse tree produced by finalParser#get_duration.
    def enterGet_duration(self, ctx:finalParser.Get_durationContext):
        pass

    # Exit a parse tree produced by finalParser#get_duration.
    def exitGet_duration(self, ctx:finalParser.Get_durationContext):
        pass


    # Enter a parse tree produced by finalParser#get_players.
    def enterGet_players(self, ctx:finalParser.Get_playersContext):
        pass

    # Exit a parse tree produced by finalParser#get_players.
    def exitGet_players(self, ctx:finalParser.Get_playersContext):
        pass



del finalParser