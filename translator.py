import sys

from lexer import tokenize
from parser import Parser
from codegen import generate


def main():

    if len(sys.argv) < 2:

        print(
            "አጠቃቀም: python3 translator.py program.አም"
        )
        return

    filename = sys.argv[1]

    with open(
        filename,
        "r",
        encoding="utf-8"
    ) as f:

        source = f.read()

    tokens = tokenize(source)

    parser = Parser(tokens)

    ast = parser.parse()

    output = generate(ast)

    output_file = filename.replace(
        ".አም",
        ".py"
    )

    with open(
        output_file,
        "w",
        encoding="utf-8"
    ) as f:

        f.write(output)

    print(
        "✅ ተተርጎሟል:",
        output_file
    )


if __name__ == "__main__":
    main()