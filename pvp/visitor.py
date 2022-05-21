# Generated from final.g4 by ANTLR 4.9
from antlr4 import *
import os
import shutil
import subprocess


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
        #global duration        
        #duration = int(ctx.duration.text)
        
        return self.visitChildren(ctx)


    # Visit a parse tree produced by finalParser#get_player_one.
    def visitGet_player_one(self, ctx:finalParser.Get_player_oneContext):
        dir_1 = str(ctx.player_one.text)
        src = 'player_library'+ '/' +  dir_1
        dest = 'players'
    
        self.copy_players(src, dest)
        
        #print('src: ' + src + '\n' + 'dest: ' + dest)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by finalParser#get_player_n.
    def visitGet_player_n(self, ctx:finalParser.Get_player_nContext):
        dir_n = str(ctx.player_n.text)
        src = 'player_library'+ '/' + dir_n
        dest = 'players'

        self.copy_players(src, dest)

        #print('src: ' + src + '\n' + 'dst: ' + dest)
        return self.visitChildren(ctx)

    
    def copy_players(self, src, dst, *, follow_sym=True):
        if os.path.isdir(dst):
            dst = os.path.join(dst, os.path.basename(src))
        if os.path.isdir(src):
            shutil.copytree(src, dst)
            shutil.copystat(src, dst, follow_symlinks=follow_sym)
        #return dst
    
    #subprocess.call('python run_me.py', timeout=duration, shell=True)

#os.system('python run_me.py')
#subprocess.call('python run_me.py', timeout = 5, shell=True)
del finalParser


















