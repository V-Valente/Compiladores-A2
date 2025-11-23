from typing import List, Dict, Any, Tuple
from .ast_nodes import *

class SemanticError(Exception):
    pass

INT  = "int"
BOOL = "bool"

@dataclass(frozen=True)
class Sym:
    name: str
    typ: str
    is_array: bool
    is_const: bool
    scope_depth: int

def check_semantics(prog: Program):
    scopes: List[Dict[str, Sym]] = []
    defs: set[Sym] = set()
    symtab_snapshot: List[Dict[str, Any]] = []

    def push():
        scopes.append({})

    def pop():
        nonlocal defs
        for s in list(defs):
            if s.scope_depth == len(scopes)-1:
                defs.remove(s)
        scopes.pop()

    def declare(name: str, typ: str, is_array: bool, is_const: bool) -> Sym:
        depth = len(scopes)-1
        if name in scopes[-1]:
            raise SemanticError(f"Redeclaração no mesmo escopo: '{name}'.")
        sym = Sym(name, typ, is_array, is_const, depth)
        scopes[-1][name] = sym
        symtab_snapshot.append({
            "name": name,
            "type": typ + ("[]" if is_array else ""),
            "const": is_const,
            "scope_depth": depth
        })
        return sym

    def lookup(name: str) -> Sym:
        for depth in range(len(scopes)-1, -1, -1):
            tab = scopes[depth]
            if name in tab: return tab[name]
        raise SemanticError(f"Variável '{name}' não declarada.")

    def _check_block(node: Block):
        push()
        _check_stmts(node.stmts)
        pop()

    def _check_stmts(node):
        if node is None: return
        if isinstance(node, Seq):
            _check_stmts(node.first)
            _check_stmt(node.second)
        else:
            _check_stmt(node)

    def _check_stmt(node):
        nonlocal defs
        if isinstance(node, Block):
            _check_block(node); return

        if isinstance(node, Decl):
            if not scopes: push()
            sym = declare(node.id.name, node.typ, node.is_array, node.is_const)
            if node.init is not None:
                t, arr = _infer_expr_type(node.init)
                if sym.is_array:
                    if not isinstance(node.init, NewArray):
                        raise SemanticError(f"Inicialização de array '{sym.name}' deve ser 'new {sym.typ}[...]'.")
                    if t != sym.typ or not arr:
                        raise SemanticError(f"Inicialização incompatível em '{sym.name}'.")
                else:
                    if arr:
                        raise SemanticError(f"Variável escalar '{sym.name}' não pode receber array.")
                    if t != sym.typ:
                        raise SemanticError(f"Tipo de '{sym.name}' é {sym.typ}, não {t}.")
                defs.add(sym)
            return

        if isinstance(node, Print):
            for a in node.args: _infer_expr_type(a)
            return

        if isinstance(node, Eval):
            expr = node.expr
            if isinstance(expr, Assign):
                if isinstance(expr.left, Id):
                    sym = lookup(expr.left.name)
                    if sym.is_const:
                        raise SemanticError(f"Não é permitido reatribuir const '{sym.name}'.")
                    tR, aR = _infer_expr_type(expr.right)
                    if sym.is_array:
                        if not aR:
                            raise SemanticError(f"Variável array '{sym.name}' só pode receber array.")
                        if tR != sym.typ:
                            raise SemanticError(f"Tipo base incompatível em '{sym.name}'.")
                    else:
                        if aR:
                            raise SemanticError(f"Variável escalar '{sym.name}' não pode receber array.")
                        if tR != sym.typ:
                            raise SemanticError(f"Tipo de '{sym.name}' é {sym.typ}, não {tR}.")
                    defs.add(sym)
                    return
                elif isinstance(expr.left, ArrayRef):
                    sym = lookup(expr.left.id.name)
                    if not sym.is_array:
                        raise SemanticError(f"'{sym.name}' não é array.")
                    ti, ai = _infer_expr_type(expr.left.index)
                    if ai or ti != INT:
                        raise SemanticError("Índice de array deve ser int.")
                    tR, aR = _infer_expr_type(expr.right)
                    if aR:
                        raise SemanticError("Atribuição de elemento não aceita array.")
                    if tR != sym.typ:
                        raise SemanticError(f"Elemento de '{sym.name}' é {sym.typ}, não {tR}.")
                    if sym not in defs:
                        raise SemanticError(f"Uso de array '{sym.name}' antes de inicialização.")
                    return
            else:
                _infer_expr_type(expr)
                return

        if isinstance(node, Assign):
             pass 

        if isinstance(node, If):
            ct, ca = _infer_expr_type(node.cond)
            if ca or ct != BOOL:
                raise SemanticError("Condição do if deve ser bool.")
            defs_before = set(defs)
            defs_then = set(defs)
            _check_stmt(node.then_stmt)
            defs_after_then = set(defs)
            defs = set(defs_then)
            if node.else_stmt is not None:
                _check_stmt(node.else_stmt)
                defs_after_else = set(defs)
                defs = (defs_after_then & defs_after_else) | (defs_before & defs_after_then & defs_after_else)
            else:
                defs = defs_before
            return

        if isinstance(node, While):
            ct, ca = _infer_expr_type(node.cond)
            if ca or ct != BOOL:
                raise SemanticError("Condição do while deve ser bool.")
            defs_save = set(defs)
            _check_stmt(node.body)
            defs = defs_save
            return

        if isinstance(node, Do):
            _check_stmt(node.body)
            ct, ca = _infer_expr_type(node.cond)
            if ca or ct != BOOL:
                raise SemanticError("Condição do do-while deve ser bool.")
            return

        if isinstance(node, Program):
            _check_block(node.block); return

    def _infer_expr_type(expr) -> Tuple[str, bool]:
        if isinstance(expr, Num):  return (INT, False)
        if isinstance(expr, Bool): return (BOOL, False)
        if isinstance(expr, Id):
            sym = lookup(expr.name)
            if sym.is_array:
                return (sym.typ, True)
            if sym not in defs:
                raise SemanticError(f"Uso de variável '{sym.name}' antes de inicialização.")
            return (sym.typ, False)
        if isinstance(expr, NewArray):
            t, a = _infer_expr_type(expr.size)
            if a or t != INT:
                raise SemanticError("Tamanho do array deve ser int.")
            return (expr.base, True)
        if isinstance(expr, ArrayRef):
            sym = lookup(expr.id.name)
            if not sym.is_array:
                raise SemanticError(f"'{sym.name}' não é array.")
            if sym not in defs:
                raise SemanticError(f"Uso de array '{sym.name}' antes de inicialização.")
            ti, ai = _infer_expr_type(expr.index)
            if ai or ti != INT:
                raise SemanticError("Índice de array deve ser int.")
            return (sym.typ, False)
        if isinstance(expr, Unary):
            t, a = _infer_expr_type(expr.expr)
            if expr.op == "!":
                if a or t != BOOL: raise SemanticError("Operador '!' requer bool.")
                return (BOOL, False)
            if expr.op == "-":
                if a or t != INT:  raise SemanticError("Operador unário '-' requer int.")
                return (INT, False)
        if isinstance(expr, Ari):
            lt, la = _infer_expr_type(expr.left)
            rt, ra = _infer_expr_type(expr.right)
            if la or ra or lt != INT or rt != INT:
                raise SemanticError(f"Operação aritmética '{expr.op}' requer inteiros escalares.")
            return (INT, False)
        if isinstance(expr, Rel):
            lt, la = _infer_expr_type(expr.left)
            rt, ra = _infer_expr_type(expr.right)
            if la or ra or lt != INT or rt != INT:
                raise SemanticError(f"Operação relacional '{expr.op}' requer inteiros escalares.")
            return (BOOL, False)
        if isinstance(expr, Eq):
            lt, la = _infer_expr_type(expr.left)
            rt, ra = _infer_expr_type(expr.right)
            if la or ra or lt != rt:
                raise SemanticError("Comparação requer operandos escalares do mesmo tipo.")
            return (BOOL, False)
        if isinstance(expr, Lg):
            lt, la = _infer_expr_type(expr.left)
            rt, ra = _infer_expr_type(expr.right)
            if la or ra or lt != BOOL or rt != BOOL:
                raise SemanticError(f"Operador lógico '{expr.op}' requer bool.")
            return (BOOL, False)
        if isinstance(expr, Assign):
            return _infer_expr_type(expr.right)
        raise SemanticError(f"Expressão não reconhecida: {type(expr).__name__}")

    _check_block(prog.block)
    return symtab_snapshot

def print_symtab(symtab_snapshot: List[Dict[str, Any]]):
    print("=== TABELA DE SÍMBOLOS ===")
    for row in sorted(symtab_snapshot, key=lambda r: (r["scope_depth"], r["name"])):
        cflag = " const" if row["const"] else ""
        print(f"[escopo {row['scope_depth']}] {row['name']} : {row['type']}{cflag}")
