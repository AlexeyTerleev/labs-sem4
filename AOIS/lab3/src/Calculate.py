
OPERATORS = {
        '~': (1, lambda x, y: x == y),
        '>': (2, lambda x, y: not x or y),
        '+': (3, lambda x, y: x or y),
        '*': (4, lambda x, y: x and y),
        '!': (5, lambda x: not x)
    }


def parse(formula_string):
    for sign in formula_string:
        if sign in '01':
            yield bool(int(sign))
        if sign in OPERATORS or sign in "()":
            yield sign


def shunting_yard(parsed_formula):
    stack = []
    for token in parsed_formula:
        if token in OPERATORS:
            while stack and stack[-1] != "(" and OPERATORS[token][0] <= OPERATORS[stack[-1]][0]:
                yield stack.pop()
            stack.append(token)
        elif token == ")":
            while stack:
                element = stack.pop()
                if element == "(":
                    break
                yield element
        elif token == "(":
            stack.append(token)
        else:
            yield token
    while stack:
        yield stack.pop()


def calc(polish):
    stack = []
    for token in polish:
        if token in OPERATORS:
            if token == '!':
                first = stack.pop()
                stack.append(OPERATORS[token][1](first))
            else:
                second, first = stack.pop(), stack.pop()
                stack.append(OPERATORS[token][1](first, second))
        else:
            stack.append(token)
    return stack[0]


def solve(formula: str) -> bool:
    return calc(shunting_yard(parse(formula)))
