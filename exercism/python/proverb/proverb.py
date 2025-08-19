def proverb(*elem, **options):
    result_text = []
    if len(elem) < 1:
        return result_text

    opt = options.get('qualifier')
    if len(elem) > 1:
        for i in range(len(elem)-1):
            result_text.append(f"For want of a {elem[i]} the {elem[i+1]} was lost.")
    result_text.append(f"And all for the want of a {opt+" " if opt != None else ""}{elem[0]}.")
    return result_text

