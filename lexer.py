import re

KEYWORDS = {
    "ቁጥር": "VAR",
    "ፃፍ": "PRINT",

    "ከሆነ": "IF",
    "ካልሆነ": "ELSE",

    "ሲሆን": "WHILE",

    "ተግባር": "FUNCTION",
    "መልስ": "RETURN",

    "ጀምር": "BEGIN",
    "ጨርስ": "END"
}

TOKEN_SPEC = [
    ("NUMBER", r"\d+"),
    ("STRING", r'"[^"]*"'),

    ("EQ", r"=="),
    ("GT", r">"),
    ("LT", r"<"),

    ("ASSIGN", r"="),

    ("OP", r"[+\-*/]"),

    ("LPAREN", r"\("),
    ("RPAREN", r"\)"),

    ("COMMA", r","),

    ("COLON", r":"),

    ("ID", r"[\u1200-\u137F_a-zA-Z][\u1200-\u137F_a-zA-Z0-9]*"),

    ("NEWLINE", r"\n"),
    ("SKIP", r"[ \t]+"),
]

pattern = "|".join(
    f"(?P<{name}>{regex})"
    for name, regex in TOKEN_SPEC
)


def tokenize(code):

    tokens = []

    for match in re.finditer(pattern, code):

        kind = match.lastgroup
        value = match.group()

        if kind == "ID" and value in KEYWORDS:
            kind = KEYWORDS[value]

        if kind not in ("NEWLINE", "SKIP"):
            tokens.append((kind, value))

    return tokens