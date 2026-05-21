from nodes import *


def generate(node):

    if isinstance(node, Program):
        return "\n".join(generate(s) for s in node.statements)

    elif isinstance(node, VarAssign):
        return f"{node.name} = {generate(node.value)}"

    elif isinstance(node, Number):
        return node.value

    elif isinstance(node, String):
        return node.value

    elif isinstance(node, Var):
        return node.name

    elif isinstance(node, BinOp):
        return f"{generate(node.left)} {node.op} {generate(node.right)}"

    elif isinstance(node, Compare):
        return f"{generate(node.left)} {node.op} {generate(node.right)}"

    elif isinstance(node, Print):
        return f"print({generate(node.expr)})"

    elif isinstance(node, Return):
        return f"return {generate(node.value)}"

    elif isinstance(node, Call):

        args = ", ".join(
            generate(a)
            for a in node.args
        )

        return f"{node.name}({args})"

    elif isinstance(node, Function):

        code = (
            f"def {node.name}"
            f"({', '.join(node.params)}):\n"
        )

        for stmt in node.body:
            code += "    " + generate(stmt) + "\n"

        return code.rstrip()

    elif isinstance(node, While):

        code = (
            f"while {generate(node.condition)}:\n"
        )

        for stmt in node.body:
            code += "    " + generate(stmt) + "\n"

        return code.rstrip()

    elif isinstance(node, If):

        code = (
            f"if {generate(node.condition)}:\n"
        )

        for stmt in node.body:
            code += "    " + generate(stmt) + "\n"

        if node.else_body:

            code += "else:\n"

            for stmt in node.else_body:
                code += "    " + generate(stmt) + "\n"

        return code.rstrip()
    
    elif isinstance(node, Assign):

        return (
            f"{node.name} = "
            f"{generate(node.value)}"
        )

    raise Exception(
        f"Unknown node {type(node)}"
    )
