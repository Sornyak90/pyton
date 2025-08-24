def score(word):
    
    
    res = []
    for ch in word.upper():
        if ch in "AEIOULNRST": 
            res.append(1)
        if ch in "DG": 
            res.append(2)
        if ch in "BCMP":
            res.append(3)
        if ch in "FHVWY": 
            res.append(4)
        if ch in "K": 
            res.append(5),
        if ch in "JX": 
            res.append(8),
        if ch in "QZ": 
            res.append(10)

    return sum(res)

print(score("a"))
        
