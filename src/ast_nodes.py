from dataclasses import dataclass
from typing import Optional, List

@dataclass
class Program:
    block: "Block"

@dataclass
class Block:
    stmts: Optional[object]

@dataclass
class Seq:
    first: Optional[object]
    second: object

@dataclass
class Decl:
    typ: str
    is_array: bool
    is_const: bool
    id: "Id"
    init: Optional[object] = None

@dataclass
class Eval:
    expr: object

@dataclass
class Print:
    args: List[object]

@dataclass
class If:
    cond: object
    then_stmt: object
    else_stmt: Optional[object] = None

@dataclass
class While:
    cond: object
    body: object

@dataclass
class Do:
    body: object
    cond: object

@dataclass
class Assign:
    left: object
    right: object

@dataclass
class Rel:
    op: str
    left: object
    right: object

@dataclass
class Eq:
    op: str
    left: object
    right: object

@dataclass
class Lg:
    op: str
    left: object
    right: object

@dataclass
class Unary:
    op: str
    expr: object

@dataclass
class Ari:
    op: str
    left: object
    right: object

@dataclass
class NewArray:
    base: str
    size: object

@dataclass
class ArrayRef:
    id: "Id"
    index: object

@dataclass
class Num:
    value: int

@dataclass
class Bool:
    value: bool

@dataclass
class Id:
    name: str
