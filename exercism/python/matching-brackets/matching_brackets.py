def is_paired(input_string):
    skobki = '(){}[]'
    skobki_l = '({['
    input_string = [inx for inx in input_string if inx in skobki]
    result = True
    stek = []
    for inx in input_string:
        if inx in skobki_l:
            stek.append(inx)
        else:
            if len(stek) != 0 and inx == ')' and stek[-1] == '(':
                stek.pop()
            elif len(stek) != 0 and inx == '}' and stek[-1] == '{':
                stek.pop()
            elif len(stek) != 0 and inx  == ']' and stek[-1] == '[':
                stek.pop()
            else:
                result = False
                break
    else:
        if len(stek) != 0:
            result =False

    return result