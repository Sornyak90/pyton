def transpose(text):
    lines = text.split("\n")
    max_len = max(map(len, lines))
    lines = [line.ljust(max_len, "*") for line in lines]
    res = [''.join(row) for row in zip(*lines)]
    new_res = []
    for i in range(len(res)):
        new_string = ''
        current_line = res[i]
        for j in range(len(current_line)):
            if current_line[j] == '*':
                if j < len(current_line) - 1 and any(char != '*' for char in current_line[j+1:]):
                    new_string += ' '
                else:
                    new_string += ''
            else:
                new_string += current_line[j]
        new_res.append(new_string)
    new_res = "\n".join(new_res)
    return new_res

"""
def transpose(text):
    lines = text.split("\n")
    max_len = max(map(len, lines))
    padded_lines = [line.ljust(max_len, "*") for line in lines]
    transposed = [''.join(row) for row in zip(*padded_lines)]
    result = ["".join(c if c != '*' else (' ' if any(ch != '*' for ch in s[j+1:]) else '') for j, c in enumerate(s)) for s in transposed]
    return '\n'.join(result)
    """