def calc(a, b, op):
    if not (isinstance(a, int) or isinstance(a, float)) or not (
        isinstance(b, int) or isinstance(b, float)
    ):
        raise ValueError

    if op == "/" or op == "*" or op == "+" or op == "-":
        if op == "/":
            return a / b

        elif op == "*":
            return a * b

        elif op == "+":
            return a + b

        elif op == "-":
            return a - b
    else:
        raise TypeError
