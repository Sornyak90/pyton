def can_chain(dominoes):
    result = None
    
    if dominoes == []:
        return []

    domino_dict = {}
    for row in dominoes:
        for key in row:
            domino_dict[key] = domino_dict.get(key, 0) + 1

    for value in domino_dict.values():
        if value % 2 != 0:
            return result
    
    count_num = len(domino_dict)
    total_sum = sum(domino_dict.values())
    quotient = total_sum//count_num

    if abs(quotient - count_num) == 1:
        result_domino = [dominoes[0]]
        for rows in dominoes[1:]:
           if result_domino[-1][1] in rows:
            if result_domino[-1][1] == rows[0]:
                result_domino.append(rows)
            else:
                result_domino.append(reversed(rows))

           
            
           
    

    return result

# input_dominoes = [(1, 2), (2, 3), (3, 1), (4, 5), (5, 6), (6, 4)]
input_dominoes = [(1, 2), (3, 1), (2, 3)]
print(can_chain(input_dominoes))
