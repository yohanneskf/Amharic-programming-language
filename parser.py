from nodes import *


class Parser:

    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def current(self):
        if self.pos < len(self.tokens):
            return self.tokens[self.pos]
        return None

    def eat(self, expected=None):

        tok = self.current()

        if tok is None:
            raise Exception("ስህተት: ያልተጠበቀ EOF")

        if expected and tok[0] != expected:
            raise Exception(
                f"ስህተት: {expected} ተጠበቀ "
                f"ነገር ግን {tok[0]} ተገኘ"
            )

        self.pos += 1
        return tok

    def parse(self):

        statements = []

        while self.current():
            statements.append(self.statement())

        return Program(statements)

    def statement(self):

        tok = self.current()

        if tok[0] == "VAR":
            return self.var_assign()

        elif tok[0] == "PRINT":
            return self.print_stmt()

        elif tok[0] == "IF":
            return self.if_stmt()

        elif tok[0] == "WHILE":
            return self.while_stmt()

        elif tok[0] == "FUNCTION":
            return self.function_def()

        elif tok[0] == "RETURN":
            return self.return_stmt()
        
        elif tok[0] == "ID":

            next_tok = self.tokens[self.pos + 1] \
                if self.pos + 1 < len(self.tokens) \
                else None

            if next_tok and next_tok[0] == "ASSIGN":
                return self.assign_stmt()

            raise Exception(
                f"ስህተት: ያልታወቀ statement {tok}"
            )

        else:
            raise Exception(f"ስህተት: {tok}")

    def block(self):

        statements = []

        self.eat("BEGIN")

        while self.current() and self.current()[0] != "END":
            statements.append(self.statement())

        self.eat("END")

        return statements

    def var_assign(self):

        self.eat("VAR")

        name = self.eat("ID")[1]

        self.eat("ASSIGN")

        value = self.expr()

        return VarAssign(name, value)

    def print_stmt(self):

        self.eat("PRINT")

        self.eat("LPAREN")

        expr = self.expr()

        self.eat("RPAREN")

        return Print(expr)

    def if_stmt(self):

        self.eat("IF")

        condition = self.condition()

        self.eat("COLON")

        body = self.block()

        else_body = None

        if self.current() and self.current()[0] == "ELSE":

            self.eat("ELSE")
            self.eat("COLON")

            else_body = self.block()

        return If(condition, body, else_body)

    def while_stmt(self):

        self.eat("WHILE")

        condition = self.condition()

        self.eat("COLON")

        body = self.block()

        return While(condition, body)

    def function_def(self):

        self.eat("FUNCTION")

        name = self.eat("ID")[1]

        self.eat("LPAREN")

        params = []

        while self.current()[0] != "RPAREN":

            params.append(self.eat("ID")[1])

            if self.current()[0] == "COMMA":
                self.eat("COMMA")

        self.eat("RPAREN")

        self.eat("COLON")

        body = self.block()

        return Function(name, params, body)

    def return_stmt(self):

        self.eat("RETURN")

        return Return(self.expr())

    def condition(self):

        left = self.expr()

        tok = self.current()

        if tok and tok[0] in ("GT", "LT", "EQ"):

            op = self.eat()[1]

            right = self.expr()

            return Compare(left, op, right)

        return left
    
    def assign_stmt(self):

        name = self.eat("ID")[1]

        self.eat("ASSIGN")

        value = self.expr()

        return Assign(name, value)

    def expr(self):

        left = self.term()

        while self.current() and self.current()[0] == "OP":

            op = self.eat("OP")[1]

            right = self.term()

            left = BinOp(left, op, right)

        return left

    def term(self):

        tok = self.current()

        if tok[0] == "NUMBER":
            self.eat("NUMBER")
            return Number(tok[1])

        elif tok[0] == "STRING":
            self.eat("STRING")
            return String(tok[1])

        elif tok[0] == "ID":

            name = self.eat("ID")[1]

            if self.current() and self.current()[0] == "LPAREN":

                self.eat("LPAREN")

                args = []

                while self.current()[0] != "RPAREN":

                    args.append(self.expr())

                    if self.current()[0] == "COMMA":
                        self.eat("COMMA")

                self.eat("RPAREN")

                return Call(name, args)

            return Var(name)

        raise Exception("ስህተት: expression")
    