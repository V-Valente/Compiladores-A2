from src.generated.MiniLangParser import MiniLangParser
from src.generated.MiniLangVisitor import MiniLangVisitor
from src.ast_nodes import *

class MiniLangVisitorImpl(MiniLangVisitor):
    
    def visitProgram(self, ctx: MiniLangParser.ProgramContext):
        return Program(self.visit(ctx.block()))

    def visitBlock(self, ctx: MiniLangParser.BlockContext):
        seq = None
        for stmt_ctx in ctx.stmt():
            stmt_node = self.visit(stmt_ctx)
            seq = Seq(seq, stmt_node)
        return Block(seq)

    def visitStmtBlock(self, ctx: MiniLangParser.StmtBlockContext):
        return self.visit(ctx.block())

    def visitStmtDecl(self, ctx: MiniLangParser.StmtDeclContext):
        return self.visit(ctx.decl())

    def visitDecl(self, ctx: MiniLangParser.DeclContext):
        is_const = ctx.CONST() is not None
        typ_str = ctx.type_().getText()
        is_array = ctx.LBRACK() is not None
        name = ctx.ID().getText()
        init = None
        if ctx.expr():
            init = self.visit(ctx.expr())
        return Decl(typ_str, is_array, is_const, Id(name), init)

    def visitStmtPrint(self, ctx: MiniLangParser.StmtPrintContext):
        args = [self.visit(e) for e in ctx.expr()]
        return Print(args)

    def visitStmtIf(self, ctx: MiniLangParser.StmtIfContext):
        cond = self.visit(ctx.expr())
        then_stmt = self.visit(ctx.stmt(0))
        else_stmt = None
        if ctx.ELSE():
            else_stmt = self.visit(ctx.stmt(1))
        return If(cond, then_stmt, else_stmt)

    def visitStmtWhile(self, ctx: MiniLangParser.StmtWhileContext):
        cond = self.visit(ctx.expr())
        body = self.visit(ctx.stmt())
        return While(cond, body)

    def visitStmtDoWhile(self, ctx: MiniLangParser.StmtDoWhileContext):
        body = self.visit(ctx.stmt())
        cond = self.visit(ctx.expr())
        return Do(body, cond)

    def visitStmtExpr(self, ctx: MiniLangParser.StmtExprContext):
        expr = self.visit(ctx.expr())
        return Eval(expr)

    def visitAssignment(self, ctx: MiniLangParser.AssignmentContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        return Assign(left, right)

    def visitMulDiv(self, ctx: MiniLangParser.MulDivContext):
        return Ari(ctx.op.text, self.visit(ctx.expr(0)), self.visit(ctx.expr(1)))

    def visitAddSub(self, ctx: MiniLangParser.AddSubContext):
        return Ari(ctx.op.text, self.visit(ctx.expr(0)), self.visit(ctx.expr(1)))

    def visitRelational(self, ctx: MiniLangParser.RelationalContext):
        op = ctx.op.text
        if op == "<=": op = "≤"
        if op == ">=": op = "≥"
        return Rel(op, self.visit(ctx.expr(0)), self.visit(ctx.expr(1)))

    def visitEquality(self, ctx: MiniLangParser.EqualityContext):
        return Eq(ctx.op.text, self.visit(ctx.expr(0)), self.visit(ctx.expr(1)))

    def visitLogicAnd(self, ctx: MiniLangParser.LogicAndContext):
        return Lg("&&", self.visit(ctx.expr(0)), self.visit(ctx.expr(1)))

    def visitLogicOr(self, ctx: MiniLangParser.LogicOrContext):
        return Lg("||", self.visit(ctx.expr(0)), self.visit(ctx.expr(1)))

    def visitUnaryNot(self, ctx: MiniLangParser.UnaryNotContext):
        return Unary("!", self.visit(ctx.expr()))

    def visitUnaryMinus(self, ctx: MiniLangParser.UnaryMinusContext):
        val = self.visit(ctx.expr())
        if isinstance(val, Num): return Num(-val.value)
        return Unary("-", val)

    def visitParen(self, ctx: MiniLangParser.ParenContext):
        return self.visit(ctx.expr())

    def visitIntLit(self, ctx: MiniLangParser.IntLitContext):
        return Num(int(ctx.getText()))

    def visitBoolLit(self, ctx: MiniLangParser.BoolLitContext):
        return Bool(ctx.getText() == "true")

    def visitVarRef(self, ctx: MiniLangParser.VarRefContext):
        return Id(ctx.getText())

    def visitArrayAccess(self, ctx: MiniLangParser.ArrayAccessContext):
        return ArrayRef(Id(ctx.ID().getText()), self.visit(ctx.expr()))

    def visitNewArray(self, ctx: MiniLangParser.NewArrayContext):
        return NewArray(ctx.type_().getText(), self.visit(ctx.expr()))
