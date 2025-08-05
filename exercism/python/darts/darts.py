def score(x, y):
    x0, y0 = 0, 0  
    r1 = 1
    r2 = 5
    r3 = 10
    res=0

    dist = ((x)**2 + (y)**2)**0.5

    if dist <= 1:
        res = 10
    elif 1 < dist <= 5:
        res = 5
    elif 5 < dist <= 10:
        res = 1
    else:
        res = 0
    return res

