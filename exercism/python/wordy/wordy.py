def answer(question):
    znaki = ('+', '-', '*', '/')
    replacements = {
        "plus": '+',
        "minus": '-',
        "multiplied by": '*',
        "divided by": '/'
    }

    question_lower = question.lower()
    if any(word in question_lower for word in ["cube", "squared", "power", "root"]) \
            and not any(op in question_lower for op in replacements.keys()):
        raise ValueError("unknown operation")

    matem = question
    for old, new in replacements.items():
        matem = matem.replace(old, new)

    matem1 = ''.join(matem[i] for i in range(len(matem)) if matem[i].isdigit() or matem[i] in znaki or matem[i] == ' ')
    matem = matem1.strip()

    if not matem:
        raise ValueError("syntax error")

    matem = matem.split()

    if len(matem) % 2 == 0:
        raise ValueError("syntax error")  

    if not matem[0].lstrip('-').isdigit() or not matem[-1].lstrip('-').isdigit():
        raise ValueError("syntax error")

    for i in range(1, len(matem) - 1, 2):
        if matem[i] not in znaki:
            raise ValueError("syntax error")
        if not matem[i+1].lstrip('-').isdigit():
            raise ValueError("syntax error")

    if len(matem) > 3:
        matem.insert(0, '(')
        matem.insert(4, ')')

    matem_new = ''.join(matem)

    if any(c not in '0123456789+-*/(). ' for c in matem_new):
        raise ValueError("syntax error")

    try:
        result = eval(matem_new)
    except:
        raise ValueError("syntax error")

    return result