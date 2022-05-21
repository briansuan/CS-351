# Generated from final.g4 by ANTLR 4.9
from antlr4 import *
import subprocess
import shutil
import os

if __name__ is not None and "." in __name__:
    from .finalParser import finalParser
else:
    from finalParser import finalParser



# This class defines a complete generic visitor for a parse tree produced by finalParser.
class finalVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by finalParser#start.
    def visitStart(self, ctx:finalParser.StartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by finalParser#get_duration.
    def visitGet_duration(self, ctx:finalParser.Get_durationContext):
        global duration
        # Get duration
        self.duration = int(ctx.duration.text)
        
        return self.visitChildren(ctx)


    # Visit a parse tree produced by finalParser#get_players.
    def visitGet_players(self, ctx:finalParser.Get_playersContext):
        # Store each player into a list
        players = ctx.players.text.split('vs')
        dest = 'players'
        strOutput = ''

        #Copy each player into players dir
        for i in range(len(players)):
            src = 'player_library/' + players[i]
            self.copy_players(src, dest)

        # Run game with all players for the specified duration
        try:
            subprocess.call('python run_me.py', timeout = self.duration, shell=True)
        except TimeoutExpired as e:
            strOutput += 'Error: Time limit exceeded, terminated..'
        except Exception as e:
            strOutput += 'Error: ' + str(e) 
        
        return self.visitChildren(ctx)
    
    def copy_players(self, src, dst, *, follow_sym=True):
        if os.path.isdir(dst):
            dst = os.path.join(dst, os.path.basename(src))
        if os.path.isdir(src):
            shutil.copytree(src, dst)
            shutil.copystat(src, dst, follow_symlinks=follow_sym)

        return dst


del finalParser
