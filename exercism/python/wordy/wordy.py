def answer(question):
    operations = {
        "plus": "+",
        "minus": "-",
        "multiplied by": "*",
        "divided by": "/"
    }

    if any(word in question.lower() for word in ["cube", "squared", "power", "root"]) \
       and not any(op in question.lower() for op in operations):
        raise ValueError("unknown operation")

    expr = question
    for word, op in operations.items():
        expr = expr.replace(word, op)

    expr = ''.join(c for c in expr if c.isdigit() or c in '+-*/ ').strip()

    if not expr:
        raise ValueError("syntax error")

    tokens = expr.split()

    if (len(tokens) % 2 != 1
        or not tokens[0].lstrip('-').isdigit()
        or not tokens[-1].lstrip('-').isdigit()
        or any(tokens[i] not in '+-*/' for i in range(1, len(tokens)-1, 2))
        or any(not tokens[i].lstrip('-').isdigit() for i in range(2, len(tokens), 2))
    ):
        raise ValueError("syntax error")

    if len(tokens) > 3:
        tokens.insert(0, '(')
        tokens.insert(4, ')')

    try:
        return eval(''.join(tokens))
    except:
        raise ValueError("syntax error")