grammar MiniLang;

program: block EOF;

block: '{' stmt* '}';

stmt
    : block                                         # StmtBlock
    | decl                                          # StmtDecl
    | 'print' '(' expr (',' expr)* ')' ';'          # StmtPrint
    | 'if' '(' expr ')' stmt ('else' stmt)?         # StmtIf
    | 'while' '(' expr ')' stmt                     # StmtWhile
    | 'do' stmt 'while' '(' expr ')' ';'            # StmtDoWhile
    | expr ';'                                      # StmtExpr
    ;

decl: CONST? type (LBRACK RBRACK)? ID ('=' expr)? ';' ;

type: 'int' | 'bool';

expr
    : expr op=('*'|'/') expr                        # MulDiv
    | expr op=('+'|'-') expr                        # AddSub
    | expr op=('<'|'<='|'>'|'>=') expr              # Relational
    | expr op=('=='|'!=') expr                      # Equality
    | expr op='&&' expr                             # LogicAnd
    | expr op='||' expr                             # LogicOr
    | <assoc=right> expr op='=' expr                # Assignment
    | '!' expr                                      # UnaryNot
    | '-' expr                                      # UnaryMinus
    | atom                                          # AtomExpr
    ;

atom
    : '(' expr ')'              # Paren
    | NUM                       # IntLit
    | 'true'                    # BoolLit
    | 'false'                   # BoolLit
    | 'new' type '[' expr ']'   # NewArray
    | ID '[' expr ']'           # ArrayAccess
    | ID                        # VarRef
    ;

CONST: 'const';
INT: 'int';
BOOL: 'bool';
PRINT: 'print';
IF: 'if';
ELSE: 'else';
WHILE: 'while';
DO: 'do';
TRUE: 'true';
FALSE: 'false';
NEW: 'new';
LBRACK: '[';
RBRACK: ']';
ID: [a-zA-Z_] [a-zA-Z0-9_]*;
NUM: [0-9]+;
WS: [ \t\r\n]+ -> skip;
LINE_COMMENT: '//' ~[\r\n]* -> channel(HIDDEN);
BLOCK_COMMENT: '/*' .*? '*/' -> channel(HIDDEN);
