# Generated from MiniLang.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,38,142,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,1,0,1,0,1,0,1,1,1,1,5,1,20,8,1,10,1,12,1,23,9,1,1,1,1,1,1,2,1,
        2,1,2,1,2,1,2,1,2,1,2,5,2,34,8,2,10,2,12,2,37,9,2,1,2,1,2,1,2,1,
        2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,49,8,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,
        1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,68,8,2,1,3,3,3,71,8,
        3,1,3,1,3,1,3,3,3,76,8,3,1,3,1,3,1,3,3,3,81,8,3,1,3,1,3,1,4,1,4,
        1,5,1,5,1,5,1,5,1,5,1,5,3,5,93,8,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,
        5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,5,5,116,8,
        5,10,5,12,5,119,9,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,
        1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,3,6,140,8,6,1,6,0,1,10,7,0,2,4,6,
        8,10,12,0,5,1,0,22,23,1,0,8,9,1,0,10,11,1,0,12,15,1,0,16,17,161,
        0,14,1,0,0,0,2,17,1,0,0,0,4,67,1,0,0,0,6,70,1,0,0,0,8,84,1,0,0,0,
        10,92,1,0,0,0,12,139,1,0,0,0,14,15,3,2,1,0,15,16,5,0,0,1,16,1,1,
        0,0,0,17,21,5,1,0,0,18,20,3,4,2,0,19,18,1,0,0,0,20,23,1,0,0,0,21,
        19,1,0,0,0,21,22,1,0,0,0,22,24,1,0,0,0,23,21,1,0,0,0,24,25,5,2,0,
        0,25,3,1,0,0,0,26,68,3,2,1,0,27,68,3,6,3,0,28,29,5,24,0,0,29,30,
        5,3,0,0,30,35,3,10,5,0,31,32,5,4,0,0,32,34,3,10,5,0,33,31,1,0,0,
        0,34,37,1,0,0,0,35,33,1,0,0,0,35,36,1,0,0,0,36,38,1,0,0,0,37,35,
        1,0,0,0,38,39,5,5,0,0,39,40,5,6,0,0,40,68,1,0,0,0,41,42,5,25,0,0,
        42,43,5,3,0,0,43,44,3,10,5,0,44,45,5,5,0,0,45,48,3,4,2,0,46,47,5,
        26,0,0,47,49,3,4,2,0,48,46,1,0,0,0,48,49,1,0,0,0,49,68,1,0,0,0,50,
        51,5,27,0,0,51,52,5,3,0,0,52,53,3,10,5,0,53,54,5,5,0,0,54,55,3,4,
        2,0,55,68,1,0,0,0,56,57,5,28,0,0,57,58,3,4,2,0,58,59,5,27,0,0,59,
        60,5,3,0,0,60,61,3,10,5,0,61,62,5,5,0,0,62,63,5,6,0,0,63,68,1,0,
        0,0,64,65,3,10,5,0,65,66,5,6,0,0,66,68,1,0,0,0,67,26,1,0,0,0,67,
        27,1,0,0,0,67,28,1,0,0,0,67,41,1,0,0,0,67,50,1,0,0,0,67,56,1,0,0,
        0,67,64,1,0,0,0,68,5,1,0,0,0,69,71,5,21,0,0,70,69,1,0,0,0,70,71,
        1,0,0,0,71,72,1,0,0,0,72,75,3,8,4,0,73,74,5,32,0,0,74,76,5,33,0,
        0,75,73,1,0,0,0,75,76,1,0,0,0,76,77,1,0,0,0,77,80,5,34,0,0,78,79,
        5,7,0,0,79,81,3,10,5,0,80,78,1,0,0,0,80,81,1,0,0,0,81,82,1,0,0,0,
        82,83,5,6,0,0,83,7,1,0,0,0,84,85,7,0,0,0,85,9,1,0,0,0,86,87,6,5,
        -1,0,87,88,5,20,0,0,88,93,3,10,5,3,89,90,5,11,0,0,90,93,3,10,5,2,
        91,93,3,12,6,0,92,86,1,0,0,0,92,89,1,0,0,0,92,91,1,0,0,0,93,117,
        1,0,0,0,94,95,10,10,0,0,95,96,7,1,0,0,96,116,3,10,5,11,97,98,10,
        9,0,0,98,99,7,2,0,0,99,116,3,10,5,10,100,101,10,8,0,0,101,102,7,
        3,0,0,102,116,3,10,5,9,103,104,10,7,0,0,104,105,7,4,0,0,105,116,
        3,10,5,8,106,107,10,6,0,0,107,108,5,18,0,0,108,116,3,10,5,7,109,
        110,10,5,0,0,110,111,5,19,0,0,111,116,3,10,5,6,112,113,10,4,0,0,
        113,114,5,7,0,0,114,116,3,10,5,4,115,94,1,0,0,0,115,97,1,0,0,0,115,
        100,1,0,0,0,115,103,1,0,0,0,115,106,1,0,0,0,115,109,1,0,0,0,115,
        112,1,0,0,0,116,119,1,0,0,0,117,115,1,0,0,0,117,118,1,0,0,0,118,
        11,1,0,0,0,119,117,1,0,0,0,120,121,5,3,0,0,121,122,3,10,5,0,122,
        123,5,5,0,0,123,140,1,0,0,0,124,140,5,35,0,0,125,140,5,29,0,0,126,
        140,5,30,0,0,127,128,5,31,0,0,128,129,3,8,4,0,129,130,5,32,0,0,130,
        131,3,10,5,0,131,132,5,33,0,0,132,140,1,0,0,0,133,134,5,34,0,0,134,
        135,5,32,0,0,135,136,3,10,5,0,136,137,5,33,0,0,137,140,1,0,0,0,138,
        140,5,34,0,0,139,120,1,0,0,0,139,124,1,0,0,0,139,125,1,0,0,0,139,
        126,1,0,0,0,139,127,1,0,0,0,139,133,1,0,0,0,139,138,1,0,0,0,140,
        13,1,0,0,0,11,21,35,48,67,70,75,80,92,115,117,139
    ]

class MiniLangParser ( Parser ):

    grammarFileName = "MiniLang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'{'", "'}'", "'('", "','", "')'", "';'", 
                     "'='", "'*'", "'/'", "'+'", "'-'", "'<'", "'<='", "'>'", 
                     "'>='", "'=='", "'!='", "'&&'", "'||'", "'!'", "'const'", 
                     "'int'", "'bool'", "'print'", "'if'", "'else'", "'while'", 
                     "'do'", "'true'", "'false'", "'new'", "'['", "']'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "CONST", "INT", "BOOL", "PRINT", "IF", 
                      "ELSE", "WHILE", "DO", "TRUE", "FALSE", "NEW", "LBRACK", 
                      "RBRACK", "ID", "NUM", "WS", "LINE_COMMENT", "BLOCK_COMMENT" ]

    RULE_program = 0
    RULE_block = 1
    RULE_stmt = 2
    RULE_decl = 3
    RULE_type = 4
    RULE_expr = 5
    RULE_atom = 6

    ruleNames =  [ "program", "block", "stmt", "decl", "type", "expr", "atom" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    CONST=21
    INT=22
    BOOL=23
    PRINT=24
    IF=25
    ELSE=26
    WHILE=27
    DO=28
    TRUE=29
    FALSE=30
    NEW=31
    LBRACK=32
    RBRACK=33
    ID=34
    NUM=35
    WS=36
    LINE_COMMENT=37
    BLOCK_COMMENT=38

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def block(self):
            return self.getTypedRuleContext(MiniLangParser.BlockContext,0)


        def EOF(self):
            return self.getToken(MiniLangParser.EOF, 0)

        def getRuleIndex(self):
            return MiniLangParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = MiniLangParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 14
            self.block()
            self.state = 15
            self.match(MiniLangParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniLangParser.StmtContext)
            else:
                return self.getTypedRuleContext(MiniLangParser.StmtContext,i)


        def getRuleIndex(self):
            return MiniLangParser.RULE_block

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = MiniLangParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 17
            self.match(MiniLangParser.T__0)
            self.state = 21
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 55766419466) != 0):
                self.state = 18
                self.stmt()
                self.state = 23
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 24
            self.match(MiniLangParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MiniLangParser.RULE_stmt

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class StmtBlockContext(StmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniLangParser.StmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def block(self):
            return self.getTypedRuleContext(MiniLangParser.BlockContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmtBlock" ):
                return visitor.visitStmtBlock(self)
            else:
                return visitor.visitChildren(self)


    class StmtDeclContext(StmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniLangParser.StmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def decl(self):
            return self.getTypedRuleContext(MiniLangParser.DeclContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmtDecl" ):
                return visitor.visitStmtDecl(self)
            else:
                return visitor.visitChildren(self)


    class StmtWhileContext(StmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniLangParser.StmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def WHILE(self):
            return self.getToken(MiniLangParser.WHILE, 0)
        def expr(self):
            return self.getTypedRuleContext(MiniLangParser.ExprContext,0)

        def stmt(self):
            return self.getTypedRuleContext(MiniLangParser.StmtContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmtWhile" ):
                return visitor.visitStmtWhile(self)
            else:
                return visitor.visitChildren(self)


    class StmtExprContext(StmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniLangParser.StmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(MiniLangParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmtExpr" ):
                return visitor.visitStmtExpr(self)
            else:
                return visitor.visitChildren(self)


    class StmtPrintContext(StmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniLangParser.StmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def PRINT(self):
            return self.getToken(MiniLangParser.PRINT, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(MiniLangParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmtPrint" ):
                return visitor.visitStmtPrint(self)
            else:
                return visitor.visitChildren(self)


    class StmtDoWhileContext(StmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniLangParser.StmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def DO(self):
            return self.getToken(MiniLangParser.DO, 0)
        def stmt(self):
            return self.getTypedRuleContext(MiniLangParser.StmtContext,0)

        def WHILE(self):
            return self.getToken(MiniLangParser.WHILE, 0)
        def expr(self):
            return self.getTypedRuleContext(MiniLangParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmtDoWhile" ):
                return visitor.visitStmtDoWhile(self)
            else:
                return visitor.visitChildren(self)


    class StmtIfContext(StmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniLangParser.StmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IF(self):
            return self.getToken(MiniLangParser.IF, 0)
        def expr(self):
            return self.getTypedRuleContext(MiniLangParser.ExprContext,0)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniLangParser.StmtContext)
            else:
                return self.getTypedRuleContext(MiniLangParser.StmtContext,i)

        def ELSE(self):
            return self.getToken(MiniLangParser.ELSE, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmtIf" ):
                return visitor.visitStmtIf(self)
            else:
                return visitor.visitChildren(self)



    def stmt(self):

        localctx = MiniLangParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_stmt)
        self._la = 0 # Token type
        try:
            self.state = 67
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                localctx = MiniLangParser.StmtBlockContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 26
                self.block()
                pass
            elif token in [21, 22, 23]:
                localctx = MiniLangParser.StmtDeclContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 27
                self.decl()
                pass
            elif token in [24]:
                localctx = MiniLangParser.StmtPrintContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 28
                self.match(MiniLangParser.PRINT)
                self.state = 29
                self.match(MiniLangParser.T__2)
                self.state = 30
                self.expr(0)
                self.state = 35
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==4:
                    self.state = 31
                    self.match(MiniLangParser.T__3)
                    self.state = 32
                    self.expr(0)
                    self.state = 37
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 38
                self.match(MiniLangParser.T__4)
                self.state = 39
                self.match(MiniLangParser.T__5)
                pass
            elif token in [25]:
                localctx = MiniLangParser.StmtIfContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 41
                self.match(MiniLangParser.IF)
                self.state = 42
                self.match(MiniLangParser.T__2)
                self.state = 43
                self.expr(0)
                self.state = 44
                self.match(MiniLangParser.T__4)
                self.state = 45
                self.stmt()
                self.state = 48
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                if la_ == 1:
                    self.state = 46
                    self.match(MiniLangParser.ELSE)
                    self.state = 47
                    self.stmt()


                pass
            elif token in [27]:
                localctx = MiniLangParser.StmtWhileContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 50
                self.match(MiniLangParser.WHILE)
                self.state = 51
                self.match(MiniLangParser.T__2)
                self.state = 52
                self.expr(0)
                self.state = 53
                self.match(MiniLangParser.T__4)
                self.state = 54
                self.stmt()
                pass
            elif token in [28]:
                localctx = MiniLangParser.StmtDoWhileContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 56
                self.match(MiniLangParser.DO)
                self.state = 57
                self.stmt()
                self.state = 58
                self.match(MiniLangParser.WHILE)
                self.state = 59
                self.match(MiniLangParser.T__2)
                self.state = 60
                self.expr(0)
                self.state = 61
                self.match(MiniLangParser.T__4)
                self.state = 62
                self.match(MiniLangParser.T__5)
                pass
            elif token in [3, 11, 20, 29, 30, 31, 34, 35]:
                localctx = MiniLangParser.StmtExprContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 64
                self.expr(0)
                self.state = 65
                self.match(MiniLangParser.T__5)
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


    class DeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(MiniLangParser.TypeContext,0)


        def ID(self):
            return self.getToken(MiniLangParser.ID, 0)

        def CONST(self):
            return self.getToken(MiniLangParser.CONST, 0)

        def LBRACK(self):
            return self.getToken(MiniLangParser.LBRACK, 0)

        def RBRACK(self):
            return self.getToken(MiniLangParser.RBRACK, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniLangParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniLangParser.RULE_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecl" ):
                return visitor.visitDecl(self)
            else:
                return visitor.visitChildren(self)




    def decl(self):

        localctx = MiniLangParser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 70
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==21:
                self.state = 69
                self.match(MiniLangParser.CONST)


            self.state = 72
            self.type_()
            self.state = 75
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==32:
                self.state = 73
                self.match(MiniLangParser.LBRACK)
                self.state = 74
                self.match(MiniLangParser.RBRACK)


            self.state = 77
            self.match(MiniLangParser.ID)
            self.state = 80
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==7:
                self.state = 78
                self.match(MiniLangParser.T__6)
                self.state = 79
                self.expr(0)


            self.state = 82
            self.match(MiniLangParser.T__5)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(MiniLangParser.INT, 0)

        def BOOL(self):
            return self.getToken(MiniLangParser.BOOL, 0)

        def getRuleIndex(self):
            return MiniLangParser.RULE_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType" ):
                return visitor.visitType(self)
            else:
                return visitor.visitChildren(self)




    def type_(self):

        localctx = MiniLangParser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 84
            _la = self._input.LA(1)
            if not(_la==22 or _la==23):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MiniLangParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class AssignmentContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniLangParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(MiniLangParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)


    class LogicOrContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniLangParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(MiniLangParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicOr" ):
                return visitor.visitLogicOr(self)
            else:
                return visitor.visitChildren(self)


    class UnaryNotContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(MiniLangParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnaryNot" ):
                return visitor.visitUnaryNot(self)
            else:
                return visitor.visitChildren(self)


    class MulDivContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniLangParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(MiniLangParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMulDiv" ):
                return visitor.visitMulDiv(self)
            else:
                return visitor.visitChildren(self)


    class AddSubContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniLangParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(MiniLangParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddSub" ):
                return visitor.visitAddSub(self)
            else:
                return visitor.visitChildren(self)


    class RelationalContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniLangParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(MiniLangParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelational" ):
                return visitor.visitRelational(self)
            else:
                return visitor.visitChildren(self)


    class UnaryMinusContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(MiniLangParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnaryMinus" ):
                return visitor.visitUnaryMinus(self)
            else:
                return visitor.visitChildren(self)


    class EqualityContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniLangParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(MiniLangParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEquality" ):
                return visitor.visitEquality(self)
            else:
                return visitor.visitChildren(self)


    class AtomExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def atom(self):
            return self.getTypedRuleContext(MiniLangParser.AtomContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtomExpr" ):
                return visitor.visitAtomExpr(self)
            else:
                return visitor.visitChildren(self)


    class LogicAndContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniLangParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(MiniLangParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicAnd" ):
                return visitor.visitLogicAnd(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniLangParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 10
        self.enterRecursionRule(localctx, 10, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 92
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [20]:
                localctx = MiniLangParser.UnaryNotContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 87
                self.match(MiniLangParser.T__19)
                self.state = 88
                self.expr(3)
                pass
            elif token in [11]:
                localctx = MiniLangParser.UnaryMinusContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 89
                self.match(MiniLangParser.T__10)
                self.state = 90
                self.expr(2)
                pass
            elif token in [3, 29, 30, 31, 34, 35]:
                localctx = MiniLangParser.AtomExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 91
                self.atom()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 117
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 115
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
                    if la_ == 1:
                        localctx = MiniLangParser.MulDivContext(self, MiniLangParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 94
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 95
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==8 or _la==9):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 96
                        self.expr(11)
                        pass

                    elif la_ == 2:
                        localctx = MiniLangParser.AddSubContext(self, MiniLangParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 97
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 98
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==10 or _la==11):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 99
                        self.expr(10)
                        pass

                    elif la_ == 3:
                        localctx = MiniLangParser.RelationalContext(self, MiniLangParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 100
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 101
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 61440) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 102
                        self.expr(9)
                        pass

                    elif la_ == 4:
                        localctx = MiniLangParser.EqualityContext(self, MiniLangParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 103
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 104
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==16 or _la==17):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 105
                        self.expr(8)
                        pass

                    elif la_ == 5:
                        localctx = MiniLangParser.LogicAndContext(self, MiniLangParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 106
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 107
                        localctx.op = self.match(MiniLangParser.T__17)
                        self.state = 108
                        self.expr(7)
                        pass

                    elif la_ == 6:
                        localctx = MiniLangParser.LogicOrContext(self, MiniLangParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 109
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 110
                        localctx.op = self.match(MiniLangParser.T__18)
                        self.state = 111
                        self.expr(6)
                        pass

                    elif la_ == 7:
                        localctx = MiniLangParser.AssignmentContext(self, MiniLangParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 112
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 113
                        localctx.op = self.match(MiniLangParser.T__6)
                        self.state = 114
                        self.expr(4)
                        pass

             
                self.state = 119
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class AtomContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MiniLangParser.RULE_atom

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class VarRefContext(AtomContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniLangParser.AtomContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(MiniLangParser.ID, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarRef" ):
                return visitor.visitVarRef(self)
            else:
                return visitor.visitChildren(self)


    class NewArrayContext(AtomContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniLangParser.AtomContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NEW(self):
            return self.getToken(MiniLangParser.NEW, 0)
        def type_(self):
            return self.getTypedRuleContext(MiniLangParser.TypeContext,0)

        def LBRACK(self):
            return self.getToken(MiniLangParser.LBRACK, 0)
        def expr(self):
            return self.getTypedRuleContext(MiniLangParser.ExprContext,0)

        def RBRACK(self):
            return self.getToken(MiniLangParser.RBRACK, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNewArray" ):
                return visitor.visitNewArray(self)
            else:
                return visitor.visitChildren(self)


    class ArrayAccessContext(AtomContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniLangParser.AtomContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(MiniLangParser.ID, 0)
        def LBRACK(self):
            return self.getToken(MiniLangParser.LBRACK, 0)
        def expr(self):
            return self.getTypedRuleContext(MiniLangParser.ExprContext,0)

        def RBRACK(self):
            return self.getToken(MiniLangParser.RBRACK, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayAccess" ):
                return visitor.visitArrayAccess(self)
            else:
                return visitor.visitChildren(self)


    class IntLitContext(AtomContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniLangParser.AtomContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUM(self):
            return self.getToken(MiniLangParser.NUM, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIntLit" ):
                return visitor.visitIntLit(self)
            else:
                return visitor.visitChildren(self)


    class BoolLitContext(AtomContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniLangParser.AtomContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def TRUE(self):
            return self.getToken(MiniLangParser.TRUE, 0)
        def FALSE(self):
            return self.getToken(MiniLangParser.FALSE, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoolLit" ):
                return visitor.visitBoolLit(self)
            else:
                return visitor.visitChildren(self)


    class ParenContext(AtomContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniLangParser.AtomContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(MiniLangParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParen" ):
                return visitor.visitParen(self)
            else:
                return visitor.visitChildren(self)



    def atom(self):

        localctx = MiniLangParser.AtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_atom)
        try:
            self.state = 139
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                localctx = MiniLangParser.ParenContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 120
                self.match(MiniLangParser.T__2)
                self.state = 121
                self.expr(0)
                self.state = 122
                self.match(MiniLangParser.T__4)
                pass

            elif la_ == 2:
                localctx = MiniLangParser.IntLitContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 124
                self.match(MiniLangParser.NUM)
                pass

            elif la_ == 3:
                localctx = MiniLangParser.BoolLitContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 125
                self.match(MiniLangParser.TRUE)
                pass

            elif la_ == 4:
                localctx = MiniLangParser.BoolLitContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 126
                self.match(MiniLangParser.FALSE)
                pass

            elif la_ == 5:
                localctx = MiniLangParser.NewArrayContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 127
                self.match(MiniLangParser.NEW)
                self.state = 128
                self.type_()
                self.state = 129
                self.match(MiniLangParser.LBRACK)
                self.state = 130
                self.expr(0)
                self.state = 131
                self.match(MiniLangParser.RBRACK)
                pass

            elif la_ == 6:
                localctx = MiniLangParser.ArrayAccessContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 133
                self.match(MiniLangParser.ID)
                self.state = 134
                self.match(MiniLangParser.LBRACK)
                self.state = 135
                self.expr(0)
                self.state = 136
                self.match(MiniLangParser.RBRACK)
                pass

            elif la_ == 7:
                localctx = MiniLangParser.VarRefContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 138
                self.match(MiniLangParser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[5] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 4)
         




