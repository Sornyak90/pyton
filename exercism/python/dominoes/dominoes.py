from copy import deepcopy
def can_chain(dominoes):
    if len(dominoes) == 0:
        return []
    
    i = 0
    while i < len(dominoes):
        if dominoes[i][0] == dominoes[i][1]:
            # Проверяем, есть ли другие вхождения этого числа
            count = 0
            for d in dominoes:
                if d[0] == dominoes[i][0] or d[1] == dominoes[i][0]:
                    count += 1
                    if count > 1: 
                        break
            
            if count > 1:
                del dominoes[i]
                continue 
        i += 1
                
    domino_set = set(domino[i] for domino in dominoes for i in range(len(domino)))
    domino = [[] for i in range(len(domino_set))]
    for _domino in dominoes:
        domino[_domino[0]-1].append(_domino[1])
        domino[_domino[1]-1].append(_domino[0])

    for d in domino:
        if len(d)%2 != 0:
            return None

    domino_copy = deepcopy(domino)
    result = []
    j=0
    status = False
    check = check_clean(domino_copy)
    for i in range(len(domino_copy)):
        
        while check:
            if len(domino_copy[i])== 0:
                break
            result.append((i+1,domino_copy[i][j]))
            _j=domino_copy[i][j]
            del domino_copy[i][j]
            inx = domino_copy[_j-1].index(i+1)
            if inx == -1:
                result = False
                status = True
                break
            del domino_copy[_j-1][inx]
            i=_j-1
            j=0
        if status:
            break
        check = check_clean(domino_copy)
        if result[0][0] == result[-1][-1] and not check:
            return result
        j=0
        domino_copy = deepcopy(domino)
        result = []
       
    return None

def check_clean(array):
    for row in array:
        if len(row) != 0:
            return True
    return False

