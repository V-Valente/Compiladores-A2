# Generated from MiniLang.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .MiniLangParser import MiniLangParser
else:
    from MiniLangParser import MiniLangParser

# This class defines a complete generic visitor for a parse tree produced by MiniLangParser.

class MiniLangVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MiniLangParser#program.
    def visitProgram(self, ctx:MiniLangParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#block.
    def visitBlock(self, ctx:MiniLangParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#StmtBlock.
    def visitStmtBlock(self, ctx:MiniLangParser.StmtBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#StmtDecl.
    def visitStmtDecl(self, ctx:MiniLangParser.StmtDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#StmtPrint.
    def visitStmtPrint(self, ctx:MiniLangParser.StmtPrintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#StmtIf.
    def visitStmtIf(self, ctx:MiniLangParser.StmtIfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#StmtWhile.
    def visitStmtWhile(self, ctx:MiniLangParser.StmtWhileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#StmtDoWhile.
    def visitStmtDoWhile(self, ctx:MiniLangParser.StmtDoWhileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#StmtExpr.
    def visitStmtExpr(self, ctx:MiniLangParser.StmtExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#decl.
    def visitDecl(self, ctx:MiniLangParser.DeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#type.
    def visitType(self, ctx:MiniLangParser.TypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#Assignment.
    def visitAssignment(self, ctx:MiniLangParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#LogicOr.
    def visitLogicOr(self, ctx:MiniLangParser.LogicOrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#UnaryNot.
    def visitUnaryNot(self, ctx:MiniLangParser.UnaryNotContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#MulDiv.
    def visitMulDiv(self, ctx:MiniLangParser.MulDivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#AddSub.
    def visitAddSub(self, ctx:MiniLangParser.AddSubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#Relational.
    def visitRelational(self, ctx:MiniLangParser.RelationalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#UnaryMinus.
    def visitUnaryMinus(self, ctx:MiniLangParser.UnaryMinusContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#Equality.
    def visitEquality(self, ctx:MiniLangParser.EqualityContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#AtomExpr.
    def visitAtomExpr(self, ctx:MiniLangParser.AtomExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#LogicAnd.
    def visitLogicAnd(self, ctx:MiniLangParser.LogicAndContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#Paren.
    def visitParen(self, ctx:MiniLangParser.ParenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#IntLit.
    def visitIntLit(self, ctx:MiniLangParser.IntLitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#BoolLit.
    def visitBoolLit(self, ctx:MiniLangParser.BoolLitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#NewArray.
    def visitNewArray(self, ctx:MiniLangParser.NewArrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#ArrayAccess.
    def visitArrayAccess(self, ctx:MiniLangParser.ArrayAccessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#VarRef.
    def visitVarRef(self, ctx:MiniLangParser.VarRefContext):
        return self.visitChildren(ctx)



del MiniLangParser