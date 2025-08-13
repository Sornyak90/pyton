def decode(string):
    if not string:
        return ''
    
    digit_str = ''
    result = ""
    n = 1
    for char in string:
        if char.isdigit():
            digit_str+=char
            n = int(digit_str)
        else:
            digit_str = ''
            for i in range(n):
                result+=char
            n = 1
    return result





def encode(string):
    if not string:
        return ''

    result = []
    current_char = string[0]
    count = 1

    for char in string[1:]:
        if char == current_char:
            count += 1
        else:
            result.append(str(count) * (count > 1)+ f'{current_char}')
            current_char = char
            count = 1

    result.append(str(count) * (count > 1)+ f'{current_char}')

    return ''.join(result)

print(decode("XYZ"))#, "2A3B4C")