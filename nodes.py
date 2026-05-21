class Program:
    def __init__(self, statements):
        self.statements = statements


class VarAssign:
    def __init__(self, name, value):
        self.name = name
        self.value = value


class Number:
    def __init__(self, value):
        self.value = value


class String:
    def __init__(self, value):
        self.value = value


class Var:
    def __init__(self, name):
        self.name = name


class BinOp:
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right


class Compare:
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right


class Print:
    def __init__(self, expr):
        self.expr = expr


class If:
    def __init__(self, condition, body, else_body=None):
        self.condition = condition
        self.body = body
        self.else_body = else_body


class While:
    def __init__(self, condition, body):
        self.condition = condition
        self.body = body


class Function:
    def __init__(self, name, params, body):
        self.name = name
        self.params = params
        self.body = body


class Return:
    def __init__(self, value):
        self.value = value


class Call:
    def __init__(self, name, args):
        self.name = name
        self.args = args

class Assign:
    def __init__(self, name, value):
        self.name = name
        self.value = value